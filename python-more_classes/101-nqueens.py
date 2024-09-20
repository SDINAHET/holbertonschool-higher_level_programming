#!/usr/bin/python3
"""
Module 101-nqueens
===================
This module solves the N queens problem using a backtracking algorithm.
The N queens problem is the challenge of placing N non-attacking queens
on an N×N chessboard. This means no two queens can share the same row, column,
or diagonal.

The solution is printed as a list of lists, where each inner list contains
the row and column positions of a queen on the board.
"""


def print_solution(solution):
    """
    Prints the board configuration for a solution.

    Args:
        solution (list): A list of lists, where each inner list represents
        the position of a queen as [row, column].

    Example:
        [[0, 1], [1, 3], [2, 0], [3, 2]] represents queens placed at:
        - Row 0, Column 1
        - Row 1, Column 3
        - Row 2, Column 0
        - Row 3, Column 2
    """
    print(solution)


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at the given board position (row, col)
    A position is safe if no queens are attacking each other. This means there
    should be no other queens in the same column, or on the same diagonal.

    Args:
        board (list): A list where the index represents the row and the value
                      represents the column of a queen.
        row (int): The current row index where we are trying to place a queen.
        col (int): The column index where we are trying to place a queen.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for i in range(row):
        # Check if another queen is in the same column or diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Recursively solves the N queens problem by placing queens one row at a time
    The function uses backtracking to explore possible queen placements,
    ensuring that no two queens can attack each other. Once all queens are
    placed, the solution is printed.

    Args:
        board (list): A list of length `n` where the value at each index
        represents the column position of the queen in that row.
        row (int): The current row index where we are trying to place a queen.
        n (int): The size of the board (also the number of queens to place).

    Returns:
        None: The function prints each solution as it finds one.
    """
    if row == n:
        # All queens are placed, print the solution
        solution = [[i, board[i]] for i in range(n)]
        print_solution(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            # Place the queen at (row, col)
            board[row] = col
            # Recursively place queens in the next row
            solve_nqueens(board, row + 1, n)


def main():
    """
    Main function to handle input and initiate solving the N queens problem.

    This function prompts the user to input the size of the chessboard (N).
    It validates the input to ensure N is an integer and at least 4.
    Then, it initializes an empty board and calls the recursive solver function

    Input:
        The function prompts the user for the value of N via `input()`.

    Returns:
        None: The function will either solve the N queens problem or print an
              error message if the input is invalid.
    """
    n_str = input("Enter the value of N: ")

    try:
        n = int(n_str)
    except ValueError:
        print("N must be a number")
        return

    if n < 4:
        print("N must be at least 4")
        return

    # Initialize the board with -1, indicating no queens are placed yet
    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()
