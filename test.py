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
