#!/usr/bin/python3
"""
This module displays all values in the states table of hbtn_0e_0_usa
"""
import MySQLdb
import sys


def my_safe_filter_states(username, password, db_name, name):
    """
    This function displays all values in the states where name matches the argument in a safe way
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
    mysql_query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    cur.execute(mysql_query, (name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password db_name name".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    my_safe_filter_states(username, password, db_name, name)

