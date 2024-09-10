#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)  # Output: (89, 100)

print(add_tuple(tuple_a, (1,)))  # Output: (2, 89)
print(add_tuple(tuple_a, ()))    # Output: (1, 89)
