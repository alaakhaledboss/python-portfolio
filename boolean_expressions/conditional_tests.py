# conditional_tests.py
# Ten conditional tests predicting True or False values.

user = "analyst"
role = "viewer"
failed = 3
port = 22

print("Is user == 'analyst'? I predict True.")
print(user == "analyst")

print("\nIs role == 'admin'? I predict False.")
print(role == "admin")

print("\nIs failed >= 3? I predict True.")
print(failed >= 3)

print("\nIs failed < 3? I predict False.")
print(failed < 3)

print("\nIs port != 80? I predict True.")
print(port != 80)

print("\nIs port <= 21? I predict False.")
print(port <= 21)

print("\nIs user == 'analyst' and failed == 3? I predict True.")
print(user == "analyst" and failed == 3)

print("\nIs role == 'viewer' and failed > 5? I predict False.")
print(role == "viewer" and failed > 5)

print("\nIs role == 'admin' or failed == 3? I predict True.")
print(role == "admin" or failed == 3)

print("\nIs not failed == 3? I predict False.")
print(not failed == 3)