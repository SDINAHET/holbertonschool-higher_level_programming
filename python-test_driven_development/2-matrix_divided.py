#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements
of a matrix by a given divisor, ensuring the matrix structure and handling
exceptions like division by zero.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats,
                   or if `div` is not a number, or if rows of `matrix`
                   are not of the same size.
        ZeroDivisionError: If `div` is zero.

    Returns:
        list of lists of float: The new matrix with divided values rounded
        to 2 decimal places.
    """
    # Check if matrix is a list of lists of int/float
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(elem, (int, float)) for row in matrix
               for elem in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows in the matrix are of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    return [[round(elem / div, 2) for elem in row] for row in matrix]
