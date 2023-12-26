from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

# Desativar verificações SSL (não recomendado para produção)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ssl_context.verify_mode = ssl.CERT_NONE

# Detalhes de conexão
vcenter_host = 'your-vcenter-server'
username = 'your-username'
password = 'your-password'

# Conectar ao vCenter
si = SmartConnect(host=vcenter_host, user=username, pwd=password, sslContext=ssl_context)

# Obter objeto de serviço de inventário
content = si.RetrieveContent()

# Substitua 'your-host-name' pelo nome do host real
host_name = 'your-host-name'

# Encontrar o objeto de host pelo nome
host = None
for child_entity in content.rootFolder.childEntity:
    if hasattr(child_entity, 'hostFolder'):
        host_list = child_entity.hostFolder.childEntity
        for h in host_list:
            if h.name == host_name:
                host = h
                break

# Verificar se o host foi encontrado
if host:
    # Obter o objeto de computação do host
    host_compute_resource = host.host[0]
    
    # Obter o objeto de cluster associado
    cluster = host_compute_resource.parent
    cluster_name = cluster.name
    cluster_moid = cluster._moId

    print(f'Cluster Name: {cluster_name}')
    print(f'Cluster MoID: {cluster_moid}')
else:
    print(f'Host {host_name} não encontrado.')

# Desconectar do vCenter
Disconnect(si)
