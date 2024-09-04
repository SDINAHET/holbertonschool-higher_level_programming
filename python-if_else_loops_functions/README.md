readme of project3
#!/usr/bin/python3 et rendre executable chmod a+x *

0-positive_or_negative.py
1-laste_digit.py

Explanation:
import random: Imports the random module, which is used to generate a random integer.
number = random.randint(-10000, 10000): Assigns a random integer between -10,000 and 10,000 to the variable number.
last_digit = abs(number) % 10 if number >= 0 else -(abs(number) % 10):
If number is non-negative, the last digit is calculated as number % 10.
If number is negative, the last digit is calculated as -(abs(number) % 10).
print(f"Last digit of {number} is {last_digit} and is ", end=""): Prints the initial part of the required message without a newline, so that the next print statement can complete the sentence.
if-elif-else structure:
if last_digit > 5:: If the last digit is greater than 5, prints "greater than 5".
elif last_digit == 0:: If the last digit is 0, prints "0".
else:: If the last digit is less than 6 and not 0, prints "less than 6 and not 0".

output:
Last digit of 4205 is 5 and is less than 6 and not 0
Last digit of -626 is -6 and is less than 6 and not 0
Last digit of 1144 is 4 and is less than 6 and not 0
Last digit of -9200 is 0 and is 0
Last digit of 5247 is 7 and is greater than 5

2-print_alphabet.py

Explanation:
for letter in range(97, 123):
The range(97, 123) generates numbers from 97 to 122, which correspond to the ASCII values of lowercase 'a' to 'z'.
print("{}".format(chr(letter)), end="")
chr(letter) converts the ASCII value (e.g., 97) to its corresponding character ('a').
print("{}".format(...), end="") is used to print each character without a newline at the end. This is essential because we need to print all the letters on the same line.

output:
abcdefghijklmnopqrstuvwxyz
 sans espace:  print("{}".format(chr(letter)), end="")
Certainly! The line print("{}".format(chr(letter)), end="") is used to print characters without adding a newline after each one. Let’s break down each part of this line to understand it better:

Components:
chr(letter)

Function: chr() is a built-in Python function that takes an integer (representing an ASCII value) and returns the corresponding character.
Example: chr(97) returns 'a' because 97 is the ASCII value for the lowercase letter 'a'.
"{}".format(chr(letter))

"{}": This is a placeholder within a string. It tells Python where to insert the value you want to format into the string.
.format(): This method is used to substitute the {} placeholder in the string with the value provided.
chr(letter): This value is inserted into the {} placeholder in the string.
Example: If letter is 97, then chr(97) is 'a', so "{}".format(chr(letter)) will produce the string 'a'.
print("{}".format(chr(letter)), end="")

print(): This function outputs the string to the console.
"{}".format(chr(letter)): The print function will output the character corresponding to chr(letter), formatted into the string.
end="": The end parameter of the print() function specifies what to print at the end of the output. By default, print() adds a newline (\n) after each call. Setting end="" overrides this behavior, so no newline is added, and the next print call will print directly after the previous one.

avec un espace: format(chr(letter))
#!/usr/bin/python3
for letter in range(97, 123):
    print(chr(letter))


1ere version:
#!/usr/bin/python3
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")

2ème version:
#!/usr/bin/python3

print(''.join(chr(i) for i in range(97, 123)))

3-print_alphabt.py

output:
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z

4-print_hexa.py


5-print_comb2.py


6-print_comb3.py


7-islower.py


8-uppercase.py


9-print_last_digit.py


10-add.py


11-pow.py


12-fizzbuzz.py
