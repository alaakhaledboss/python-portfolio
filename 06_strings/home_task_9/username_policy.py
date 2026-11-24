# username_policy.py
MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    """Return username stripped of outer whitespace and converted to lowercase."""
    return username.strip().lower()


def bad_character(username):
    """Return the first character not allowed (letter, digit, or _), or ""."""
    for ch in username:
        if not (ch.isalnum() or ch == "_"):
            return ch
    return ""


def policy_problem(username):
    """Return the first policy problem for username, or "" if compliant."""
    if len(username) < MIN_LENGTH or len(username) > MAX_LENGTH:
        return f"length must be {MIN_LENGTH} to {MAX_LENGTH}."
    if not username[0].isalpha():
        return "it must start with a letter."
    bad = bad_character(username)
    if bad != "":
        return f"the character {bad} is not allowed."
    return ""


def main():
    """Prompt for a username, clean it, and report whether it is accepted."""
    raw = input("New username: ")
    cleaned = clean(raw)
    problem = policy_problem(cleaned)
    if problem == "":
        print(f"Accepted [{cleaned}].")
    else:
        print(f"Rejected [{cleaned}]: {problem}")


if __name__ == "__main__":
    main()
