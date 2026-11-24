# log_analyzer.py
ALERT_LIMIT = 3
LOG = """09:01 OK user=sara ip=192.0.2.5
09:02 FAILED user=admin ip=192.0.2.7
09:02 FAILED user=admin ip=192.0.2.7
09:03 FAILED user=root ip=192.0.2.7
09:04 OK user=omar ip=198.51.100.4
09:06 FAILED user=Sara ip=203.0.113.9
09:07 FAILED user=test ip=192.0.2.7
09:09 OK user=admin ip=192.0.2.5
09:12 FAILED user=guest ip=203.0.113.9
09:15 OK user=lina ip=198.51.100.8"""


def get_field(line, name):
    """Return the value after name= up to the next space or end of line, or ""."""
    prefix = name + "="
    start = line.find(prefix)
    if start == -1:
        return ""
    start += len(prefix)
    end = line.find(" ", start)
    if end == -1:
        return line[start:]
    return line[start:end]


def get_status(line):
    """Return the second word of the line (e.g., OK or FAILED)."""
    words = line.split()
    if len(words) < 2:
        return ""
    return words[1]


def count_status(status):
    """Return how many lines in LOG have the given status."""
    count = 0
    for line in LOG.splitlines():
        if get_status(line) == status:
            count += 1
    return count


def show_summary():
    """Print total lines, failed count, and OK count."""
    lines = LOG.splitlines()
    print(f"Lines: {len(lines)}")
    print(f"Failed: {count_status('FAILED')}")
    print(f"OK: {count_status('OK')}")


def search(keyword):
    """Print matching lines with 1-based line numbers (case-insensitive) and match count."""
    key_lower = keyword.lower()
    matches = 0
    line_num = 0
    for line in LOG.splitlines():
        line_num += 1
        if key_lower in line.lower():
            print(f"{line_num}: {line}")
            matches += 1
    print(f"Matches: {matches}")


def ip_report(ip):
    """Print failed login times and users for ip, total count, and alert if >= ALERT_LIMIT."""
    failed_count = 0
    for line in LOG.splitlines():
        if get_status(line) == "FAILED" and get_field(line, "ip") == ip:
            words = line.split()
            time_str = words[0] if words else ""
            user = get_field(line, "user")
            print(f"{time_str} {user}")
            failed_count += 1
    print(f"Failed logins from {ip}: {failed_count}")
    if failed_count >= ALERT_LIMIT:
        print("ALERT: possible password guessing.")


def mask(word):
    """Return first and last characters with * between them, or * for length <= 2."""
    if len(word) <= 2:
        return "*"
    return word[0] + ("*" * (len(word) - 2)) + word[-1]


def show_masked():
    """Print the whole LOG with every user= value masked using replace."""
    for line in LOG.splitlines():
        user = get_field(line, "user")
        if user != "":
            masked_line = line.replace(f"user={user}", f"user={mask(user)}")
        else:
            masked_line = line
        print(masked_line)


def show_menu():
    """Print the analyzer title and menu options."""
    print("AUTH LOG ANALYZER")
    print("1. Summary")
    print("2. Search")
    print("3. IP report")
    print("4. Masked log")
    print("q. Quit")


def main():
    """Run the interactive log analyzer menu loop."""
    show_menu()
    while True:
        choice = input("Choice: ").strip().lower()
        if choice == "1":
            show_summary()
        elif choice == "2":
            keyword = input("Keyword: ")
            search(keyword)
        elif choice == "3":
            ip = input("IP: ").strip()
            ip_report(ip)
        elif choice == "4":
            show_masked()
        elif choice == "q":
            print("Bye.")
            break
        else:
            print("Unknown choice.")


if __name__ == "__main__":
    main()
