# port_facts.py
# Calculates port and IPv4 address capacities using exponentiation.
# References: RFC 9293 (TCP), RFC 791 (Internet Protocol)

PORT_BITS = 16
IP_BITS = 32

possible_ports = 2 ** PORT_BITS
highest_port = (2 ** PORT_BITS) - 1
ipv4_addresses = 2 ** IP_BITS

print(f"Possible ports: {possible_ports}")
print(f"Highest port number: {highest_port}")
print(f"Possible IPv4 addresses: {ipv4_addresses}")