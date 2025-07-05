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
        print(f"Invalid or missing job: {job_name}")
        return None
