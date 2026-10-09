# fix_the_record.py
# This program prints a short record about a network device.

device_name = "edge-router" # the + mark was missing
second_ip = "192.0.2.1" # the variable name cannot start with a number
device_class = "router" # the variable name cannot be a reserved keyword
port = int("22") #the system cannot translate a string to an integer if the string is not a number

print("Device:", device_name)
print("Backup IP:", second_ip)
print("Type:", device_class)
print("Port:", port)