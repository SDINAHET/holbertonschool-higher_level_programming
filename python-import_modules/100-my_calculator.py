#!/usr/bin/python3

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return a - b


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return a * b


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)


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
        an error message to the standard output and exits with a status code.
    """

    import sys

    # List of valid operators
    valid_operators = ['+', '-', '*', '/']
    args = sys.argv[1:]

    # Check if the number of arguments is exactly 3
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    try:
        a = int(args[0])
        operator = args[1]
        b = int(args[2])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Check if the operator is valid
    if operator not in valid_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the calculation and handle division by zero
    try:
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            if b == 0:
                print("Error: Division by zero")
                sys.exit(1)
            result = div(a, b)
        print(f"{a} {operator} {b} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero")
        sys.exit(1)

    # Exit successfully
    sys.exit(0)


if __name__ == "__main__":
    main()
