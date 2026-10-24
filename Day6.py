logs = [
    "  INFO: Server started  ",
    "ERROR: Disk space critical",
    "  warning: High memory usage",
    "INFO: Backup completed",
    "error: Database connection failed",
    "WARNING: CPU usage high"
]

error_count = 0

for log in logs:
    message = log.strip()
    lower_txt = message.lower()
    
    if lower_txt.startswith("error:"):
        print(f"ERROR: {message}")
        error_count += 1
    elif lower_txt.startswith("warning:"):
        print(f"WARNING: {message}")

print(f"Total errors: {error_count}")