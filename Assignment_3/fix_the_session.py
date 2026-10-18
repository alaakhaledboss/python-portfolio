# fix_the_session.py
# This program reports a user's session time.
  
username = input("Username: ")
total_seconds = input("Session length in seconds: ")
   
minutes = int(int(total_seconds) / 60)
seconds = int(total_seconds) % 60
   
print("=" * 30)
print(f"User: {username}")
print(f"Session: {minutes} min {seconds} s")
print("=" * 30)
