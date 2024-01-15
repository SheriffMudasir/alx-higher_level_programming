#!/usr/bin/python3
"""
This module lists cities of a state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def filter_cities(username, password, db_name, name):
    """
    This function takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
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
    mysql_query = "SELECT * FROM cities WHERE state_id IN (SELECT id FROM states WHERE name=%s) ORDER BY id ASC"

    cur.execute(mysql_query, (name,))

    cities = [cities_row[2] for cities_row in cur.fetchall()]
    print(', '.join(cities))

    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, db_name, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    filter_cities(username, password, db_name, name)

