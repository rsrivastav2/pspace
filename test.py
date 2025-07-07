cursor.execute("""
    INSERT INTO job_history 
    (job_name, execution_date, start_time, end_time, duration_minutes, status, remarks)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", (job_name, exec_date, start_time, end_time, duration, status, remarks))
