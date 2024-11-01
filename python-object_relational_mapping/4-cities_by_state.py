#!/usr/bin/python3
"""
Module: 4-cities_by_state

This script connects to a MySQL database and lists all cities in the `cities`
table of `hbtn_0e_4_usa`, along with their corresponding state names.

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
    - Executes a single SQL query to fetch city names, city ids, and their
    associated state names
    - Sorts and displays results by `cities.id` in ascending order
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and lists all cities with their respective
    state names,     sorted by `cities.id`.
    """
    # Get MySQL username, password, and database name from command-line
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

    # Execute the SQL query to fetch city details and their associated state
    # names
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
