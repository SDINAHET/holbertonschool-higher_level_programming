#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2) # output: 12
print("nb_print: {:d}".format(nb_print)) # output: nb_print: 2
nb_print = safe_print_list(my_list, len(my_list)) # output: 12345
print("nb_print: {:d}".format(nb_print)) # output:nb_print: 5
nb_print = safe_print_list(my_list, len(my_list) + 2) # output: 12345
print("nb_print: {:d}".format(nb_print)) # output:nb_print: 5
