# threat_level.py
# Categorizes a security score into a specific threat level.

score = int(input("Enter alert severity score (0-100): "))

if score >= 90:
    print("Threat Level: Critical - Immediate containment required.")
elif score >= 70:
    print("Threat Level: High - Investigation recommended.")
elif score >= 40:
    print("Threat Level: Medium - Monitor endpoint activity.")
else:
    print("Threat Level: Low - Normal baseline activity.")