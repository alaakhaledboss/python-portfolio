# type_check.py
# Checking datatypes and type conversion in python

# Predictions:
# 8080 -> int
# "8080" -> str
# 99.5 -> float
# "198.51.100.7" -> str
# 1_000 -> int

print("Type of 8080:", type(8080))
print("Type of \"8080\":", type("8080"))
print("Type of 99.5:", type(99.5))
print("Type of \"198.51.100.7\":", type("198.51.100.7"))
print("Type of 1_000:", type(1_000))

# Conversions with types
print("Converted 443:", int("443"), type(int("443")))
print("Converted 8080:", str(8080), type(str(8080)))
print("Converted 2.5:", float("2.5"), type(float("2.5")))