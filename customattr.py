from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

# Replace these variables with your vCenter details
VCENTER_SERVER = "your-vcenter-server"
USERNAME = "your-username"
PASSWORD = "your-password"
VM_NAME = "your-vm-name"

# Disable SSL verification (useful in development, not recommended for production)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ssl_context.verify_mode = ssl.CERT_NONE

# Connect to vCenter
si = SmartConnect(
    host=VCENTER_SERVER,
    user=USERNAME,
    pwd=PASSWORD,
    sslContext=ssl_context
)

# Search for the VM by name
content = si.RetrieveContent()
vm = None
vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
for vm_obj in vm_view.view:
    if vm_obj.name == VM_NAME:
        vm = vm_obj
        break

# Check if VM is found
if vm is not None:
    # Retrieve custom attributes
    custom_attributes = vm.config.extraConfig
    print(f"Custom Attributes for VM {VM_NAME}:")
    for attribute in custom_attributes:
        print(f"Key: {attribute.key}, Value: {attribute.value}")
else:
    print(f"VM {VM_NAME} not found.")

# Disconnect from vCenter
Disconnect(si)
