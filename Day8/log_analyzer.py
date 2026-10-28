error_count = 0
warning_count = 0

with open("Day8/server.log", "r") as file:
    for line in file:
        normal_txt = line.strip()
        lower_case = normal_txt.lower()

        if lower_case.startswith("error:"):
            error_count += 1
        elif lower_case.startswith("warning:"):
            warning_count += 1

print(f"Total errors: {error_count}")
print(f"Total warnings: {warning_count}")

with open("Day8/log_report.txt", "w") as file:
    file.write("Server Log Analysis Report\n")
    file.write(f"Total errors: {error_count}\n")
    file.write(f"Total warnings: {warning_count}\n")