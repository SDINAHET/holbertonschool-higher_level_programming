#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name itself

    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
