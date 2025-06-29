import subprocess
import json

# Set your parameters
vm_name = "your-vm-name"
resource_group = "your-resource-group"
user_email = "youruser@domain.com"

def run_command(cmd):
    print(f"\n[Running] {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"[Error] {result.stderr}")
    else:
        print(result.stdout)
    return result

def az_login():
    run_command("az login")

def install_aad_extension(vm, rg):
    run_command(f"""
    az vm extension set \
        --publisher Microsoft.Azure.ActiveDirectory \
        --name AADLoginForLinux \
        --resource-group {rg} \
        --vm-name {vm}
    """)

def get_user_object_id(email):
    result = run_command(f"az ad user show --id {email} --query objectId -o tsv")
    return result.stdout.strip()

def assign_vm_role(user_id, vm, rg, role="Virtual Machine Administrator Login"):
    scope_cmd = f"""
    az vm show --name {vm} --resource-group {rg} --query id -o tsv
    """
    vm_id = run_command(scope_cmd).stdout.strip()
    run_command(f"""
    az role assignment create \
        --assignee {user_id} \
        --role "{role}" \
        --scope {vm_id}
    """)

def ssh_into_vm(vm, rg):
    run_command(f"az ssh vm --name {vm} --resource-group {rg}")

# === MAIN EXECUTION ===
az_login()
install_aad_extension(vm_name, resource_group)
user_id = get_user_object_id(user_email)
assign_vm_role(user_id, vm_name, resource_group)
ssh_into_vm(vm_name, resource_group)
