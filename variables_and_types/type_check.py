# this code is for datatype checking in python
# 8080 is an integer
# "8080" is a string
# 99.5 is a float
# "198.51.100.7" is a string
# 1_000 is an integer (underscores are allowed in numeric literals for readability)

print("Type of 8080:", type(8080))
print("Type of \"8080\":", type("8080"))
print("Type of 99.5:", type(99.5))
print("Type of \"198.51.100.7\":", type("198.51.100.7"))
print("Type of 1_000:", type(1_000))

print("Type of int(\"443\") is :", type(int("443")))
print("Type of str(8080) is :", type(str(8080)))
print("Type of float(\"2.5\") is :", type(float("2.5")))