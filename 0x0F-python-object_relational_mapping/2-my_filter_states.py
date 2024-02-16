#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves
records from the 'states' table based on a provided state name pattern.
It takes four command-line
arguments: <username>, <password>, <database>, and <state_name_pattern>.
The script queries the 'states' table
for records whose 'name' column matches the provided pattern.
It prints the details of the matching states,
ordered by ID in ascending order.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    s = db.cursor()
    s.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = s.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    s.close()
    db.close()
