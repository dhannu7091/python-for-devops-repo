server_name = "web-server-01"
cpu_usage = 86
memory_usage = 78
disk_usage = 91
is_running = False

print(f"Server Name: {server_name}")

if is_running:
    print("Server Status: RUNNING")

    if cpu_usage >= 90:
        print("CPU: CRITICAL")
    elif cpu_usage >= 75:
        print("CPU: WARNING")
    else:
        print("CPU: OK")
    
    if memory_usage >= 90:
        print("Memory: CRITICAL")
    elif memory_usage >= 75:
        print("Memory: WARNING")
    else:
        print("Memory: OK")
    
    if disk_usage >= 90:
        print("Disk: CRITICAL")
    elif disk_usage >= 80:
        print("Disk: WARNING")
    else:
        print("Disk: OK")

else:
    print("CRITICAL: Server is down")
    