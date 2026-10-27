servers = [
    {"name": "app-01", "cpu": 55, "memory": 62},
    {"name": "app-02", "cpu": 81, "memory": 74},
    {"name": "db-01", "cpu": 93, "memory": 88},
    {"name": "cache-01", "cpu": 40, "memory": 95}
]

def check_resources(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 75:
        return "WARNING"
    else:
        return "OK"

for server in servers:
    cpu_status = check_resources(server["cpu"])
    memory_status = check_resources(server["memory"])

    print(f"{server['name']}: CPU {server['cpu']}% - {cpu_status} | Memory {server['memory']}% - {memory_status}")