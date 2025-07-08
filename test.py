stdin, stdout, stderr = ssh.exec_command(kill_cmd)

exit_code = stdout.channel.recv_exit_status()
err = stderr.read().decode().strip()
out = stdout.read().decode().strip()

ssh.close()

if exit_code == 0:
    print(f"[SUCCESS] PID {pid} killed on '{machine}'. Exit Code: {exit_code}")
    update_job_as_terminated(job_name)
else:
    print(f"[ERROR] Failed to kill PID {pid} on '{machine}'. Exit Code: {exit_code}")
    if err:
        print(f"stderr: {err}")
    if out:
        print(f"stdout: {out}")
