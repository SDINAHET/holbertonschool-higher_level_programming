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


1ere version: 7 check sur 7
#!/usr/bin/python3
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")

2ème version: 2 check sur 7
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

3-print_alphabt.py

Explanation:
Range: range(97, 123) iterates over ASCII values from 97 ('a') to 122 ('z').

Condition: if letter != 101 and letter != 113 checks if the current ASCII value is neither 101 ('e') nor 113 ('q').

Print: print("{}".format(chr(letter)), end="") prints each character corresponding to the ASCII value, using end="" to avoid newline characters between prints.

This code will output all letters of the alphabet except 'e' and 'q'.

output:
abcdfghijklmnoprstuvwxyz

4-print_hexa.py

Explanation:
Range: range(0, 99) iterates through numbers from 0 to 98.

{:x}: In the format string, {:x} formats the number as a lowercase hexadecimal without the "0x" prefix. The "0x" is added manually in the string.

print function: This prints each number in the required format.

output:
0 = 0x0
1 = 0x1
2 = 0x2
...
97 = 0x61
98 = 0x62

./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
19 = 0x13
20 = 0x14
21 = 0x15
22 = 0x16
23 = 0x17
24 = 0x18
25 = 0x19
26 = 0x1a
27 = 0x1b
28 = 0x1c
29 = 0x1d
30 = 0x1e
31 = 0x1f
32 = 0x20
33 = 0x21
34 = 0x22
35 = 0x23
36 = 0x24
37 = 0x25
38 = 0x26
39 = 0x27
40 = 0x28
41 = 0x29
42 = 0x2a
43 = 0x2b
44 = 0x2c
45 = 0x2d
46 = 0x2e
47 = 0x2f
48 = 0x30
49 = 0x31
50 = 0x32
51 = 0x33
52 = 0x34
53 = 0x35
54 = 0x36
55 = 0x37
56 = 0x38
57 = 0x39
58 = 0x3a
59 = 0x3b
60 = 0x3c
61 = 0x3d
62 = 0x3e
63 = 0x3f
64 = 0x40
65 = 0x41
66 = 0x42
67 = 0x43
68 = 0x44
69 = 0x45
70 = 0x46
71 = 0x47
72 = 0x48
73 = 0x49
74 = 0x4a
75 = 0x4b
76 = 0x4c
77 = 0x4d
78 = 0x4e
79 = 0x4f
80 = 0x50
81 = 0x51
82 = 0x52
83 = 0x53
84 = 0x54
85 = 0x55
86 = 0x56
87 = 0x57
88 = 0x58
89 = 0x59
90 = 0x5a
91 = 0x5b
92 = 0x5c
93 = 0x5d
94 = 0x5e
95 = 0x5f
96 = 0x60
97 = 0x61
98 = 0x62

5-print_comb2.py

Explanation:
Range: range(0, 99) iterates through numbers from 0 to 98.

{:x}: In the format string, {:x} formats the number as a lowercase hexadecimal without the "0x" prefix. The "0x" is added manually in the string.

print function: This prints each number in the required format.

Explanation:
range(100): The loop iterates over numbers from 0 to 99.

{:02d}: This formatting ensures each number is printed with at least two digits. For example, 0 becomes 00, 9 becomes 09, etc.

Conditional Statement:

If the current number is less than 99, print it followed by , , and use end="" to avoid moving to the next line.
If the number is 99, print it without a trailing comma and space, ensuring the output ends correctly with 99 followed by a newline.
This program meets the constraints of using no more than two print functions and only one loop, without storing numbers or strings in variables or importing any modules.

./5-print_comb2.py
output:
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99

6-print_comb3.py

Explanation:
First loop (for i in range(0, 10)): This loop iterates over the first digit from 0 to 9.

Second loop (for j in range(i + 1, 10)): This loop iterates over the second digit from i+1 to 9. This ensures that the two digits are different and that combinations like 01 and 10 are not repeated.

Conditional Statement:

If the pair of digits is 89 (the last valid combination), it is printed without a trailing comma and space to ensure the output format is correct.
Otherwise, each combination is printed followed by a comma and a space, using end="" to keep printing on the same line.
This code meets all the constraints of using no more than two loops, no more than three print functions, and it does not store numbers or strings in variables or import any modules. The output is in ascending order, with the smallest combination printed first.

./6-print_comb3.py
output:
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89

7-islower.py

Explication
Importation de la fonction : islower = __import__('7-islower').islower importe la fonction islower depuis le fichier 7-islower.py.
Tests :
Chaque appel à islower est formaté pour afficher si le caractère est "lower" (minuscule) ou "upper" (majuscule) selon le résultat retourné par la fonction.
Exécution
Assurez-vous que les fichiers 7-islower.py et 7-main.py sont dans le même répertoire. Puis, exécutez 7-main.py en utilisant la commande suivante dans votre terminal :

./7-main.py

output:
a is lower
H is upper
A is upper
3 is upper
g is lower

Assurez-vous que 7-islower.py contient uniquement la définition de la fonction islower, et que 7-main.py est configuré pour tester la fonction comme décrit.

8-uppercase.py

Explanation
Loop through each character: The loop iterates over each character in the string.

Check if the character is lowercase:

ord(char) >= 97 and ord(char) <= 122: This checks if the character is a lowercase letter.
Convert to uppercase:

If the character is lowercase, convert it to uppercase by subtracting 32 from its ASCII value and then converting it back to a character using chr().
Print the character:

Use print("{}".format(char), end="") to print each character without a newline after each character.
The print("") after the loop ensures that a newline is printed after the entire string.

8-main.py

output
BEST
BEST SCHOOL 98 BATTERY STREET

9-print_last_digit.py

Explanation
abs(number): This ensures that if the input number is negative, it becomes positive before we extract the last digit.

number % 10: This operation gives the last digit of the number. For example:

98 % 10 = 8
-1024 % 10 = 4 (because we use abs() to convert -1024 to 1024).
Print the last digit: Use print("{}".format(last_digit), end="") to print the last digit without a newline after the output.

Return the last digit: The function also returns the value of the last digit, as specified.

Testing
You can test the function with the following 9-main.py script:
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

Expected Output
Running ./9-main.py should produce the following output:
8044

Breakdown of Output:
The last digit of 98 is 8, which is printed.
The last digit of 0 is 0, which is printed.
The last digit of -1024 is 4, which is printed and returned by the function.

10-add.py

Explanation
a + b: This adds the two integers a and b and returns the result.
The function simply returns the sum of the two integers.
Testing
You can test the function with the following 10-main.py script:

Expected Output
Running ./10-main.py should produce the following output:
3
98
98

11-pow.py

Explanation
a ** b: This computes a raised to the power of b. This works for both positive and negative exponents, and it can handle any integer or floating-point numbers.

Testing
You can test the function with the following 11-main.py script:

Expected Output
Running ./11-main.py should produce the following output:
4
9604
1
0.0001
-1024

12-fizzbuzz.py
