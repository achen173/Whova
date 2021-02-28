import sqlite3

from db_table import db_table
schema = {'"Date"': 'text', '"Time Start"': 'text', '"Time End"': 'text', '"Session or \nSub-session(Sub)"': 'text', '"Session Title"': 'text', '"Room/Location"': 'text', '"Description"': 'text', '"Speakers"': 'text', '"ID"': 'text', '"ParentID"': 'text'}
database = db_table("users", schema)
for x in database.select():
    print(x, '\n')


