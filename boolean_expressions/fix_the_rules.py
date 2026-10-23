# fix_the_rules.py
# This program checks a connection against three rules with all bugs fixed.

role = input("Role: ")
# Runtime error: input() returns str, must convert to int before comparison operator <=
port = int(input("Port: "))

# Syntax error: used single '=' (assignment) instead of double '==' (comparison)
is_admin = role == "admin"

# Syntax error: invalid operator '=<' (must be '<=')
is_system_port = port <= 1023

# Semantic error: 'port == 80 or 443' evaluates 443 as truthy; both sides of 'or' need full comparisons
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")