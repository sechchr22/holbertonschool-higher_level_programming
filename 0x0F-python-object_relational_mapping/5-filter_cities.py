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
    arg = argv[4]
    filtered_arg = arg.split(';')

    if len(filtered_arg) is 1:

        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            port=3306,
            db=database)

    cur = db.cursor()

    cur.execute(
        "SELECT DISTINCT cities.name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = '{}')".format(
            filtered_arg[0]))
    rows = cur.fetchall()
    print(", ".join([i[0] for i in rows]))
    cur.close()
    db.close()
