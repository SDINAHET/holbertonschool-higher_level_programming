#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)  # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
print(matrix)      # Original matrix remains unchanged
