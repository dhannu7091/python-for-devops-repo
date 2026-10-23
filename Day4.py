servers = ["web-01", "web-02", "db-01", "cache-01"]
cpu_usages = [35, 78, 94, 65]
maintenance = [False, True, False, False]

for server, cpu, maintenance_mode in zip(servers, cpu_usages, maintenance):
    if maintenance_mode:
        continue
    
    if cpu >= 90:
        status = "CRITICAL"
    elif cpu >= 75:
        status = "WARNING"
    else:
        status = "OK"
        
    print(f"{server}: CPU {cpu}% - {status}")
