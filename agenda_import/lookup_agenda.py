import sqlite3
import sys
from db_table import db_table



print(sys.argv)

# mystr = "\"" + x.lstrip("*") + "\""
# data = [x.replace("'", "") for x in data]   # be careful cuz some letters are illegal in name

if len(sys.argv) == 3:
    colmn = "\"" + sys.argv[1].lstrip("*") + "\""
    data = "\"" + sys.argv[-1].replace("'", "") + "\""
    conn = sqlite3.connect("interview_test.db")
    cur = conn.cursor()
    print("SELECT * FROM users WHERE "+colmn+" = "+data)
    cur.execute("SELECT DISTINCT * FROM users WHERE "+colmn+" = "+data+" OR ParentID = (SELECT ID FROM users WHERE "+colmn+" = "+data+") ORDER BY ID;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

test = "SELECT * FROM users WHERE colmn = data UNION ALL SELECT * FROM users WHERE ParentID = (SELECT ID FROM users WHERE colmn = data) ORDER BY ID; "
test2 = "SELECT distinct ParentID from (SELECT * FROM users WHERE "+colmn+" = "+data+" OR ParentID = (SELECT ID FROM users WHERE "+colmn+" = "+data+") ORDER BY ID;) T"