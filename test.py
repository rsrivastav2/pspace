
        # Compose the command to run the script in background and get its PID
        remote_cmd = f"nohup {job['command']} > /tmp/{job_name}.log 2>&1 & echo $!"
        stdin, stdout, stderr = ssh.exec_command(remote_cmd)

        pid = stdout.read().decode().strip()

        if not pid.isdigit():
            print(f"[ERROR] Failed to retrieve PID for job '{job_name}'. Output: {pid}")
            return

        print(f"[RUNNING] Job '{job_name}' started on '{job['machine']}' with PID: {pid}")

        # Log to DB
        update_job_run_status(job_name, pid, "Running", time.time())

        ssh.close()
