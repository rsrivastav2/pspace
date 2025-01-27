import subprocess
import os

# Set the Service Principal credentials as environment variables
os.environ['AZURE_CLIENT_ID'] = 'your-client-id'
os.environ['AZURE_TENANT_ID'] = 'your-tenant-id'
os.environ['AZURE_CLIENT_SECRET'] = 'your-client-secret'

# Use az login to authenticate using the service principal
command = ["az", "login", "--service-principal", "--username", os.environ['AZURE_CLIENT_ID'], 
           "--password", os.environ['AZURE_CLIENT_SECRET'], "--tenant", os.environ['AZURE_TENANT_ID']]

# Run the az login command to authenticate
result = subprocess.run(command, capture_output=True, text=True)

# Check if login was successful
if result.returncode == 0:
    print("Successfully logged in with Service Principal")
else:
    print("Login failed:", result.stderr)

# Now, you can run other az commands as needed.
# Example command to list Azure subscriptions
command = ["az", "account", "list", "--output", "table"]

result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print(result.stdout)

# If there's any error, print the error
if result.stderr:
    print("Error:", result.stderr)
