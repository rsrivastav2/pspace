import subprocess
import os

# Set the full path to the az executable
az_path = r"C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\wbin\az"  # Adjust based on your system

# Set Service Principal credentials as environment variables
os.environ['AZURE_CLIENT_ID'] = 'your-client-id'
os.environ['AZURE_TENANT_ID'] = 'your-tenant-id'
os.environ['AZURE_CLIENT_SECRET'] = 'your-client-secret'

# Authenticate using the Service Principal
login_command = [
    az_path, "login", "--service-principal", 
    "--username", os.environ['AZURE_CLIENT_ID'], 
    "--password", os.environ['AZURE_CLIENT_SECRET'], 
    "--tenant", os.environ['AZURE_TENANT_ID']
]

# Run the az login command to authenticate
result = subprocess.run(login_command, capture_output=True, text=True)

# Check login result
if result.returncode == 0:
    print("Successfully logged in with Service Principal.")
else:
    print("Login failed:", result.stderr)

# Example command to list Azure subscriptions
list_command = [az_path, "account", "list", "--output", "table"]

# Run the command to list subscriptions
result = subprocess.run(list_command, capture_output=True, text=True)

# Print the output
print(result.stdout)

# Print any errors if occurred
if result.stderr:
    print("Error:", result.stderr)
