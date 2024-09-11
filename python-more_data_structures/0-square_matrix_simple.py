#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Return a new matrix with the square of each element
    return [[element ** 2 for element in row] for row in matrix]
