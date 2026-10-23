server_name = "web-server-01"
cpu_usage = 65.5
memory_usage = 72
total_disk_gb = 100
used_disk_gb = 65
free_disk_gb = total_disk_gb - used_disk_gb

print("========== SERVER REPORT ==========")
print(f"Server Name: {server_name}")
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"Total Disk: {total_disk_gb} GB")
print(f"Used Disk: {used_disk_gb} GB")
print(f"Free Disk: {free_disk_gb} GB")
print("===================================")