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
