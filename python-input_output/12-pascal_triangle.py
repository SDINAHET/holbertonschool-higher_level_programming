#!/usr/bin/python3
"""
This module defines the function `pascal_triangle(n)` which generates
the Pascal's triangle up to the nth row.

Pascal's triangle is a triangular array where each number is the sum of
the two directly above it, starting with 1 at the top.

Example:
    To generate the first 5 rows of Pascal's triangle:
    triangle = pascal_triangle(5)
    Output:
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists of integers representing the Pascal's triangle
        of n.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
