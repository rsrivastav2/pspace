import subprocess
import os

# Set the full path to the az executable (modify the path based on your system)
az_path = r"C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\wbin\az"  # For Windows
# az_path = '/usr/local/bin/az'  # For macOS/Linux, adjust if necessary

# Set Service Principal credentials as environment variables
os.environ['AZURE_CLIENT_ID'] = 'your-client-id'
os.environ['AZURE_TENANT_ID'] = 'your-tenant-id'
os.environ['AZURE_CLIENT_SECRET'] = 'your-client-secret'

# Define your AKS cluster name and resource group
aks_cluster_name = 'your-cluster-name'
resource_group = 'your-resource-group'

# Authenticate using the Service Principal (login)
login_command = [
    az_path, "login", "--service-principal",
    "--username", os.environ['AZURE_CLIENT_ID'],
    "--password", os.environ['AZURE_CLIENT_SECRET'],
    "--tenant", os.environ['AZURE_TENANT_ID']
]

# Run the login command
result = subprocess.run(login_command, capture_output=True, text=True)

# Check login result
if result.returncode == 0:
    print("Successfully logged in with Service Principal.")
else:
    print("Login failed:", result.stderr)

# Update the kubeconfig using az aks get-credentials
get_credentials_command = [
    az_path, "aks", "get-credentials",
    "--name", aks_cluster_name,
    "--resource-group", resource_group,
    "--overwrite-existing"  # Optional: overwrites any existing kubeconfig entries for this cluster
]

# Run the command to update kubeconfig
result = subprocess.run(get_credentials_command, capture_output=True, text=True)

# Check the result
if result.returncode == 0:
    print("Kubeconfig updated successfully.")
else:
    print("Failed to update kubeconfig:", result.stderr)

# Optionally, set the KUBECONFIG environment variable to point to a custom location
os.environ['KUBECONFIG'] = '/path/to/custom/kubeconfig'  # Adjust if using a custom kubeconfig file

# Verify if kubectl can now access the cluster (optional step)
verify_command = ['kubectl', 'get', 'nodes']
verify_result = subprocess.run(verify_command, capture_output=True, text=True)

if verify_result.returncode == 0:
    print("Successfully connected to the AKS cluster.")
    print(verify_result.stdout)  # Output the list of nodes
else:
    print("Failed to connect to the AKS cluster:", verify_result.stderr)
