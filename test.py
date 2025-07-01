import pyodbc
import subprocess
from collections import defaultdict, deque

# --- Connect to Access DB ---
def connect_db(db_path):
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={db_path};'
    )
    return pyodbc.connect(conn_str)

# --- Load all jobs and dependencies ---
def load_jobs_and_dependencies(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT job_name, command FROM Jobs")
    jobs = {row.job_name: row.command for row in cursor.fetchall()}

    cursor.execute("SELECT job_name, depends_on FROM Dependencies")
    dependencies = defaultdict(list)     # job -> [its predecessors]
    reverse_deps = defaultdict(list)     # job -> [its dependents]
    in_degree = defaultdict(int)

    for row in cursor.fetchall():
        dependencies[row.job_name].append(row.depends_on)
        reverse_deps[row.depends_on].append(row.job_name)
        in_degree[row.job_name] += 1

    return jobs, dependencies, reverse_deps, in_degree

# --- Find dependent jobs of the triggered job ---
def find_all_dependents(start_job, reverse_deps):
    queue = deque([start_job])
    visited = set([start_job])
    result = []

    while queue:
        job = queue.popleft()
        result.append(job)
        for dep in reverse_deps.get(job, []):
            if dep not in visited:
                visited.add(dep)
                queue.append(dep)
    return result

# --- Filter and sort only impacted jobs ---
def resolve_subgraph_order(start_job, all_jobs, dependencies, reverse_deps):
    affected_jobs = find_all_dependents(start_job, reverse_deps)

    # Build reduced graph
    in_degree = defaultdict(int)
    reduced_reverse = defaultdict(list)

    for job in affected_jobs:
        for pred in dependencies.get(job, []):
            if pred in affected_jobs:
                in_degree[job] += 1
                reduced_reverse[pred].append(job)

    queue = deque([j for j in affected_jobs if in_degree[j] == 0])
    ordered = []

    while queue:
        job = queue.popleft()
        ordered.append(job)
        for dep in reduced_reverse[job]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)

    return ordered

# --- Run a shell job ---
def run_job(job_name, command):
    print(f"Running {job_name}: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
        return "success"
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        return "failed"

# --- Update job status ---
def update_status(conn, job_name, status):
    cursor = conn.cursor()
    cursor.execute("UPDATE Jobs SET status = ? WHERE job_name = ?", (status, job_name))
    conn.commit()

# --- Main Trigger Function ---
def trigger_job_with_dependents(db_path, job_to_trigger):
    conn = connect_db(db_path)
    jobs, dependencies, reverse_deps, _ = load_jobs_and_dependencies(conn)

    if job_to_trigger not in jobs:
        print(f"Job {job_to_trigger} not found.")
        return

    execution_order = resolve_subgraph_order(job_to_trigger, jobs, dependencies, reverse_deps)

    print(f"Execution order: {execution_order}")

    for job in execution_order:
        status = run_job(job, jobs[job])
        update_status(conn, job, status)
        if status != "success":
            print(f"Stopping execution due to failure in {job}")
            break

    conn.close()

# === Entry point ===
if __name__ == "__main__":
    db_file = r"C:\path\to\your\jobs.accdb"
    trigger_job_with_dependents(db_file, "test")
