error_count = 0
warning_count = 0

try:
    with open("Day8/server.log", "r") as file:
        for line in file:
            normal_txt = line.strip()
            plain_txt = normal_txt.lower()

            if plain_txt.startswith("error:"):
                error_count += 1
            elif plain_txt.startswith("warning:"):
                warning_count += 1

except FileNotFoundError:
    print("ERROR: server.log file not found")

else:
    with open("Day9/log_report.txt", "w") as file:
        file.write("Server Log Analysis Report\n")
        file.write(f"Total errors: {error_count}\n")
        file.write(f"Total warnings: {warning_count}\n")

    print(f"Total errors: {error_count}")
    print(f"Total warnings: {warning_count}")