from pyVim import connect
from pyVmomi import vim

def get_vmware_session(vcenter_host, username, password):
    # Connect to vCenter
    service_instance = connect.SmartConnectNoSSL(
        host=vcenter_host,
        user=username,
        pwd=password,
    )
    return service_instance

def get_esxi_host_info(service_instance, host_name):
    # Retrieve ESXi host by name
    host_view = service_instance.content.viewManager.CreateContainerView(
        service_instance.content.rootFolder,
        [vim.HostSystem],
        True
    )
    esxi_host = None
    for host in host_view.view:
        if host_name == host.summary.config.name:
            esxi_host = host
            break
    host_view.Destroy()
    return esxi_host

def get_cluster_info(service_instance, cluster_name):
    # Retrieve cluster by name
    cluster_view = service_instance.content.viewManager.CreateContainerView(
        service_instance.content.rootFolder,
        [vim.ClusterComputeResource],
        True
    )
    cluster = None
    for cl in cluster_view.view:
        if cluster_name == cl.name:
            cluster = cl
            break
    cluster_view.Destroy()
    return cluster

def get_host_performance_metrics(esxi_host):
    # Retrieve performance manager
    perf_manager = esxi_host.parent.parent.content.perfManager

    # Specify performance counters for CPU and Memory
    counters = perf_manager.QueryPerfCounterByLevel(
        level=1
    )

    # Filter for CPU and Memory counters
    cpu_counter = next(counter for counter in counters if counter.groupInfo.key == 'cpu' and counter.nameInfo.key == 'usage')
    memory_counter = next(counter for counter in counters if counter.groupInfo.key == 'mem' and counter.nameInfo.key == 'usage')

    # Query performance stats
    query = vim.PerformanceManager.QuerySpec(
        entity=esxi_host,
        metricId=[
            vim.PerformanceManager.MetricId(counterId=cpu_counter.key),
            vim.PerformanceManager.MetricId(counterId=memory_counter.key)
        ],
        format='normal'
    )

    stats = perf_manager.QueryPerf(querySpec=[query])

    # Print performance stats
    for val in stats[0].value[0].value:
        print(f"{val.id.counterId}: {val.value[0]}")

if __name__ == "__main__":
    vcenter_host = "your_vcenter_host"
    username = "your_username"
    password = "your_password"
    host_name = "your_esxi_host_name"
    cluster_name = "your_cluster_name"

    # Establish a session with vCenter
    service_instance = get_vmware_session(vcenter_host, username, password)

    # Get ESXi host information
    esxi_host = get_esxi_host_info(service_instance, host_name)
    if esxi_host:
        print(f"ESXi Host Information:")
        print(f"Name: {esxi_host.summary.config.name}")
        print(f"CPU Cores: {esxi_host.hardware.cpuInfo.numCpuCores}")
        print(f"Memory Size: {esxi_host.hardware.memorySize / 1024 / 1024} MB")

        # Get performance metrics for the ESXi host
        print("\nPerformance Metrics:")
        get_host_performance_metrics(esxi_host)

    # Get Cluster information
    cluster = get_cluster_info(service_instance, cluster_name)
    if cluster:
        print(f"\nCluster Information:")
        print(f"Name: {cluster.name}")

    # Disconnect from vCenter
    connect.Disconnect(service_instance)
