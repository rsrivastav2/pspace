import paramiko

# Define SSH login credentials (you can pull these from DB or config if needed)
REMOTE_HOST = "192.168.1.101"
USERNAME = "unixuser"
PASSWORD = "your_password"  # ❗ Avoid hardcoding in production

def run_job(job_name, command):
    print(f"[{job_name}] Running remotely with password: {command}")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect using username and password
        ssh.connect(hostname=REMOTE_HOST, username=USERNAME, password=PASSWORD)

        stdin, stdout, stderr = ssh.exec_command(command)
        exit_code = stdout.channel.recv_exit_status()

        out = stdout.read().decode()
        err = stderr.read().decode()

        print(out)
        if err:
            print(f"[{job_name} STDERR]: {err}")

        ssh.close()
        return "success" if exit_code == 0 else "failed"

    except Exception as e:
        print(f"[{job_name} ERROR]: {str(e)}")
        return "failed"
