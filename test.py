def get_job_details(job_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT machine_name, command, status FROM Jobs WHERE job_name = ?", (job_name,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {
            "machine": result[0],
            "command": result[1],
            "status": result[2]
        }
    return None
