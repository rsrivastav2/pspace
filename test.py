import pyodbc
import paramiko

DB_PATH = r"your_db_path.accdb"  # Replace with your actual path

def get_connection():
    return pyodbc.connect(
        rf"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB_PATH};"
    )

def get_job_pid_and_machine(job_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT pid, machine_name FROM Jobs WHERE job_name = ?", (job_name,))
    row = cursor.fetchone()
    conn.close()

    if row and row[0] and row[1]:
        return {"pid": str(row[0]), "machine": row[1]}
    else:
        print(f"[INFO] No PID or machine found for job '{job_name}'")
        return None

def update_job_status_terminated(job_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Jobs
        SET pid = NULL, status = 'Terminated'
        WHERE job_name = ?
    """, (job_name,))
    conn.commit()
    conn.close()
    print(f"[UPDATED] Job '{job_name}' marked as Terminated and PID cleared.")

def terminate_job_by_name(job_name, username, password):
    job = get_job_pid_and_machine(job_name)
    if not job:
        return

    pid = job["pid"]
    machine = job["machine"]

    try:
        print(f"[INFO] Attempting to kill PID {pid} on machine {machine}...")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(machine, username=username, password=password)

        # Run kill command
        kill_cmd = f"kill -9 {pid}"
        stdin, stdout, stderr = ssh.exec_command(kill_cmd)

        err = stderr.read().decode().strip()
        out = stdout.read().decode().strip()

        ssh.close()

        if err:
            print(f"[ERROR] Failed to kill PID {pid}: {err}")
        else:
            print(f"[SUCCESS] Killed PID {pid} on {machine}")
            update_job_status_terminated(job_name)

    except Exception as e:
        print(f"[ERROR] Exception during termination: {e}")
