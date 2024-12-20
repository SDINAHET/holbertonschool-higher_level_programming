# SQL - Introduction

![Project badge](https://img.shields.io/badge/Progress-100%25-green)

## Project Overview

- **Level**: Novice
- **Weight**: 1
- **Your score will be updated as you progress.**

### Description
This project serves as an introduction to SQL and relational databases. It covers fundamental concepts, basic SQL statements, and hands-on tasks to solidify your understanding.

### Concepts
In this project, you will learn the following:

- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create a database in MySQL
- The difference between `DDL` and `DML`
- How to `CREATE` or `ALTER` a table
- How to `SELECT`, `INSERT`, `UPDATE`, or `DELETE` data
- Understanding `subqueries`
- How to use MySQL functions

###  Describe Concepts
Here's a concise introduction to each of these database concepts:

1. What’s a `Database`?

- A database is an organized collection of data that can be easily `accessed`, `managed`, and `updated`. `Databases store data in tables, rows, and columns to facilitate efficient retrieval and manipulation`.

2. What’s a `Relational Database`?

- A relational database stores data in tables with `rows` and `columns`, where `each table represents an entity`, and `each row represents a record`. `Relationships` between tables (like `foreign keys`) help organize and link related data. This structure `allows data` to be `queried using SQL`.

3. What Does `SQL` Stand For?

- `SQL` stands for `Structured Query Language`. It's a programming language specifically designed for managing and manipulating relational databases.

4. What’s `MySQL`?

- MySQL is an open-source relational database management system (`RDBMS`) that uses SQL for data operations. It's widely used in web applications and known for its `reliability`, `performance`, and `ease of use`.

5. How to Create a Database in `MySQL`:

- Use the following `SQL` command:
```sql
CREATE  DATABASE database_name;
```
- Replace `database_name` with your chosen name for the database.

6. What Do `DDL` and `DML` Stand For?

- `DDL` (`Data Definition Language`): Commands that `define` or `alter` the `structure` of the database and tables, such as `CREATE`, `ALTER`, `DROP`.
- `DML` (`Data Manipulation Language`): Commands that `manipulate the data` in `tables`, such as `SELECT`, `INSERT`, `UPDATE`, `DELETE`.

7. How to `CREATE` or `ALTER a Table`

- `CREATE TABLE`: Creates a new table.
```sql
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype,
  ...
);
```
- `ALTER TABLE`: Modifies an existing table
```sql
ALTER TABLE table_name
ADD column_name datatype;
```

8. How to `SELECT Data` from a `Table`

- Use the `SELECT` statement to `retrieve data`:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

9. How to `INSERT`, `UPDATE`, or `DELETE Data`

- `INSERT`: Adds new data to a table
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```
- `UPDATE`: Modifies existing data in a table.
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
- `DELETE`: Removes data from a table
```sql
DELETE FROM table_name
WHERE condition;
```

10. What are Subqueries?

- A subquery is a query nested within another query. It can be used in `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements to provide a value or condition.
```sql
SELECT column1
FROM table_name
WHERE column2 = (SELECT column2 FROM another_table WHERE condition);
```

11. How to Use `MySQL Functions`

- `MySQL` includes built-in functions for operations on data, such as:
	- `Aggregate functions` like `SUM()`, `COUNT()`, `AVG()`, `MIN()`, and `MAX()` for calculations on data sets.
	- `String functions` like `CONCAT()`, `LENGTH()`, `UPPER()`, and `LOWER()` for string manipulation.
	- `Date functions` like `NOW()`, `CURDATE()`, `YEAR()`, and `MONTH()` for handling date and time values.


### Learning Objectives
By the end of this project, you should be able to explain the following concepts without assistance:

- General knowledge of databases and SQL
- Creating and managing databases and tables in MySQL
- Executing basic SQL queries and operations

## Resources
Read or watch the following materials to enhance your understanding:

- [What is Database & SQL?](https://example.com)
- [Install MySQL (MySQL Server)](https://example.com)
- [A Basic MySQL Tutorial](https://example.com)
- [Basic SQL statements: DDL and DML](https://example.com) (no need to read the chapter “Privileges”)
- [Basic queries: SQL and RA](https://example.com)
- [SQL technique: functions](https://example.com)
- [SQL technique: subqueries](https://example.com)
- [Backticks vs. Apostrophes](https://example.com)
- [MySQL Cheat Sheet](https://example.com)
- [MySQL 8.0 SQL Statement Syntax](https://example.com)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- Each SQL query should have a comment just before it
- Each file should start with a comment describing the task
- All SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`)
- A `README.md` file is mandatory at the root of the project folder
- The length of your files will be tested using `wc`

## More Info
### Comments for your SQL file:
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
Connect to your MySQL server:
```bash
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

Tasks

`-0.List databases`: Write a script that lists all databases in your MySQL server.

`-1.Create a database`: Create the database hbtn_0c_0.

`-2.Delete a database`: Delete the database hbtn_0c_0.

`-3.List tables`: List all tables in a specified database.

`-4.First table`: Create a table called first_table in the current database.

`-5.Full description`: Print the description of the first_table.

`-6.List all in table`: List all rows in the first_table.

`-7.First add`: Insert a new row in the first_table.

`-8.Count 89`: Display the number of records with id = 89.

`-9.Full creation`: Create a second_table and insert multiple rows.

`-10.List by best`: List records from second_table ordered by score.

`-11.Select the best`: List records with a score >= 10.

`12.Cheating is bad`: Update Bob's score to 10.

`-13.Score too low`: Remove records with a score <= 5.

`-14.Average`: Compute the average score.

`-15.Number by score`: List the number of records per score.

`-16.Say my name`: List records in second_table with a name value.

***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

## 0. List databases
***mandatory***

Write a script that lists all databases of your MySQL server.

```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `0-list_databases.sql`


```sql
-- Task 0: List all databases
SHOW DATABASES;
```


## 1. Create a database
***mandatory***

Write a script that creates the database `hbtn_0c_0` in your MySQL server.

- If the database `hbtn_0c_0` already exists, your script should not fail.
- You are not allowed to use the `SELECT` or `SHOW` statements.

```bash
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `1-create_database_if_missing.sql`


```sql
-- Task 1: Create a database hbtn_0c_0 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```


## 2. Delete a database
***mandatory***

Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

- If the database `hbtn_0c_0` doesn’t exist, your script should not fail.
- You are not allowed to use the `SELECT` or `SHOW` statements.

```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `2-remove_database.sql`


```sql
-- Task 2: Delete the database hbtn_0c_0 if it exists
DROP DATABASE IF EXISTS hbtn_0c_0;
```


## 3. List tables
***mandatory***

Write a script that lists all the tables of a database in your MySQL server.

- The database name will be passed as an argument of the `mysql` command (in the following example: `mysql` is the name of the database).

```bash
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password:
Tables_in_mysql
columns_priv
component
db
default_roles
engine_cost
func
general_log
global_grants
gtid_executed
help_category
help_keyword
help_relation
help_topic
innodb_index_stats
innodb_table_stats
password_history
plugin
procs_priv
proxies_priv
replication_asynchronous_connection_failover
replication_asynchronous_connection_failover_managed
role_edges
server_cost
servers
slave_master_info
slave_relay_log_info
slave_worker_info
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `3-list_tables.sql`


```sql
-- Task 3: List all tables of a database
SHOW TABLES;
```


## 4. First table
***mandatory***

Write a script that creates a table called `first_table` in the current database in your MySQL server.

**`first_table` description:**
- `id` INT
- `name` VARCHAR(256)

- The database name will be passed as an argument of the `mysql` command.
- If the table `first_table` already exists, your script should not fail.
- You are not allowed to use the `SELECT` or `SHOW` statements.

```bash
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `4-first_table.sql`


```sql
-- Task 4: Create a table called first_table in the current database
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```


## 5. Full description
***mandatory***

Write a script that prints the following description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

- The database name will be passed as an argument of the `mysql` command.
- You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements.

```bash
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Table   Create Table
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `5-full_table.sql`


```sql
-- Task 5: Print the full description of the table first_table
SHOW CREATE TABLE first_table;
```

## 6. List all in table
***mandatory***

Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

- All fields should be printed.
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `6-list_values.sql`


```sql
-- Task 6: List all rows of the table first_table
SELECT * FROM first_table;
```


## 7. First add
***mandatory***

Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

- **New row:**
	- `id` = `89`
	- `name` = `Best School`

- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `7-insert_value.sql`


```sql
-- Task 7: Insert a new row in the table first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```


## 8. Count 89
***mandatory***

Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password:
3
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `8-count_89.sql`


```sql
-- Task 8: Display the number of records with id = 89 in the table first_table
SELECT COUNT(*) FROM first_table WHERE id = 89;
```


## 9. Full creation
***mandatory***

Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and adds multiple rows.

-`second_table` description:

	- `id` INT

	- `name` VARCHAR(256)
	
	- `score` INT

- The database name will be passed as an argument to the `mysql` command.
- If the table `second_table` already exists, your script should not fail.
- You are not allowed to use the `SELECT` and `SHOW` statements.

Your script should create these records:

	- `id` = 1, `name` = “John”, `score` = 10

	- `id` = 2, `name` = “Alex”, `score` = 3

	- `id` = 3, `name` = “Bob”, `score` = 14

	- `id` = 4, `name` = “George”, `score` = 8

```bash
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `9-full_creation.sql`


```sql
-- Task 9: Create a table second_table and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
```


## 10. List by best
***mandatory***

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### Requirements:
- Results should display both the score and the name (in this order).
- Records should be ordered by score (top first).
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `10-top_score.sql`


```sql
-- Task 10: List all records of the table second_table ordered by score
SELECT score, name
FROM second_table
ORDER BY score DESC;
```


## 11. Select the best
***mandatory***

Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Results should display both the score and the name (in this order).
- Records should be ordered by score (top first).
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
14  Bob
10  John
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `11-best_score.sql`


```sql
-- Task 11: List all records with a score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
```


## 12. Cheating is bad
***mandatory***

Write a script that updates the score of Bob to `10` in the table `second_table`.
- You are not allowed to use Bob’s id value, only the `name` field.
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `12-no_cheating.sql`


```sql
-- Task 12: Update the score of Bob to 10 in the second_tableUPDATE second_table
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
```


## 13. Score too low
***mandatory***

Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `13-change_class.sql`


```sql
-- Task 13: Remove all records with a score <= 5 in the second_table
DELETE FROM second_table
WHERE score <= 5;
```


## 14. Average
***mandatory***

Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The result column name should be `average`.
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
average
9.3333
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `14-average.sql`


```sql
-- Task 14: Compute the score average of all records in the second_table
SELECT AVG(score) AS average
FROM second_table;
```


## 15. Number by score
***mandatory***

Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- The result should display:
	- The `score`.
	- The number of records for this `score` with the label `number`.
- The list should be sorted by the number of records (descending).
- The database name will be passed as an argument to the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   number
10  2
8   1
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `15-groups.sql`


```sql
-- Task 15: List the number of records with the same score in the second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
```


## 16. Say my name
***mandatory***

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Don’t list rows without a `name` value.
- Results should display the score and the name (in this order).
- Records should be listed by descending score.
- The database name will be passed as an argument to the `mysql` command.

In this example, new data have been added to the table `second_table`.

```bash
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$
```
***Repo:***

GitHub repository: `holbertonschool-higher_level_programming`

Directory: `SQL_introduction`

File: `16-no_link.sql`


```sql
-- Task 16: List all records with a name value in the second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
```

