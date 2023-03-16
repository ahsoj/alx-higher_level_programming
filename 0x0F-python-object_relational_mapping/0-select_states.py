#!/usr/bin/python3
"""Create mysql cursor connector for selectings item from tables"""

import MySQLdb
import sys


def main(argvs):
    """
    lists all states from the database hbtn_0e_0_usa
    """
    conn = MySQLdb.connect(
            host="localhost", 
            port=3306, 
            user=f"{argvs[0]}", 
            passwd=f"{argvs[1]}", 
            db=f"{argvs[2]}", 
            charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main(sys.argv[1:])
