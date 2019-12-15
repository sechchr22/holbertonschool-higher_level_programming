#!/usr/bin/python3
"""
module to list all states from database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        port=3306,
        db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
