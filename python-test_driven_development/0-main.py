#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))       # Output: 3
print(add_integer(100, -2))    # Output: 98
print(add_integer(2))           # Output: 100
print(add_integer(100.3, -2))   # Output: 98
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)                   # Output: b must be an integer
try:
    print(add_integer(None))
except Exception as e:
    print(e)                   # Output: a must be an integer
