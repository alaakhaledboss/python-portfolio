# fix_the_session.py
# This program reports a user's session time with bugs fixed.

username = input("Username: ")

# Runtime error: input() returns a str, must be converted to int before math
total_seconds = int(input("Session length in seconds: "))

# Semantic error: use floor division // instead of float division / for whole minutes
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
# Semantic error: added 'f' prefix so the f-string evaluates the variable
print(f"User: {username}")
# Runtime error: cannot concatenate str and int directly, converted minutes/seconds via f-string instead
print(f"Session: {minutes} min {seconds} s")
print("=" * 30)