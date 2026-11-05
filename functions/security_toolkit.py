# security_toolkit.py

MIN_LENGTH = 8


def border(width):
    """Print top or bottom border frame line."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Display text inside a formatted text box."""
    width = len(text)
    border(width)
    print(f"| {text} |")
    border(width)


def show_menu():
    """Display the interactive menu options."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):
    """Return the IANA classification string of a port number."""
    if port < 0 or port > 65535:
        return "invalid"
    elif port <= 1023:
        return "system"
    elif port <= 49151:
        return "user"
    else:
        return "dynamic"


def check_port():
    """Prompt for port number and print its category inside a box."""
    val = int(input("Port: "))
    r = port_range(val)
    show_box(f"Port {val}: {r}")


def password_problem(password, username):
    """Return description of the first failed password rule, or empty string."""
    if len(password) < MIN_LENGTH:
        return f"too short (at least {MIN_LENGTH})"
    if password == username:
        return "same as the username"
    return ""


def check_password():
    """Prompt for credentials and display validation result inside a box."""
    u = input("Username: ")
    p = input("Password: ")
    prob = password_problem(p, u)
    if prob:
        show_box(f"Rejected: {prob}")
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Return whole days required to brute-force a PIN of given digit count."""
    total_combinations = 10 ** digits
    total_seconds = total_combinations // per_second
    return total_seconds // 86400


def check_pin():
    """Prompt for PIN details and display estimated crack time inside a box."""
    d = int(input("PIN digits: "))
    g = int(input("Guesses per second: "))
    days = days_to_guess(d, g)
    show_box(f"{d} digits: {days} days")


def main():
    """Execute the main event loop for the Security Toolkit."""
    show_menu()
    checks_count = 0

    while True:
        choice = input("Choice (1, 2, 3, or q): ")
        if choice == "1":
            check_port()
            checks_count += 1
        elif choice == "2":
            check_password()
            checks_count += 1
        elif choice == "3":
            check_pin()
            checks_count += 1
        elif choice == "q":
            show_box(f"Checks done: {checks_count}")
            break
        else:
            print("Unknown choice.")


if __name__ == "__main__":
    main()