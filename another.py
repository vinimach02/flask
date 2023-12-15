import requests

# vCenter connection parameters
vcenter_host = "your-vcenter-host"
vcenter_user = "your-username"
vcenter_password = "your-password"

# VM and disk information
vm_id = "your-vm-id"
disk_id = "your-disk-id"

# Authentication and obtaining the session token
auth_url = f"https://{vcenter_host}/rest/com/vmware/cis/session"
auth_response = requests.post(auth_url, auth=(vcenter_user, vcenter_password), verify=False)
auth_token = auth_response.json()["value"]

# Get capacity information for the specified disk
capacity_url = f"https://{vcenter_host}/rest/vcenter/vm/{vm_id}/hardware/disk/{disk_id}/capacity"
capacity_response = requests.get(capacity_url, headers={"vmware-api-session-id": auth_token}, verify=False)
capacity = capacity_response.json()["value"]

# Get used space information for the specified disk
used_space_url = f"https://{vcenter_host}/rest/vcenter/vm/{vm_id}/hardware/disk/{disk_id}"
used_space_response = requests.get(used_space_url, headers={"vmware-api-session-id": auth_token}, verify=False)
used_space = used_space_response.json()["value"]

# Calculate free space by subtracting used space from capacity
free_space = capacity - used_space

# Print the results
print(f"Capacity: {capacity} bytes")
print(f"Used Space: {used_space} bytes")
print(f"Free Space: {free_space} bytes")
