#!/usr/bin/python3
"""
This module lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def cities_by_state(username, password, db_name):
    """
    This function retrieves and lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT * FROM cities ORDER BY cities.id")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    cities_by_state(username, password, db_name)
