#!/usr/bin/python3
"""
This script connects to a MySQL database and
retrieves the namesof cities in a specific state.
It uses INNER JOIN to combine data from the
'cities' and 'states' tables and filters
results based on the given state name.
The script takes four command-line arguments:
<username>, <password>, <database>, and <state_name>.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    d = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], d=sys.argv[3])
    s = d.cursor()
    s.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([cy[2] for cy in s.fetchall() if cy[4] == sys.argv[4]]))
