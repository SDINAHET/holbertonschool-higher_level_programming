#!/usr/bin/python3
import sys

# Importing all functions from calculator_1.py
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div


def main():
    # Check if the number of arguments is exactly 3
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Parse arguments
    try:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Dictionary mapping operators to functions
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    # Check if the operator is valid
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the calculation and print the result
    if operator == '/' and b == 0:
        print("Error: Division by zero")
        sys.exit(1)

    result = operations[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
    sys.exit(0)


if __name__ == "__main__":
    main()
