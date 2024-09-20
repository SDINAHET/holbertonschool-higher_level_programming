#!/usr/bin/python3
"""
Module 101-nqueens
Solves the N queens problem using backtracking.
"""

def print_solution(solution):
    """Prints the board configuration for a solution."""
    print(solution)

def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at the board position (row, col).
    Queens must not be in the same row, column, or diagonal.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    """
    Recursively solves the N queens problem by placing queens one row at a time
    """
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        print_solution(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            # No need to undo assignment as we overwrite it on thenextiteration

def main():
    """Main function to handle input and initiate solving the N queens
    problem."""
    n_str = input("Enter the value of N: ")

    try:
        n = int(n_str)
    except ValueError:
        print("N must be a number")
        return

    if n < 4:
        print("N must be at least 4")
        return

    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()
