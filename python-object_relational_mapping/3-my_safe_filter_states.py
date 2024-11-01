#!/usr/bin/python3
"""
Module: 3-my_safe_filter_states

This script connects to a MySQL database and lists all states in the `states`
table where the `name` matches a specified argument. The query is safely
executed to prevent SQL injection by using parameterized queries.

Usage:
    ./3-my_safe_filter_states.py <mysql_username> <mysql_password>
    <database_name> <state_name>

Positional Arguments:
    mysql_username    -- MySQL username
    mysql_password    -- MySQL password
    database_name     -- Name of the MySQL database
    state_name        -- Name of the state to search for in the `states` table

Requirements:
    - MySQLdb module (import MySQLdb) for MySQL connectivity
    - MySQL server must be running on localhost at port 3306

Example:
    To list all states with the name "Arizona":
        $ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa "Arizona"
    Output:
        (2, 'Arizona')

Functionality:
    - Establishes a connection to a local MySQL database
    - Executes a parameterized SQL query to fetch rows where `name` matches
    the provided `state_name`
    - Sorts and displays results by `states.id` in ascending order

Notes:
    - The use of parameterized queries ensures that user input is escaped,
    mitigating SQL injection risks.
    - Results are displayed as they appear in the database and sorted by
    `states.id`.
    - The code will not execute if imported as a module due to the
    `if __name__ == "__main__":` block.
"""

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
