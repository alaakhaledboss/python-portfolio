# Name: Ala'a Khaled
# Date: October 2, 2026
# Description: Quick breakdown of how print() handles separators and line ends under the hood.
# Source: https://docs.python.org/3/library/functions.html#print

# Research:
# 1. By default, print() inserts a single space (' ') between values (handled by the 'sep' parameter).
# 2. At the end of the line, it appends a newline character ('\n') by default (handled by 'end').

# 3. The 'sep' parameter can be used to change the separator between values.
# 4. The 'end' parameter can be used to change the character appended at the end of the line.

# Quick example passing 3 values:
print("System", "Status", "Secure")