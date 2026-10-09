# int_research.py
# Name: Ala'a Khaled Mohammad Al-Bustanji
# Date: October 9, 2026
# Description: Testing string parsing capabilities of int() based on Python documentation.
# Documentation Source: https://docs.python.org/3/library/functions.html#int

# Predictions & Explanation:
# - int(" 22 "): Works. Leading and trailing whitespace is automatically stripped.
# - int("+22"): Works. Explicit '+' sign prefix is allowed.
# - int("0022"): Works. Leading zeros are safely stripped for decimal values.
# - int("2_2"): Works. Underscores are valid digit separators in Python numeric strings , the same way in 1_000.

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))