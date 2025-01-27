get_credentials_command = [
    az_path, "aks", "get-credentials",
    "--name", aks_cluster_name,
    "--resource-group", resource_group,
    "--overwrite-existing"  # Optional: overwrites any existing kubeconfig entries for this cluster
]

# Run the command to update kubeconfig
result = subprocess.run(get_credentials_command, capture_output=True, text=True)
