#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves records
from the 'states' table.It takes three command-line
arguments: <username>, <password>, and <database>.
The script then prints the details of states whose
names start with the letter 'N'.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    s = db.cursor()
    s.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in s.fetchall() if state[1][0] == "N"]
