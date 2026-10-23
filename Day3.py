servers = ["web-01", "web-02", "db-01", "cache-01"]
cpu_usages = [35, 78, 94, 65]

for i in range(len(servers)):
    server = servers[i]
    cpu = cpu_usages[i]

    if cpu >= 90:
        status = "CRITICAL"
    elif cpu >= 75:
        status = "WARNING"
    else:
        status = "OK"

    print(f"{server}: CPU {cpu}% - {status}")