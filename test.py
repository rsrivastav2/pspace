 status = "success" if exit_code == 0 else "failed"

    except Exception as e:
        print(f"[{job_name} ERROR]: {str(e)}")
        status = "failed"

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds() / 60  # in minutes
    return status, start_time, end_time, duration


def update_status(conn, job_name, status, start_time, end_time, duration):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Jobs 
        SET status = ?, start_time = ?, end_time = ?, duration_minutes = ?
        WHERE job_name = ?
    """, (status, start_time, end_time, duration, job_name))
    conn.commit()

for job in execution_order:
    status, start_time, end_time, duration = run_job(job, jobs[job])
    update_status(conn, job, status, start_time, end_time, duration)
    
    if status != "success":
        print(f"Stopping execution due to failure in {job}")
        break
