# session_timer.py
# Asks for session length in seconds and calculates minutes and seconds.

total_seconds = int(input("Session length in seconds: "))

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"Session length: {minutes} minutes and {seconds} seconds")

# Test outputs:
# 905 -> Session length: 15 minutes and 5 seconds
# 60  -> Session length: 1 minutes and 0 seconds
# 59  -> Session length: 0 minutes and 59 seconds