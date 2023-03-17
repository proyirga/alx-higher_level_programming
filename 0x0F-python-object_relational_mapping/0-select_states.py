#!/usr/bin/pyhton3

"""A script that lists all states from the database hbtn_0e_0_usa:

Arguments: mysql username, mysql password and database name.

"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connection = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db_connection.cursor()

    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()

    for row in rows:
        print(row)
