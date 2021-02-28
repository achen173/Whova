import sqlite3
import sys
from db_table import db_table


conn = sqlite3.connect("interview_test.db")
cur = conn.cursor()

if len(sys.argv) == 2 and sys.argv[1] == '--help':
    cur.execute("PRAGMA table_info(users)")
    print("\nMake sure to wrap all column name and lookup value in single quotes")
    print("------- List of Column Names --------")
    ans = cur.fetchall()
    for x in range(len(ans)):
        print(x,'\t', "\"" +(ans[x])[1].replace("\n","\\n") +"\"")
    print("\n Example: python3 lookup_agenda 'Session Title' 'Morning Sessions'\n")
    # print(sys.argv)
    
elif len(sys.argv) == 3:
    colmn = "\"" + sys.argv[1].lstrip("*") + "\""
    data = sys.argv[-1].replace("'", "")
    conn = sqlite3.connect("interview_test.db")
    cur = conn.cursor()
    header = []
    cur.execute("PRAGMA table_info(users)")
    ans = cur.fetchall()
    for x in range(len(ans)):
        header.append("\"" +(ans[x])[1] +"\"")
    print("\nTable headers \t", tuple(header))
    if(colmn == "\"Speakers\""):
        data = "\"%" + data + "%\""
        cur.execute("SELECT DISTINCT * FROM users WHERE {} LIKE {} OR ParentID = (SELECT ID FROM users WHERE {} LIKE {}) ORDER BY ID;".format(colmn, data, colmn, data))
    else:
        data = "\"" + data + "\""
        cur.execute("SELECT DISTINCT * FROM users WHERE {} = {} OR ParentID = (SELECT ID FROM users WHERE {} = {}) ORDER BY ID;".format(colmn, data, colmn, data))
    rows = cur.fetchall()
    print("-----------Results----------")
    for x in range(len(rows)):
        print(x, "\t", rows[x])
        print("\n")
