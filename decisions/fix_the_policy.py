# fix_the_policy.py
# Check a new password against an example policy and classify its length.

MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Syntax error: missing colon ':' at the end of the if statement
if len(password) < MIN_LENGTH:
    print("- Too short.")
elif password == username:
    print("- Same as the username.")

# Semantic error: order of conditions was wrong (>= 16 must come before >= MIN_LENGTH)
# Semantic error: print statement was incorrectly indented inside the else block instead of running for all lengths
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

print(f"Length: {len(password)} ({strength})")