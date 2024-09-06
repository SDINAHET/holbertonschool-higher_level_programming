readme of project4
#!/usr/bin/python3 et rendre executable chmod a+x *

0-add.py

Explanation:
if __name__ == "__main__":: This ensures that the code only runs when the script is executed directly, and not when it is imported.
from add_0 import add: This imports the add function from the add_0.py file.
a = 1 and b = 2: These lines assign the values 1 and 2 to variables a and b, respectively.
print("{} + {} = {}".format(a, b, add(a, b))): This prints the result in the format 1 + 2 = 3 using Python's string formatting with format().

guillaume@ubuntu:~/$ ./0-add.py
1 + 2 = 3

Important Points:
You can only use the word add_0 once in the code—which happens in the import statement.
The program should not run on import, which is controlled by the if __name__ == "__main__": guard.
You use string formatting to display the output.

1-calculation.py


2-args.py


3-infinite_add.py


5-variable_load.py

Explanation:
a = 98: This assigns the value 98 to the variable a.
print(a): This properly prints the value of a. In Python 3, the print function requires parentheses.

output:
98

Notes:
In Python 3, the print function requires parentheses, unlike Python 2 where print a was valid.
The triple quotes """Simple variable""" are a docstring or comment, which is ignored by the interpreter.

Explanation:
if __name__ == "__main__":: This block ensures that the code inside it runs only if the script is executed directly, and not if it is imported as a module.
from variable_load_5 import a: This imports the variable a from variable_load_5.py.
print(a): This prints the value of a.
How It Works:
When you run 5-variable_load.py directly (e.g., ./5-variable_load.py), it will print 98 as defined in variable_load_5.py.
If 5-variable_load.py is imported as a module in another script, the code inside the if __name__ == "__main__": block will not execute.

Run
./5-variable_load.py

output:
98

hidden_4.pyc

100-my_calculator.py

Explanation:
Argument validation: The program checks if exactly three arguments are provided (in addition to the script name). If not, it prints the usage message and exits with a status code of 1.
Operator validation: It ensures the operator is one of the valid ones (+, -, *, /). If not, it prints the error message about the available operators and exits with a status code of 1.
Dictionary of operations: A dictionary maps the operator string to the corresponding function from calculator_1.py.
Main calculation: If the operator is valid, the program performs the calculation using the corresponding function and prints the result in the required format.
Exit status: The program exits with a status code of 0 on success.

$ ./100-my_calculator.py 3 + 5
3 + 5 = 8

$ ./100-my_calculator.py 3 H 5
Unknown operator. Available operators: +, -, * and /

$ ./100-my_calculator.py
Usage: ./100-my_calculator.py <a> <operator> <b>

root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/h
olbertonschool-higher_level_programming/python-import_modules# ./100-my_calculator.py 3 + 5
3 + 5 = 8
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/h
olbertonschool-higher_level_programming/python-import_modules# ./100-my_calculator.py 3 H 5
Unknown operator. Available operators: +, -, * and /
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/h
olbertonschool-higher_level_programming/python-import_modules# Here is the Python program that meets your requirements:

```python
#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check if the number of arguments is exactly 3
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Parse arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Dictionary mapping operators to functions
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    # Check if the operator is valid
```ge: ./100-my_calculator.py <a> <operator> <b>nd /code of `0` on success
Here: command not found
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
Command 'import' not found, but can be installed with:
apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.38-1ubuntu0.1, or
apt install imagemagick-6.q16                  # version 8:6.9.11.60+dfsg-1.3ubuntu0.22.04.5
apt install imagemagick-6.q16hdri              # version 8:6.9.11.60+dfsg-1.3ubuntu0.22.04.5
Command 'from' not found, but can be installed with:
apt install mailutils
-bash: command substitution: line 8: syntax error near unexpected token `sys.argv'
-bash: command substitution: line 8: `    if len(sys.argv) != 4:'
-bash: syntax error near unexpected token `('
-bash: syntax error near unexpected token `('
calculator_1.py: command not found
3.: command not found
4.: command not found
0: command not found
5.: command not found
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/h
olbertonschool-higher_level_programming/python-import_modules#

oot@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/h
olbertonschool-higher_level_programming/python-import_modules# ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/h
olbertonschool-higher_level_programming/python-import_modules# ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/h
olbertonschool-higher_level_programming/python-import_modules# ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/projet2/h
olbertonschool-higher_level_programming/python-import_modules#

101-easy_print.py

You can achieve this by using a write method from the standard output directly, which does not require importing any modules. Here’s how you can do it in exactly two lines:
Explanation:
The sys.stdout.write method writes directly to the standard output.
\n ensures that a new line is added after #pythoniscool.
This code meets the requirement of not using print, eval, open, or importing sys in the standard way, while still achieving the desired output.

Explanation:
import __import__: Imports the __import__ function which is a built-in function in Python used to import modules.
__import__('sys'): Dynamically imports the sys module.
.stdout.write("#pythoniscool\n"): Calls write() method of sys.stdout to print the string #pythoniscool followed by a newline.
This approach adheres to the constraints and correctly prints the required output.

102-magic_calculator.py

To write the Python function magic_calculation that corresponds to the given bytecode, you need to understand what the bytecode does:

Imports Functions: It imports two functions, add and sub, from a module magic_calculation_102.
Comparison: It compares two values a and b.
Conditionally Execute a Loop:
If a is less than b, it initializes a variable c with the result of add(a, b).
It then iterates over the range from 4 to 6, applying the add function in each iteration.
It returns the final value of c.
Alternative Execution:
If a is not less than b, it computes and returns sub(a, b).

Explanation:
Importing Functions: add and sub are imported from the module magic_calculation_102.
Comparison: If a < b, it performs the calculation as described.
Loop and Calculation: In the loop, it adds i to c for i in the range 4 to 6.
Return Value: It returns the result of c if a < b or the result of sub(a, b) otherwise.

103-fast_alphabet.py

You can achieve this with the print function and the string module, which is allowed as it does not fall under loops, conditionals, or string literals. Here's a solution that uses exactly three lines:
Explanation:
import string imports the string module.
string.ascii_uppercase is a predefined string constant in the string module that contains all uppercase letters.
print(string.ascii_uppercase) prints this string followed by a newline.
This solution is concise and adheres to the constraints.
