#!/usr/bin/python3
"""
Module: 5-filter_cities

This script connects to a MySQL database and lists all cities in a specified
state from the `cities` table of `hbtn_0e_4_usa`.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name>
    <state_name>

Positional Arguments:
    mysql_username    -- MySQL username
    mysql_password    -- MySQL password
    database_name     -- Name of the MySQL database
    state_name        -- Name of the state to filter cities by (SQL injection
    free)

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
    # Get MySQL username, password, database name, and state name from
    # command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname
                         )
    cursor = db.cursor()

    # Execute the SQL query to fetch city names for the given state name, safe
    # from SQL injection
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
