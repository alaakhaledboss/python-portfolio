# ip_check.py
def is_valid_part(part):
    """Return True if part has only digits and its numeric value is <= 255."""
    if not part.isdecimal():
        return False
    return int(part) <= 255


def ip_problem(address):
    """Return the first problem found in address, or "" if valid."""
    if address.count(".") != 3:
        return "it needs exactly 3 dots."
    parts = address.split(".")
    for part in parts:
        if part == "":
            return "a part is empty."
        if not is_valid_part(part):
            return f"{part} is not a number from 0 to 255."
    return ""


def main():
    """Prompt for an IPv4 address, validate it, and print the result."""
    address = input("IPv4 address: ").strip()
    problem = ip_problem(address)
    if problem == "":
        print(f"{address} is valid.")
    else:
        print(f"Invalid: {problem}")


if __name__ == "__main__":
    main()
