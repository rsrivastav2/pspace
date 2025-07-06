command = f"nohup bash {script_path} > /tmp/{job_name}.log 2>&1 & echo $!"
    stdin, stdout, stderr = ssh.exec_command(command)
    pid = stdout.read().decode().strip()

    print(f"[INFO] Remote job started with PID {pid}")
