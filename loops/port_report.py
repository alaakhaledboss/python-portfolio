# port_report.py
# Check a range of ports and report their IANA classification.

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

ports_checked = 0

for port in range(start_port, end_port + 1):
    if port <= 1023:
        range_type = "system"
    elif port <= 49151:
        range_type = "user"
    else:
        range_type = "dynamic"
    
    print(f"{port}: {range_type}")
    ports_checked += 1

print(f"Ports checked: {ports_checked}")