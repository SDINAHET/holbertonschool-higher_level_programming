#!/usr/bin/python3
"""
Module 1-filter_states

This script connects to a MySQL database and lists all states
from the database `hbtn_0e_0_usa` with names starting with 'N'.

The script takes three command-line arguments:
1. MySQL username
2. MySQL password
3. Database name

It connects to a MySQL server running on `localhost` at port `3306`,
executes a query to select all states whose name starts with 'N'
(case-sensitive), sorted by `id` in ascending order, and prints each row
retrieved.

Example usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and retrieves all states starting with 'N'.
    Results are sorted in ascending order by states.id.
    """
    # Get MySQL username, password, and database name from command line
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
        )
    cursor = db.cursor()

    # Execute the SQL query to select states starting with 'N'
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
