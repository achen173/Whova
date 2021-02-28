import sqlite3
import sys
from db_table import db_table


conn = sqlite3.connect("interview_test.db")
cur = conn.cursor()

mykey = ['date', 'time_start', 'time_end', 'title', 'location', 'description', 'speaker']
myvalue = ['Date','Time Start','Time End','Session Title','Room/Location','Description','Speakers']
lookup_table = {x:"\""+y+"\"" for x,y in zip(mykey, myvalue)}
if len(sys.argv) == 2 and sys.argv[1] == '--help':
    print("------- List of Column Names --------")
    for x in range(len(mykey)):
        print(x,'\t', mykey[x])
    print("\n Make sure to wrap the lookup value in single quote\n Example: python3 lookup_agenda.py time_start '08:45 AM'\n")
    
elif len(sys.argv) == 3:
    if sys.argv[1] in mykey:
        colmn = lookup_table[sys.argv[1]]
        data = sys.argv[-1].replace("'", "")    # get rid of apostrophes
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
    else:
        print("Invalid Command")
