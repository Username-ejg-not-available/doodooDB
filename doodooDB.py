import sqlparse
from table import *

# leave = False
# while not leave:
    
#     ui = input('> ')
#     if ui.upper() == "QUIT":
#         leave = True
#     else:
#         sql = list(filter(lambda x: not x.is_whitespace, sqlparse.parse(ui)[0]))
#         print(sql)


testschema = {
    "id":   [int, Schema.PRIMARY_KEY, Schema.INCREMENT], 
    "name": [str],
    "birth": [datetime],
}

testschema2 = {
    "id": [int, Schema.PRIMARY_KEY, Schema.INCREMENT],
    "name": [str],
    "death": [datetime],
    "pillowsOwned": [int]
}

t = Table("Student",Schema(testschema))
t.insert({"name":"Joe", "birth":datetime(2000, 4, 1, 1, 2, 3)})
t.insert({"name":"Garrett", "birth":datetime(2000, 6, 9, 1, 2, 3)})

t2 = Table("Weeb",Schema(testschema2))
t2.insert({"name":"Sandy", "death":datetime(2003,2,3,4,5,6), "pillowsOwned":5})
t2.insert({"name":"James", "death":datetime(2000,2,3,9,5,6), "pillowsOwned":2})
t2.insert({"name":"Joe", "death":datetime(2009,2,3,4,5,6), "pillowsOwned":69})
t2.printTable()

t3 = t.cross(t2)
t3.printTable()

t4 = t3.getRelation(True, "Student.id", "Weeb.id", "Weeb.name", "pillowsOwned")
t4.printTable()