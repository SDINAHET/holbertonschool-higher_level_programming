#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
# Inside result: 6.0
# 12 / 2 = 6.0

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
# Inside result: None
# 12 / 0 = None
