# fix_the_record.py
# Prints network device info with fixed bugs

# Syntax error: missing equals sign
device_name = "edge-router"

# Syntax error: var name can't start with a number
second_ip = "192.0.2.1"

# Syntax error: class is a reserved python keyword
device_class = "router"

# Runtime error: int() cant parse string words like "twenty-two"
port = int("22")

print("Device:", device_name)
print("Backup IP:", second_ip)
print("Type:", device_class)
print("Port:", port)