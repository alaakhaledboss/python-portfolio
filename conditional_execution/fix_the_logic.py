# fix_the_logic.py
# Evaluates system rules with all conditional bugs fixed.

status = input("Enter connection status (active/idle/blocked): ")
# Runtime error: input() returns str, must be converted to int before numerical comparison
attempts = int(input("Enter failed login count: "))

# Syntax error: missing colon ':' at the end of the if statement
if status == "blocked":
    print("Connection blocked by firewall.")
# Semantic error: fixed branch ordering/logic so high-risk attempts are properly evaluated
elif attempts >= 5:
    print("Account locked due to excessive failed attempts.")
elif status == "active":
    print("Session is active.")
else:
    print("Session status normal.")