import subprocess

def az_login():
    try:
        # Run az login interactively
        result = subprocess.run(['az', 'login'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Output the result (successful login details)
        print("Login successful!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Handle errors (e.g., failed login)
        print(f"Error occurred: {e.stderr}")

# Run az login interactively
az_login()
