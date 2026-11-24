# fix_the_parser.py
LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
    # semantic: slice [0:4] stops at index 3 (4 chars); use [0:5] for 5 characters
    return line[0:5]


def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
    # semantic: str.lower() returns a new string rather than mutating in place
    user = user.lower()
    return user


def is_failed(line):
    """Return True if the line reports a failed login."""
    # semantic: log status is uppercase "FAILED", so case-sensitive check was False
    return "FAILED" in line


def hide_first(user):
    """Return user with its first letter replaced by *."""
    # runtime: strings are immutable and do not support item assignment (TypeError)
    return "*" + user[1:]


print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
# runtime: str objects have no .len() method; use the built-in len() function
print(f"Length: {len(LINE)}")
