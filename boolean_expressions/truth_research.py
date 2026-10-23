# truth_research.py
# Research on truth values in Python.
# Documentation Reference: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# bool("") prints False because empty strings are considered falsy.
print(bool(""))

# bool("0") prints True because any non-empty string is truthy, regardless of contents.
print(bool("0"))

# bool(0) prints False because numeric zero is considered falsy.
print(bool(0))

# bool(0.0) prints False because float zero is considered falsy.
print(bool(0.0))

# bool("False") prints True because "False" is a non-empty string.
print(bool("False"))