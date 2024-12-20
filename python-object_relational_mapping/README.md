# SQL - Python Object Relational Mapping

![Project badge](https://img.shields.io/badge/Progress-80%25-orange)

## Project Overview

- **Level**: Amateur
- **Weight**: 1
- **Your score will be updated as you progress.**

## Before you start…

Please make sure your MySQL server is in 8.0.
**How to install MySQL 8.0 in Ubuntu 22.04** --> https://intranet.hbtn.io/rltoken/MrRq4s05-Qo6TOgGKWIumA

### Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries, only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

### Without ORM:
```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")  # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### With ORM
```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():  # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

# Resources
Read or watch:

Object-relational mappers --> https://intranet.hbtn.io/rltoken/tCytNeWUzuWhAn9APwtp9A
mysqlclient/MySQLdb documentation --> https://intranet.hbtn.io/rltoken/V8KJv3QCReECPZ0V-kXRwg
MySQLdb tutorial --> https://intranet.hbtn.io/rltoken/j_7jU3C9Jsa0o53pgfwxOQ
SQLAlchemy tutorial --> https://intranet.hbtn.io/rltoken/7y1s8FDE_0S-uhBtCgt5-A
SQLAlchemy --> https://intranet.hbtn.io/rltoken/j6kxlUETdjiFwiu0k_JI6Q
mysqlclient/MySQLdb --> https://intranet.hbtn.io/rltoken/vzsiR8tCdY3_OWsMH33jUA
Introduction to SQLAlchemy --> https://intranet.hbtn.io/rltoken/7m6F57mBASM7A2r_GcIeMA
Flask SQLAlchemy --> https://intranet.hbtn.io/rltoken/riV6WcWo1MGRpF3WSmv4Zw
10 common stumbling blocks for SQLAlchemy newbies --> https://intranet.hbtn.io/rltoken/uRrjdEkHmjrVenCqjwJRWQ
Python SQLAlchemy Cheatsheet --> https://intranet.hbtn.io/rltoken/RfLwdV21O_TVoQU4iwaIFw
SQLAlchemy ORM Tutorial for Python Developers --> https://intranet.hbtn.io/rltoken/2BoGpuT2vAaoeuC3SN_wPA
SQLAlchemy Tutorial --> https://intranet.hbtn.io/rltoken/DrwY56jSHCOADKEbSOBa0A

# Describe Ressource
Here are some useful resources and tutorials covering object-relational mappers (ORMs) in Python, focusing on SQLAlchemy and MySQLdb, as well as their integration with Flask:

1. Object-Relational Mappers (ORMs)
ORMs allow developers to interact with databases using Python objects rather than raw SQL queries, making it easier to manage database operations.
SQLAlchemy is a popular Python ORM that works with multiple databases, including MySQL and PostgreSQL.
MySQLdb (a MySQL client for Python) is lower-level than ORMs and directly executes SQL commands.
2. mysqlclient / MySQLdb Documentation
mysqlclient/MySQLdb Documentation
Documentation for mysqlclient, which is a fork of MySQLdb. This library provides an interface to MySQL databases and allows for direct SQL execution.
3. MySQLdb Tutorial
MySQLdb User Guide
A guide on using MySQLdb to interact with MySQL databases. It explains how to set up connections, execute SQL queries, and retrieve data.
4. SQLAlchemy Tutorial
SQLAlchemy 2.0 Tutorial
This official SQLAlchemy 2.0 tutorial covers core SQLAlchemy concepts and step-by-step usage of the ORM to manage database tables and queries.
5. SQLAlchemy Documentation
SQLAlchemy ORM Documentation
Comprehensive documentation on SQLAlchemy's ORM layer, including how to create tables, define relationships, perform queries, and handle transactions.
6. Introduction to SQLAlchemy
Introduction to SQLAlchemy
This beginner-friendly tutorial series explains how SQLAlchemy works, starting from creating an engine and session, defining tables and relationships, and executing queries.
7. Flask-SQLAlchemy
Flask-SQLAlchemy Documentation
Flask-SQLAlchemy simplifies the integration of SQLAlchemy with Flask applications, adding convenience functions for managing database connections within Flask's request context.
8. 10 Common Stumbling Blocks for SQLAlchemy Newbies
10 Common Stumbling Blocks for SQLAlchemy Newbies
This article explains common mistakes and misconceptions new users encounter with SQLAlchemy, helping avoid common pitfalls with the ORM.
9. Python SQLAlchemy Cheatsheet
SQLAlchemy Cheatsheet
A quick-reference cheatsheet with SQLAlchemy commands and operations for connecting, querying, and handling transactions in SQLAlchemy.
10. SQLAlchemy ORM Tutorial for Python Developers
SQLAlchemy ORM Tutorial
Though focused on PostgreSQL, this tutorial provides a practical overview of SQLAlchemy ORM. The concepts, like defining models and relationships, are applicable to any SQL database.
11. SQLAlchemy Tutorial by DigitalOcean
SQLAlchemy Tutorial
A DigitalOcean tutorial on using SQLAlchemy with MySQL, including setup, connecting to the database, and executing basic ORM operations.

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
How to connect to a MySQL database from a Python script
How to `SELECT` rows in a MySQL table from a Python script
How to `INSERT` rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table

## Describe concept
To interact with a MySQL database in Python, you can use libraries like mysql-connector-python or SQLAlchemy, which provide tools for connecting to the database, running queries, and managing data.

Here’s a breakdown:

1. Connecting to a MySQL Database from a Python Script
To connect to a MySQL database, you can use the mysql-connector-python library.

Installation:
```bash
pip install mysql-connector-python
```
Code Example:
```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()
```
2. Selecting Rows in a MySQL Table from a Python Script
Once connected, you can select rows from a table using SQL queries.

Code Example:
```python
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print the result
for row in rows:
    print(row)
```

3. Inserting Rows in a MySQL Table from a Python Script
To insert rows into a table, you can use INSERT statements with placeholders.

Code Example:
```python
query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
values = ("value1", "value2")

cursor.execute(query, values)
conn.commit()  # Save changes

print(cursor.rowcount, "record inserted.")
```

4. What ORM (Object-Relational Mapping) Means
ORM stands for Object-Relational Mapping. It's a technique that allows you to interact with a database using high-level, object-oriented code rather than writing raw SQL queries. This is particularly helpful for making code more readable, maintainable, and abstracting away database-specific details. ORM frameworks map tables in a database to classes in code, where each row represents an instance of that class.

Popular Python ORMs include SQLAlchemy and Django ORM.

5. Mapping a Python Class to a MySQL Table Using SQLAlchemy
To map a Python class to a MySQL table with SQLAlchemy, define a class and link it to a table by using a Base class.

Installation:
```bash
pip install sqlalchemy
```

Code example:
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection
engine = create_engine("mysql+mysqlconnector://yourusername:yourpassword@localhost/yourdatabase")

# Define the base class
Base = declarative_base()

# Define the table as a Python class
class YourTable(Base):
    __tablename__ = 'your_table'  # This is the name of the MySQL table

    id = Column(Integer, primary_key=True)
    column1 = Column(String(255))
    column2 = Column(String(255))

# Create the table in the database
Base.metadata.create_all(engine)

# Start a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert a new row
new_row = YourTable(column1="value1", column2="value2")
session.add(new_row)
session.commit()
```

# Requirements
## General
Allowed editors: `vi`, `vim`, `emacs`

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)

Your files will be executed with `MySQLdb` version `2.0.x`

Your files will be executed with `SQLAlchemy` version `1.4.x`

All your files should end with a new line

The first line of all your files should be exactly `#!/usr/bin/python3`

A `README.md` file, at the root of the folder of the project, is mandatory

Your code should use the pycodestyle (version 2.7.*)

All your files must be executable

The length of your files will be tested using `wc`

All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)`)

All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)`)

All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)`)

A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
You are not allowed to use `execute` with SQLAlchemy.

# More Info
## Install MySQL 8.0 on Ubuntu 20.04 LTS
```python
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
Connect to your MySQL server:
```python
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

## Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed.
```python
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```
## Install SQLAlchemy module version 1.4.x
```python
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```
Also, you can have this warning message:
```python
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
  cursor.execute(statement, parameters)
```
You can ignore it.

## Installation Problem: Install MySQLdb module version 2.0.x

It appears that pkg-config is missing, which is required to compile mysqlclient. Here's how you can resolve this on Ubuntu:

1. Install pkg-config and necessary MySQL development libraries:
```bash
sudo apt update
sudo apt install pkg-config python3-dev libmysqlclient-dev
```

- pkg-config is needed to locate library paths and flags for compiling.

- python3-dev includes the Python headers required to build Python packages.

- libmysqlclient-dev contains the MySQL client library, which mysqlclient depends on.

2. Install mysqlclient: After installing the dependencies, try installing mysqlclient again:
```bash
sudo pip3 install mysqlclient
```



# Tasks:

`0.Get all states`

`1.Filter states`

`2.Filter states by user input`

`3.SQL Injection...`

`4.Cities by states`

`5.All cities by state`

`6.First state model`

`7.All states via SQLAlchemy`

`8.First state`

`9.Contains a`

`10.Get a state`

`11.Add a new state`

`12.Update a state`

`13.Delete states`

`14.Cities in state`

## 0. Get all states
***mandatory***

Write a script that lists all `states` from the database `hbtn_0e_0_usa`:

-Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
-You must use the module `MySQLdb` (`import MySQLdb`)
-Your script should connect to a MySQL server running on `localhost` at port `3306`
-Results must be sorted in ascending order by `states.id`
-Results must be displayed as they are in the example below
-Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `0-select_states.py`


```python
#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    # Fetch MySQL username, password, and database name from command line
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
        )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result of the query
    states = cursor.fetchall()

    # Print each row
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 0-select_states.py
```

Both commands execute SQL commands from the file 0-select_states.sql in MySQL, but there’s a slight difference in how they work:

1. `cat 0-select_states.sql | mysql -uroot -p`:

- This command uses cat to output the contents of 0-select_states.sql and pipes it (|) into MySQL.
- Here, mysql -uroot -p receives the SQL commands from standard input (STDIN).
- This approach is often used for chaining commands or when additional processing on the file contents is needed before passing it to MySQL.

2. `mysql -uroot -p < 0-select_states.sql`:

- This command directly redirects the content of 0-select_states.sql into MySQL using <.
- It achieves the same result, running the commands from the file in MySQL, but is more efficient as it doesn’t require cat to first output the file contents.
- This is often the preferred method for simplicity and efficiency.

In most cases, both commands will yield the same result, but mysql -uroot -p < 0-select_states.sql is slightly more efficient since it doesn’t involve an extra process (cat).


## Filter states

Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `1-filter_states.py`


```python
#!/usr/bin/python3
import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and retrieves all states starting with 'N'.
    Results are sorted in ascending order by states.id.
    """
    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cursor = db.cursor()

    # Execute the SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 1-filter_states.py
```

## 2. Filter states by user input
***mandatory***

Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
You must use the module `MySQLdb` (`import MySQLdb`)
Your script should connect to a MySQL server running on `localhost` at port `3306`
You must use `format` to create the SQL query with the user input
Results must be sorted in ascending order by `states.id`
Results must be displayed as they are in the example below
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `2-my_filter_states.py`


```python
#!/usr/bin/python3
import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and retrieves states that match the provided name.
    Results are sorted in ascending order by states.id.
    """
    # Get MySQL username, password, database name, and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cursor = db.cursor()

    # Execute SQL query to select states where the name matches the argument
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
```


Rules pycodstyle:
```python
 # Execute SQL query to select states where the name matches the argument
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)
```
to
```python
    # Execute SQL query to select states where the name matches the given argument
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(state_name)
    )
    cursor.execute(query)
```

```python
query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
cursor.execute(query, (state_name,))
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 2-my_filter_states.py
```

## 3. SQL Injection...
***mandatory***

Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` as an input?

```bash guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/$
```
What? Empty?

Yes, it’s an `SQL injection` to delete all records of a table… https://en.wikipedia.org/wiki/SQL_injection

Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
You must use the module `MySQLdb` (`import MySQLdb`)
Your script should connect to a MySQL server running on `localhost` at port `3306`
Results must be sorted in ascending order by `states.id`
Results must be displayed as they are in the example below
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `3-my_safe_filter_states.py`


```python
#!/usr/bin/python3

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database, retrieves and displays states with names
    matching a provided argument. Results are sorted by `states.id`.
    """
    # Fetch MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Execute the SQL query using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 3-my_safe_filter_states.py
```

## 4. Cities by states
***mandatory***

Write a script that lists all `cities` from the database `hbtn_0e_4_usa`

Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
You must use the module `MySQLdb` (`import MySQLdb`)
Your script should connect to a MySQL server running on `localhost` at port `3306`
Results must be sorted in ascending order by `cities.id`
You can use only `execute`() once
Results must be displayed as they are in the example below
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `4-cities_by_state.py`


```python
#!/usr/bin/python3
"""
Module: 4-cities_by_state

This script connects to a MySQL database and lists all cities in the `cities` table
of `hbtn_0e_4_usa`, along with their corresponding state names.

Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>

Positional Arguments:
    mysql_username    -- MySQL username
    mysql_password    -- MySQL password
    database_name     -- Name of the MySQL database

Requirements:
    - MySQLdb module (import MySQLdb) for MySQL connectivity
    - MySQL server must be running on localhost at port 3306

Example:
    To list all cities with state names:
        $ ./4-cities_by_state.py root root hbtn_0e_4_usa
    Output:
        (1, 'San Francisco', 'California')
        (2, 'San Jose', 'California')
        ...

Functionality:
    - Establishes a connection to a local MySQL database
    - Executes a single SQL query to fetch city names, city ids, and their associated state names
    - Sorts and displays results by `cities.id` in ascending order
"""
import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and lists all cities with their respective state names,
    sorted by `cities.id`.
    """
    # Get MySQL username, password, and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cursor = db.cursor()

    # Execute the SQL query to fetch city details and their associated state names
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 4-cities_by_state.py
```

## 5. All cities by state
***mandatory***

Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
You must use the module `MySQLdb` (`import MySQLdb`)
Your script should connect to a MySQL server running on `localhost` at port `3306`
Results must be sorted in ascending order by `cities.id`
You can use only `execute()` once
The results must be displayed as they are in the example below
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `5-filter_cities.py`


```python
#!/usr/bin/python3
"""
Module: 5-filter_cities

This script connects to a MySQL database and lists all cities in a specified
state from the `cities` table of `hbtn_0e_4_usa`.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>

Positional Arguments:
    mysql_username    -- MySQL username
    mysql_password    -- MySQL password
    database_name     -- Name of the MySQL database
    state_name        -- Name of the state to filter cities by (SQL injection free)

Requirements:
    - MySQLdb module (import MySQLdb) for MySQL connectivity
    - MySQL server must be running on localhost at port 3306

Example:
    To list all cities in the state of Texas:
        $ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
    Output:
        Dallas, Houston, Austin
"""
import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and lists all cities of a specified state,
    sorted by `cities.id`.
    """
    # Get MySQL username, password, database name, and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cursor = db.cursor()

    # Execute the SQL query to fetch city names for the given state name, safe from SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch and print the results as a comma-separated list
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 5-filter_cities.py
```

Explanation:
1. SQL Injection Prevention: The execute() method uses %s as a placeholder for state_name in the query, protecting against SQL injection.
2. Query Execution: The query fetches all cities belonging to the specified state_name by joining the cities and states tables.
3. Formatting: The city names are printed as a comma-separated list.
4. Execution Guard: The if __name__ == "__main__": block ensures the script only executes if run directly.

## 6.First state model
***mandatory***

Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

`State` class:
	inherits from `Base` `Tips`--> https://intranet.hbtn.io/rltoken/62tIVCmGm735_tJWLxtJrQ / https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html
	links to the MySQL table `states`
	class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
	class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
You must use the module `SQLAlchemy`
Your script should connect to a MySQL server running on `localhost` at port `3306`
WARNING: all classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`
```bash
guillaume@ubuntu:~/$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password:
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password:
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `model_state.py`


```python
#!/usr/bin/python3
"""Defines a State class linked to the states table in the MySQL database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for the declarative model
Base = declarative_base()

class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id (int): The state's id, primary key, auto-incremented, non-nullable.
        name (str): The state's name, string with max 128 characters,
        non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x model_state.py
```

Explanation

`Base = declarative_base()`: This initializes a base class for the SQLAlchemy models.

`State` class:

    - `__tablename__`: Specifies the table name as `states`.

    - Columns:

        - `id`: An auto-incrementing integer column that serves as the primary key.

        - `name`: A string column with a maximum length of 128 characters and cannot be `NULL`.

Example Usage to Create the Table
You can use the following code to connect to the database and create the `states` table by running this script. Make sure to replace `sys.argv[1]`, `sys.argv[2]`, and `sys.argv[3]` with your MySQL username, password, and database name.

```python
#!/usr/bin/python3
"""Start link class to table in database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
```

Running the Script
To create the `states` table, execute this script from the command line:

```bash
$ ./6-model_state.py root root hbtn_0e_6_usa
```

This will create the `states` table in your database `hbtn_0e_6_usa` if it does not already exist.

## 7.All states via SQLAlchemy
***mandatory***

Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
You must use the module `SQLAlchemy`
You must import `State` and `Base` from `model_state` - `from model_state import Base`, `State`
Your script should connect to a MySQL server running on `localhost` at port `3306`
Results must be sorted in ascending order by `states.id`
The results must be displayed as they are in the example below
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password:
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `7-model_state_fetch_all.py`


```python
#!/usr/bin/python3
"""
Module 7-model_state_fetch_all.py

Lists all State objects from the database hbtn_0e_6_usa.

This script connects to a MySQL database using SQLAlchemy and retrieves all
State objects, displaying them in ascending order by their id.

Usage:
    ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>

Example:
    ./7-model_state_fetch_all.py root root hbtn_0e_6_usa

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.

Output:
    Displays each state's id and name in the format "<id>: <name>"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()

    # Display each state's id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 7-model_state_fetch_all.py
```

## 8.First state
***mandatory***

Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
You must use the module `SQLAlchemy`
You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
Your script should connect to a MySQL server running on `localhost` at port `3306`
The state you display must be the first in states.id
You are not allowed to fetch all states from the database before displaying the result
The results must be displayed as they are in the example below
If the table `states` is empty, print `Nothing` followed by a new line
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `8-model_state_fetch_first.py`


```python
#!/usr/bin/python3
"""
Module 8-model_state_fetch_first.py

Prints the first State object from the database hbtn_0e_6_usa.

This script connects to a MySQL database using SQLAlchemy and retrieves the
first State object, displaying it in the format "<id>: <name>". If the table
states is empty, it prints "Nothing".

Usage:
    ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>

Example:
    ./8-model_state_fetch_first.py root root hbtn_0e_6_usa

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.

Output:
    Displays the first state's id and name or "Nothing" if there are no states.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 8-model_state_fetch_first.py
```

## 9.Contains 'a'
***mandatory***

Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
You must use the module `SQLAlchemy`
You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
Your script should connect to a MySQL server running on `localhost` at port `3306`
Results must be sorted in ascending order by `states.id`
The results must be displayed as they are in the example below
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `9-model_state_filter_a.py`


```python
#!/usr/bin/python3
"""
Module 9-model_state_filter_a.py

Lists all State objects from the database hbtn_0e_6_usa that contain
the letter 'a' in their name.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>

Example:
    ./9-model_state_filter_a.py root root hbtn_0e_6_usa

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.

Output:
    Displays each state's id and name that contains the letter 'a', sorted by id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display each state that matches the query
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 9-model_state_filter_a.py
```

## 10.get a state
***mandatory***

Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search` (SQL injection free)
You must use the module `SQLAlchemy`
You must import `State` and `Base` from `model_state` - `from model_state import Base`, `State`
Your script should connect to a MySQL server running on `localhost` at port `3306`
You can assume you have one record with the state name to search
Results must display the `states.id`
If no state has the name you searched for, display `Not found`
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `10-model_state_my_get.py`


```python
#!/usr/bin/python3
"""
Module 10-model_state_my_get.py

Prints the State object with the name passed as an argument from the
database hbtn_0e_6_usa.

Usage:
    ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>

Example:
    ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.
    state_name (str): The name of the state to search.

Output:
    Prints the state id if found; otherwise, "Not found".
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the state name to search
    state_name = sys.argv[4]

    # Query for State object with the specified name using parameterized query
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 10-model_state_my_get.py
```

## 11. Add a new state
***mandatory***

Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`

Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
You must use the module `SQLAlchemy`
You must import `State` and `Base` from `model_state - from model_state import Base`, `State`
Your script should connect to a MySQL server running on `localhost` at port `3306`
Print the new `states.id` after creation
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ ./11-model_state_insert.py root root hbtn_0e_6_usa
6
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `11-model_state_insert.py`


```python
#!/usr/bin/python3
"""
Module 11-model_state_insert.py

Adds the State object “Louisiana” to the database hbtn_0e_6_usa.

Usage:
    ./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.

Output:
    Prints the id of the newly created state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object for "Louisiana" and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the new State object
    print(f"{new_state.id}")

    # Close the session
    session.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 11-model_state_insert.py
```

## 12. Update a state
***mandatory***

Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
You must use the module `SQLAlchemy`
You must import `State` and `Base` from `model_state - from model_state import Base`, `State`
Your script should connect to a MySQL server running on `localhost` at port `3306`
Change the name of the `State` where `id = 2` to `New Mexico`
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `12-model_state_update_id_2.py`


```python
#!/usr/bin/python3
"""
Module 12-model_state_update_id_2.py

Changes the name of the State where id = 2 to "New Mexico" in the database.

Usage:
    ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state with id = 2 and update its name
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 12-model_state_update_id_2.py
```

## 13. Delete states
***mandatory***

Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`

Your script should take 3 arguments: `mysql username, mysql password` and `database name`
You must use the module `SQLAlchemy`
You must import `State` and `Base` from `model_state - from model_state import Base, State`
Your script should connect to a MySQL server running on `localhost` at port `3306`
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
2: New Mexico
4: New York
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File: `13-model_state_delete_a.py`


```python
#!/usr/bin/python3
"""
Module 13-model_state_delete_a.py

Deletes all State objects with a name containing the letter 'a'
from the database.

Usage:
    ./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete all states with 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 13-model_state_delete_a.py
```

## 14. Cities in state
***mandatory***

Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

City class:
inherits from `Base` (imported from `model_state`)
links to the MySQL table `cities`
class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
class attribute `name` that represents a column of a string of 128 characters and can’t be null
class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to `states.id`
You must use the module `SQLAlchemy`
Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:

Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
You must use the module `SQLAlchemy`
You must import `State` and `Base` from `model_state - from model_state import Base, State`
Your script should connect to a MySQL server running on `localhost` at port `3306`
Results must be sorted in ascending order by `cities.id`
Results must be display as they are in the example below (`<state name>: (<city id>) <city name>`)
Your code should not be executed when imported
```bash
guillaume@ubuntu:~/$ cat 14-model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password:
guillaume@ubuntu:~/$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/$
```
No test cases needed

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `python-object_relational_mapping`

File:`model_city.py`, `14-model_city_fetch_by_state.py`

`model_city.py
```python
#!/usr/bin/python3
"""
Defines a City class for use with SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """Represents a city for a MySQL database"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
```


`14-model_city_fetch_by_state.py`
```python
#!/usr/bin/python3
"""
Lists all City objects from the database along with their State names
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Create a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind the engine to the Base metadata
    Base.metadata.create_all(engine)

    # Start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all cities with their associated state names
    results = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()

    # Display the results in the specified format
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
```

Usage
Make sure to set the executable permission and doctring:

```bash
chmod +x 14-model_city_fetch_by_state.py
```
