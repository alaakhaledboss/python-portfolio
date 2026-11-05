# fix_the_functions.py

# Fix 1 (runtime bug): Moved function definition above execution.
def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


print_header()


def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes
        # Fix 2 (semantic bug): Placed return inside the if-block.
        return total
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


# Fix 3 (runtime bug): Corrected parameter name from 'user' to 'username'.
print(login_line(username="sara", failed=4))
# Fix 4 (semantic bug): Added print statement to output the second call.
print(login_line("omar", 1))