import pyodbc

DB_PATH = r"your_db_path.accdb"  # replace with your actual path

def get_connection():
    return pyodbc.connect(
        rf"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB_PATH};"
    )

def update_job_status(job_name, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Jobs SET status = ? WHERE job_name = ?", (new_status, job_name))
    conn.commit()
    conn.close()
    print(f"Job '{job_name}' updated to status: {new_status}")

def hold_job(job_name):
    update_job_status(job_name, "Held")

def off_hold_job(job_name):
    update_job_status(job_name, "Ready")
