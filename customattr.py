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




#---------------------
from pyVim import connect
from pyVmomi import vim
import ssl

# Desativar a verificação SSL (útil para desenvolvimento, não recomendado para produção)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ssl_context.verify_mode = ssl.CERT_NONE

# Substitua com os detalhes do seu vCenter
VCENTER_SERVER = "seu-vcenter-server"
USERNAME = "seu-usuario"
PASSWORD = "sua-senha"

# Conectar ao vCenter
si = connect.SmartConnect(
    host=VCENTER_SERVER,
    user=USERNAME,
    pwd=PASSWORD,
    sslContext=ssl_context
)

# Obter lista de VMs
content = si.RetrieveContent()
vm_list = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True).view

# Exibir informações sobre VMs
print("Lista de VMs:")
for vm in vm_list:
    print(f"Nome: {vm.name}, Estado: {vm.runtime.powerState}")

# Desconectar do vCenter
connect.Disconnect(si)
----------------
from pyVim import connect
from pyVmomi import vim

def get_disk_free_space(vm, disk_label):
    for device in vm.config.hardware.device:
        if isinstance(device, vim.vm.device.VirtualDisk) and device.deviceInfo.label == disk_label:
            summary = device.backing.disk
            return summary.freeSpace

def main():
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
    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            vm_folder = child.vmFolder
            vm_list = vm_folder.childEntity
            for curr_vm in vm_list:
                if curr_vm.name == vm_name:
                    vm = curr_vm
                    break

    if vm:
        # Get disk free space
        free_space = get_disk_free_space(vm, disk_label)
        print(f"Free Space on Disk '{disk_label}' of VM '{vm_name}': {free_space} bytes")
    else:
        print(f"VM '{vm_name}' not found.")

    # Disconnect from vCenter server
    connect.Disconnect(service_instance)

if __name__ == "__main__":
    main()
