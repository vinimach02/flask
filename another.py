import requests

def get_disk_info(auth_token, vcenter_host, vm_id, disk_id):
    capacity_url = f"https://{vcenter_host}/rest/vcenter/vm/{vm_id}/hardware/disk/{disk_id}/capacity"
    used_space_url = f"https://{vcenter_host}/rest/vcenter/vm/{vm_id}/hardware/disk/{disk_id}"

    capacity_response = requests.get(capacity_url, headers={"vmware-api-session-id": auth_token}, verify=False)
    used_space_response = requests.get(used_space_url, headers={"vmware-api-session-id": auth_token}, verify=False)

    capacity_response.raise_for_status()
    used_space_response.raise_for_status()

    capacity = capacity_response.json()["value"]
    used_space = used_space_response.json()["value"]

    return capacity, used_space

def main():
    # vCenter connection parameters
    vcenter_host = "your-vcenter-host"

    # VM and disk information
    vm_id = "your-vm-id"
    disk_id = "your-disk-id"

    # Replace 'your-auth-token' with the actual authentication token
    auth_token = "your-auth-token"

    try:
        # Get disk information
        capacity, used_space = get_disk_info(auth_token, vcenter_host, vm_id, disk_id)

        # Calculate free space
        free_space = capacity - used_space

        # Print the results
        print(f"Capacity: {capacity} bytes")
        print(f"Used Space: {used_space} bytes")
        print(f"Free Space: {free_space} bytes")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
    
#### ------------------------------------
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

# Desativando a verificação SSL (somente para testes, não use em ambientes de produção sem verificar certificados)
ssl._create_default_https_context = ssl._create_unverified_context

# Configurações de conexão
vcenter_host = "<VCENTER_HOST>"
username = "<SEU_USUARIO>"
password = "<SUA_SENHA>"

# Conectando ao vCenter
si = SmartConnect(host=vcenter_host, user=username, pwd=password, port=443)

# Obtendo o conteúdo do ServiceInstance (root folder)
content = si.RetrieveContent()

# Obtendo todos os objetos de máquina virtual
vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
vms = vm_view.view

# Iterando sobre as máquinas virtuais
for vm in vms:
    # Obtendo o nome da máquina virtual
    vm_name = vm.summary.config.name

    # Obtendo o nome do host (ESXi) no qual a máquina virtual está sendo executada
    host_name = vm.runtime.host.summary.config.name

    # Imprimindo as informações
    print(f"Nome da VM: {vm_name}, Nome do Host: {host_name}")

# Desconectando do vCenter
Disconnect(si)

