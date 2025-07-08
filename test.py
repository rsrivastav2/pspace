pid = None
        for line in out.splitlines():
            if line.startswith("PID="):
                pid = line.replace("PID=", "").strip()

        ssh.close()
