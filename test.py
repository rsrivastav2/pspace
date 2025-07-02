def fetch_jobs(db_path):
    conn = connect_db(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT job_name, status, start_time, end_time, duration_minutes FROM Jobs")

    rows = cursor.fetchall()

    print("\n=== Jobs Table ===")
    for row in rows:
        print(f"Job: {row.job_name}, Status: {row.status}, "
              f"Start: {row.start_time}, End: {row.end_time}, Duration (min): {row.duration_minutes}")

    conn.close()
