# pin_tries.py
# Allow at most 3 tries to enter the correct PIN using a while loop.

MAX_TRIES = 3
CORRECT_PIN = "2580"

tries = 0
granted = False

while tries < MAX_TRIES:
    pin = input("PIN: ")
    tries += 1
    if pin == CORRECT_PIN:
        granted = True
        break
    else:
        print(f"Wrong PIN. Tries left: {MAX_TRIES - tries}")

if granted:
    print("Access granted.")
else:
    print("Card blocked.")