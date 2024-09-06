#!/usr/bin/python3
import sys

# Importing all functions from calculator_1.py
from calculator_1 import add, sub, mul, div


def main():
    """Main function to handle the calculator operations"""

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
