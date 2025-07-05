import pyodbc
import paramiko
import time

DB_PATH = r"your_db_path.accdb"  # Replace with your actual path

# Helper to connect to Access DB
def get_connection():
    return pyodbc.connect(
        rf"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB_PATH};"
    )

# Fetch machine, command, status
def get_job_details(job_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT machine_name, command, status FROM Jobs WHERE job_name = ?", (job_name,))
    row = cursor.fetchone()
    conn.close()

    if row and len(row) >= 3:
        return {
            "machine": row[0],
            "command": row[1],
            "status": row[2]
        }
    else:
        print(f"[ERROR] Job '{job_name}' not found or missing fields.")
        return None

# Update job runtime status
def update_job_run_status(job_name, pid, status, start_time=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Jobs
        SET pid = ?, status = ?, start_time = ?
        WHERE job_name = ?
    """, (pid, status, start_time, job_name))
    conn.commit()
    conn.close()

# 🔷 MAIN: Run Job
def run_job(job_name, username, password):
    job = get_job_details(job_name)
    
    if not job:
        return

    if job["status"] == "Held":
        print(f"[INFO] Job '{job_name}' is on HOLD. Skipping execution.")
        return

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(job["machine"], username=username, password=password)

        # Run script with nohup in background, capture PID
        command = f"nohup {job['command']} > /tmp/{job_name}.log 2>&1 & echo $!"
        stdin, stdout, stderr = ssh.exec_command(command)
        pid = stdout.read().decode().strip()

        print(f"[RUNNING] Job '{job_name}' started on '{job['machine']}' with PID: {pid}")

        # Update job status in DB
        update_job_run_status(job_name, pid, "Running", time.time())

        ssh.close()

    except Exception as e:
        print(f"[ERROR] Failed to run job '{job_name}': {e}")
