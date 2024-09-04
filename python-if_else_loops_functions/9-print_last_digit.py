#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit using modulus and abs to handle negative numbers
    print("{}".format(last_digit), end="")
    return last_digit
