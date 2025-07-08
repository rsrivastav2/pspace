import pyodbc
import paramiko

DB_PATH = r"your_db_path.accdb"  # Replace with actual DB path

def get_connection():
    return pyodbc.connect(
        rf"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB_PATH};"
    )

def get_pid_from_jobs(job_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT pid FROM Jobs WHERE job_name = ?", (job_name,))
    row = cursor.fetchone()
    conn.close()
    return str(row[0]) if row and row[0] else None

def get_machine_from_jil(job_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT machine_name FROM JIL WHERE job_name = ?", (job_name,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row and row[0] else None

def update_job_as_terminated(job_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Jobs
        SET status = 'Terminated', pid = NULL
        WHERE job_name = ?
    """, (job_name,))
    conn.commit()
    conn.close()
    print(f"[UPDATED] Job '{job_name}' status set to 'Terminated'.")

def terminate_job_by_name(job_name, username, password):
    pid = get_pid_from_jobs(job_name)
    machine = get_machine_from_jil(job_name)

    if not pid:
        print(f"[INFO] No PID found for job '{job_name}'.")
        return
    if not machine:
        print(f"[INFO] No machine found for job '{job_name}' in JIL table.")
        return

    try:
        print(f"[INFO] Connecting to '{machine}' to kill PID {pid}...")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(machine, username=username, password=password)

        kill_cmd = f"kill -9 {pid}"
        stdin, stdout, stderr = ssh.exec_command(kill_cmd)

        err = stderr.read().decode().strip()
        out = stdout.read().decode().strip()

        ssh.close()

        if err:
            print(f"[ERROR] Failed to kill PID {pid} on '{machine}': {err}")
        else:
            print(f"[SUCCESS] Killed PID {pid} on '{machine}'.")
            update_job_as_terminated(job_name)

    except Exception as e:
        print(f"[ERROR] Exception while terminating job '{job_name}': {e}")
