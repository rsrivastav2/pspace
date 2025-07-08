remote_cmd = f"echo $$; {command}"
        stdin, stdout, stderr = ssh.exec_command(remote_cmd)

        # Get shell PID (1st line of output)
        pid_line = stdout.readline().strip()
        if pid_line.isdigit():
            update_job_pid(job_name, pid_line)
        else:
            print(f"[WARNING] Could not capture PID from output: '{pid_line}'")

        # Read remaining output if needed
        remaining_output = stdout.read().decode()
        error_output = stderr.read().decode()
        exit_code = stdout.channel.recv_exit_status()

        ssh.close()

        print(f"[INFO] Job '{job_name}' finished with exit code: {exit_code}")
        if error_output:
            print(f"[STDERR] {error_output}")
