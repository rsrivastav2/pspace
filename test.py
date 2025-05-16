import paramiko

hostname = 'your.vm.ip.address'
username = 'azureuser'  # your VM username
private_key_path = '/path/to/your/private/key.pem'  # or .ppk if using PuTTYgen

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect using private key
key = paramiko.RSAKey.from_private_key_file(private_key_path)
ssh.connect(hostname, username=username, pkey=key)

# Run a command
stdin, stdout, stderr = ssh.exec_command('ls -la')
print(stdout.read().decode())

# Close the connection
ssh.close()
