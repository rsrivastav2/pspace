import paramiko

# === Connection details ===
hostname = "your.unix.server"    # e.g., "192.168.1.100" or "10.0.0.5"
port = 22                        # default SSH port
username = "your_username"      # remote Unix username
password = "your_password"      # remote Unix password

# === Create SSH client ===
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Accept unknown host keys

try:
    # === Connect using username and password ===
    client.connect(
        hostname=hostname,
        port=port,
        username=username,
        password=password,
        timeout=10
    )

    print("[+] Connected successfully!")

    # === Run a test command ===
    stdin, stdout, stderr = client.exec_command("whoami")
    print("Logged in as:", stdout.read().decode().strip())

except paramiko.AuthenticationException:
    print("[-] Authentication failed.")
except Exception as e:
    print(f"[-] Connection error: {e}")
finally:
    client.close()
