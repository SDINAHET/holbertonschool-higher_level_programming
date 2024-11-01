#!/usr/bin/python3
"""
Module 2-my_filter_states

This script connects to a MySQL database and lists all values
in the `states` table of the `hbtn_0e_0_usa` database where the
`name` matches the given argument.

The script takes four command-line arguments:
1. MySQL username
2. MySQL password
3. Database name
4. State name to search for

It connects to a MySQL server running on `localhost` at port `3306`,
executes a query to find matching states by name, sorted by `id`
in ascending order, and prints each row retrieved.

Example usage:
    ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name>
    <state_name>
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and retrieves states that match the provided
    name.
    Results are sorted in ascending order by states.id.
    """
    # Get MySQL username, password, database name, and state name from command
    # line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
        )
    cursor = db.cursor()

    # Execute SQL query to select states where the name matches the argument
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(state_name)
    )
    cursor.execute(query)

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
