#!/usr/bin/python3
"""
Shows rows that matches with the arg but this on is
safe from Mysql injections
"""
import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]
arg = argv[4]
filtered_arg = arg.split(';')

if len(filtered_arg) = 1:

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        port=3306,
        db=database)
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{}' ORDER BY states.id".format(filtered_arg[0]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
