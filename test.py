from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from unix_trigger import trigger_unix_script

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_job(job_name, cron_expr):
    trigger = CronTrigger.from_crontab(cron_expr)
    scheduler.add_job(
        trigger_unix_script,
        trigger=trigger,
        args=[job_name],
        id=job_name,
        replace_existing=True
    )
    return f"Scheduled job '{job_name}' with cron '{cron_expr}'"

def list_scheduled_jobs():
    return [{
        'id': job.id,
        'next_run': str(job.next_run_time)
    } for job in scheduler.get_jobs()]
