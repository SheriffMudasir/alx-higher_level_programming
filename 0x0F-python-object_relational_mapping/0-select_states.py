#/usr/bin/python3
"""
This script list all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

def list_states(username, password, db_name):
    """
    This function retrieves and list all states from MySQL database
    """

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

    if __name__ == "__main__":
        if len(sys.argv) != 4:
            sys.exit(1)
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states(username, password, db_name)
