from pyVim import connect
from pyVmomi import vim

# vCenter connection parameters
vcenter_host = "your-vcenter-host"
vcenter_user = "your-username"
vcenter_password = "your-password"

# VM and disk information
vm_name = "your-vm-name"
disk_label = "Hard disk 1"

# Connect to vCenter server
service_instance = connect.SmartConnectNoSSL(host=vcenter_host, user=vcenter_user, pwd=vcenter_password)

# Find the VM by name
content = service_instance.RetrieveContent()
vm = None
container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
for managed_object_ref in container.view:
    if managed_object_ref.name == vm_name:
        vm = managed_object_ref
        break
container.Destroy()

# Get disk free space
if vm:
    for device in vm.config.hardware.device:
        if isinstance(device, vim.vm.device.VirtualDisk) and device.deviceInfo.label == disk_label:
            free_space = device.backing.disk.freeSpace
            print(f"Free Space on Disk '{disk_label}' of VM '{vm_name}': {free_space} bytes")
            break
    else:
        print(f"Disk '{disk_label}' not found on VM '{vm_name}'.")
else:
    print(f"VM '{vm_name}' not found.")

# Disconnect from vCenter server
connect.Disconnect(service_instance)
