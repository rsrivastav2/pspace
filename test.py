# Step 2: Set the subscription
set_subscription_command = [
    az_path, "account", "set", "--subscription", subscription_id
]

# Run the set subscription command
result = subprocess.run(set_subscription_command, capture_output=True, text=True)
