#!/usr/bin/python3
"""
This script lists all states with a name starting with N from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    This function retrieves and lists all states with a name starting with N from MySQL database
    """

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states(username, password, db_name)
