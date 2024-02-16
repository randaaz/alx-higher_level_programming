#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves records
from the 'states' table based on a provided state name pattern.
It takes five command-line arguments:
<username>, <password>, <database>, <state_name_pattern>, and <charset>.
The script queries the 'states' table for records whose 'name' column
matches the provided pattern using a parameterized query.
It prints the details of the matching states,
ordered by ID in ascending order.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    s = db.cursor()
    s.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(cities) for cities in s.fetchall()]
