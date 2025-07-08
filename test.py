from apscheduler.schedulers.background import BackgroundScheduler
import time

# Your run_job() should look like this:
# def run_job(job_name, command, machine, username, password)

scheduler = BackgroundScheduler()

def schedule_all_jobs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT job_name, schedule_time FROM Jobs WHERE status != 'Held'")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        job_name = row[0]
        schedule_time = row[1]  # assume it's a cron expression or datetime string

        # Optional: get machine/command from JIL if needed here
        job_details = get_job_details(job_name)
        if not job_details:
            continue

        scheduler.add_job(
            func=run_job,
            trigger='date',  # Or 'cron' or 'interval'
            run_date=schedule_time,
            args=[job_name, job_details['command'], job_details['machine'], "username", "password"],
            id=job_name,
            replace_existing=True
        )
        print(f"[SCHEDULED] Job '{job_name}' at {schedule_time}")

scheduler.start()
