import subprocess
import os

# Set up environment variables for service principal authentication
os.environ['AZURE_CLIENT_ID'] = 'your-client-id'
os.environ['AZURE_TENANT_ID'] = 'your-tenant-id'
os.environ['AZURE_CLIENT_SECRET'] = 'your-client-secret'

command = ["az", "account", "list", "--output", "table"]

result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
