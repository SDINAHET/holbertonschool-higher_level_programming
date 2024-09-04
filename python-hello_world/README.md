readme of project2
#!/usr/bin/python3 et rendre executable chmod a+x *

2-print.py

python3 2-print.py
"Programming is like building a multilingual puzzle

3-print_number.py

python3 3-print_number.py
98 Battery street

4-print_float.py

python3 4-print_float.py
Float: 3.14

5-print_string.py

python3 5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton

6-concat.py

python3 6-concat.py
Welcome to Holberton School!

1ere version
#!/usr/bin/python3
str1 = "Welcome to"
str2 = "Holberton School!"
print(str1 + " " + str2)
2ème version
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str3 = str1 + " " + str2
print(f"Welcome to {str3}!")

7-edges.py

python3 7-edges.py

First 3 letters: Hol
Last 2 letters: on
Middle word: olberto


8-concat_edges.py

python3 8-concat_edges.py

object-oriented programming with Python

1ere version
#!/usr/bin/python3

str = "Python is an interpreted, interactive, object-oriented programming` language that combines remarkable power with very clear syntax"
print(str[39:66] + str[106:112] + str[:6])

2ème version:
#!/usr/bin/python3

str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
print(str[39:66] + str[106:112] + str[:6])

3ème version:
#!/usr/bin/python3
str = ("Python is an interpreted, interactive, object-oriented programming"
       " language that combines remarkable power with very clear syntax")
print(str[39:66] + str[-17:-11] + str[:6])

4eme version:
#!/usr/bin/python3
str = ("Python is an interpreted, interactive, object-oriented programming "
       "language that combines remarkable power with very clear syntax")
print(str[39:66] + str[106:112] + str[:6])

5ème version
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[39:66] + str[106:112] + str[:6])

6ème version
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[39:66] + str[106:112] + str[:6])

7ème version
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[39:66] + str[106:113] + str[:6])

8ème version:
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[39:66] + str[106:112] + str[:6])

9ème version:
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[39:67] + str[107:112] + str[:6])

9-easter_egg.py

python3 9-easter_egg.py

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
