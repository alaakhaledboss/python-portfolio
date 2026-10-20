# int_research.py
# Name: Ala'a Khaled
# Date: October 9, 2026
# Description: Testing int() string conversion limits
# Source: https://docs.python.org/3/library/functions.html#int

# Predictions:
# - int(" 22 "): Works, strips spaces automatically
# - int("+22"): Works, ignores the plus sign
# - int("0022"): Works, ignores leading zeros
# - int("2_2"): Works, underscores allowed as digit separators

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))