from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
import time

# Define your job graph
job_graph = {
    "job_a": {
        "script": "/path/to/script_a.sh",
        "dependents": ["job_b", "job_c"]
    },
    "job_b": {
        "script": "/path/to/script_b.sh",
        "dependents": ["job_d"]
    },
    "job_c": {
        "script": "/path/to/script_c.sh",
        "dependents": []
    },
    "job_d": {
        "script": "/path/to/script_d.sh",
        "dependents": []
    }
}

scheduler = BackgroundScheduler()

def run_job(job_id):
    job_info = job_graph[job_id]
    script_path = job_info["script"]

    print(f"Running {job_id} -> {script_path}")
    result = subprocess.run(["/bin/bash", script_path], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"{job_id} succeeded.")
        for dependent_job_id in job_info["dependents"]:
            print(f"Triggering dependent job: {dependent_job_id}")
            run_job(dependent_job_id)
    else:
        print(f"{job_id} failed. Dependents will not run.")
        print("Error:", result.stderr)

# Start the chain by scheduling the root job(s)
# For example, schedule job_a to run every day at 2:30 PM
scheduler.add_job(lambda: run_job("job_a"), trigger='cron', hour=14, minute=30)

scheduler.start()

# Keep alive
try:
    while True:
        time.sleep(10)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
