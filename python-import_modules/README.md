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

hidden_4.pyc

