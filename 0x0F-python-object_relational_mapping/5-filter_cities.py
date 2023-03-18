#!/usr/bin/python3
"""Create mysql cursor connector for select item from tables"""

import MySQLdb


def main(argvs):
    """
      lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("""
        SELECT cities.name FROM cities \
        LEFT JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY cities.id ASC """, (argvs[3],))
    query_rows = cur.fetchall()
    ct = []
    for row in query_rows:
        ct.append("".join(row))
    print(", ".join(c for c in ct))
    cur.close()
    conn.close()


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
