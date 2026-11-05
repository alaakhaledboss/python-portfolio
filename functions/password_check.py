def long_enough(password, minimum=8):
    """Return True if password length is at least minimum."""
    return len(password) >= minimum


def differs_from_username(password, username):
    """Return True if password and username are not equal."""
    return password != username


def password_ok(password, username):
    """Return True if password passes both length and dissimilarity checks."""
    return long_enough(password) and differs_from_username(password, username)


user_input = input("Username: ")
pass_input = input("Password: ")

if password_ok(pass_input, user_input):
    print("Password accepted.")
else:
    print("Password rejected.")