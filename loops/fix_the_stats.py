# fix_the_stats.py
# Count failed logins and the average session length with all bugs fixed.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1 fix (Semantic): failed counter was initialized inside the loop and reset to 0 every iteration.
# It must be initialized outside/before the loop.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2 fix (Semantic): print was inside the loop causing it to repeat prematurely.
# Bug 3 fix (Semantic): used floor division // instead of true division / to achieve the float result (30.0).
print(f"Average session: {total / count} minutes")

# Bug 4 fix (Semantic): range(1, 4) stopped at 3, missing Level 4. Changed to range(1, 5).
for level in range(1, 5):
    print(f"Level {level}")