# pin_space_table.py
# Calculate time required to guess every PIN length from 4 to 8 digits.

GUESSES_PER_SECOND = 10

for digits in range(4, 9):
    combinations = 10 ** digits
    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = minutes // 1440  # 1440 minutes in a full day (24 * 60)
    print(f"{digits} digits: {combinations} PINs, {minutes} minutes, {days} days")