# pip install xlrd
import xlrd
from db_table import db_table
import sys
class create_db:

    def __init__(self, filename):
        loc = (filename)
        wb = xlrd.open_workbook(loc)
        self.sheet = wb.sheet_by_index(0)
        self.sheet_rows = wb.sheet_by_index(0).nrows
        self.headers = self.sheet.row_values(0) + ["ID", "ParentID"]
        self.mytable = ""

    def add_all_rows(self):
        result = []
        uniqueID = 0
        parentID = 0
        i = 1
        while i < self.sheet_rows:
            parent = False
            row = self.sheet.row_values(i)
            row.append(str(uniqueID))
            if i + 1 < self.sheet_rows and self.sheet.row_values(i+1)[3] == 'Sub':
                parent = True
            if not parent:
                row.append('')
                result.append(row)
                uniqueID += 1
                i += 1
            else:
                row.append(str(parentID))
                result.append(row)
                uniqueID += 1
                x = i+1
                while x < self.sheet_rows and self.sheet.row_values(x)[3] == 'Sub':
                    row = self.sheet.row_values(x)
                    row.append(str(uniqueID))
                    row.append(str(parentID))
                    result.append(row)
                    uniqueID += 1
                    x += 1
                i = x
                parentID += 1

    def add_header(self):
        temp = dict()
        for x in self.headers:
            if x[0] == '*':
                temp["\"" + x[1:] + "\""] = "text"
            else:
                temp["\"" + x + "\""] = "text"
        self.mytable = db_table("users", temp)

database = create_db(sys.argv[-1])
database.add_header()
database.add_all_rows()

