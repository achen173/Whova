from db_table import db_table
users = db_table("users", { "id": "integer PRIMARY KEY", "name": "text", "email": "text NOT NULL UNIQUE" })
users.insert({"name": "S", "email": "simon.ninon@whova.com"})
users.insert({"name": "S", "email": "xinxin.jin@whova.com"})
users.insert({"name": "Congming Chen", "email": "congming.chen@whova.com"})
# users.update({'name': 'John'}, {'id':2})
print(users.select(where={ "name": "S" }))
# print(users.select(['name', 'email'], {'id':2}))
# print(users.select(["name"], { "id": 2 }))
users.close()

    # Example table.select(["name"], { "id": "42" })
    #         table.select()
    #         table.select(where={ "name": "John" })