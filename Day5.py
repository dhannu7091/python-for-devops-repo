servers = ["web-01", "web-02", "db-01", "cache-01"]
cpu_usages = [35, 78, 94, 65]
memory_usages = [45, 82, 91, 60]

def check_resource(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 75:
        return "WARNING"
    else:
        return "OK"

def print_server_report(server, cpu, memory):
    cpu_status = check_resource(cpu)
    memory_status = check_resource(memory)
    print(f"{server}: CPU {cpu}% - {cpu_status} | Memory {memory}% - {memory_status}")

for server, cpu, memory in zip(servers, cpu_usages, memory_usages):
    print_server_report(server, cpu, memory)