#!/usr/bin/python3
import sys

# Importing all functions from calculator_1.py
from calculator_1 import add, sub, mul, div


def main():
    """Main function to handle the calculator operations.

    This function processes command-line arguments to perform
    basic arithmetic operations. It checks the number of arguments,
    validates them, and performs the appropriate operation based on
    the provided operator. It handles invalid arguments, unknown
    operators, and division by zero errors.
    Function Description:
        - Checks if the number of command-line arguments is correct.
        - Parses the command-line arguments to integers and operator.
        - Validates the operator and performs the requested arithmetic
        operation.
        - Handles exceptions and errors such as invalid arguments or division
        by zero.

    Parameters:
        None. The function uses command-line arguments passed to the script.

    Returns:
        None. The function prints the result of the arithmetic operation or
        an error message
        to the standard output and exits with a status code.
    """

    # Check if the number of arguments is exactly 3
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end='\n')
        exit(1)

    # Parse arguments
    try:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end='\n')
        exit(1)

    # Dictionary mapping operators to functions
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    # Check if the operator is valid
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /", end='\n')
        exit(1)

    # Perform the calculation and print the result
    if operator == '/' and b == 0:
        print("Error: Division by zero", end='\n')
        exit(1)

    result = operations[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result), end='\n')
    exit(0)


if __name__ == "__main__":
    main()
