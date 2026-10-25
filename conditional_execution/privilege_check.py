# privilege_check.py
# Uses if-elif-else branches to determine system access levels.

role = input("Enter user role (admin/analyst/viewer): ")

if role == "admin":
    print("Full root access granted.")
elif role == "analyst":
    print("Read and write access granted.")
elif role == "viewer":
    print("Read-only access granted.")
else:
    print("Access denied. Unknown role.")