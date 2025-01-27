import subprocess

def az_login_with_sp(client_id, client_secret, tenant_id):
    try:
        # Running the az login with a service principal
        command = [
            'az', 'login', 
            '--service-principal', 
            '--username', client_id,
            '--password', client_secret, 
            '--tenant', tenant_id
        ]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Print the standard output (successful login details)
        print("Service Principal login successful!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Handle errors (e.g., failed login)
        print(f"Error occurred: {e.stderr}")

# Replace with your actual service principal credentials
client_id = 'your-client-id'
client_secret = 'your-client-secret'
tenant_id = 'your-tenant-id'

# Run az login with service principal
az_login_with_sp(client_id, client_secret, tenant_id)
