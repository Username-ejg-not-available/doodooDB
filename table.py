from datetime import datetime
import doodooTypes
import console

columns = {}

def getCol(*name):
    strname = ".".join(list(name))
    if strname not in columns: columns[strname] = Column(*name)
    return columns[strname]

class Column:
    def __init__(self, *name):
        self.nameList = list(name)
        if self.getName() not in columns: 
            columns[self.getName()] = self

    def __add__(self, other):
        return getCol(self.nameList + other.nameList)

    def __repr__(self):
        return self.getName()

    def getName(self):
        return ".".join(self.nameList)   

class Pred:
    def __init__(self):
        pass

# map from name to type
class Schema:
    NULL = "NULL"
    NULLNT = "NULLNT"
    PRIMARY_KEY = "PRIMARY_KEY"
    INCREMENT = "INCREMENT"

    def __init__(self, schema):
        if not self.verify(schema): 
            raise Exception("Bad Schema!")
        self.pk = []
        for x in schema:
            if Schema.PRIMARY_KEY in schema[x]:
                self.pk += [getCol(x)]
            if Schema.NULL not in schema[x] and Schema.NULLNT not in schema[x]: 
                schema[x] += [Schema.NULLNT]
        self.schema = dict(zip(map(lambda x: getCol(x), schema.keys()), schema.values()))
        # Ex:
        # {
        #   "id": [int, Schema.PRIMARY_KEY, Schema.NULLNT],
        #   "name": [str]
        # }

    def verify(self, schema):
        return not (False in map(lambda x: doodooTypes.verifyType(schema[x][0]), schema))

class Table:
    def __init__(self,name: str, schema: Schema):
        self.name = name
        self.schema = schema
        self.table = { x: [] for x in self.schema.schema }

    # Using map entry
    def insert(self,entry):
        if len(entry) > len(self.schema.schema): 
            raise Exception("Invalid entry: "+str(entry))
        for x in self.schema.schema:
            if (Schema.NULLNT in self.schema.schema[x] and Schema.INCREMENT not in self.schema.schema[x]) and x.getName() not in entry:
                raise Exception("Missing Column \'" + str(x) + "\': "+str(entry))

        if self.keyInTable(entry):
            raise Exception("Duplicate primary key: " + str(entry))

        for x in entry:
            if getCol(x) not in self.schema.schema: raise Exception("Invalid column name: "+x)
            if not isinstance(entry[x], self.schema.schema[getCol(x)][0]): raise Exception("Bad type in column: "+x)

        for x in self.schema.schema:
            if x in self.schema.pk and Schema.INCREMENT in self.schema.schema[x]:
                if x.getName() in entry:
                    self.table[x] += [entry[x.getName()]]
                elif self.table[x] == []:
                    self.table[x] += [doodooTypes.getStartVal(self.schema.schema[x][0])]
                else:
                    from functools import reduce
                    def red(y, z): 
                        if y == Schema.NULL or z == Schema.NULL: return 0
                        return max(y, z)
                    self.table[x] += [reduce(red, self.table[x]) + 1]
            else: 
                if x.getName() in entry: self.table[x] += [entry[x.getName()]]
                else: self.table[x] += [Schema.NULL]

    def getRelation(self, predicate, *colNames: str):
        sch = {}
        for x in colNames:
            if getCol(x) not in self.schema.schema:
                raise Exception("Bad projection!")
            sch[x] = self.schema.schema[getCol(x)]
        rel = Table("_" + self.name, Schema(sch))
        for x in sch:
            rel.table[getCol(x)] = self.table[getCol(x)]
        return rel

    def asRows(self):
        return list(map(lambda x: list(x), zip(*self.table.values())))

    def usedKeys(self):
        usedKeys = []
        for pk in self.schema.pk:
            if usedKeys == []: usedKeys = self.table[pk]
            else: usedKeys = list(zip(self.table[pk], usedKeys))
        return usedKeys

    def keyInTable(self,entry):
        theKey = []
        for key in self.schema.pk:
            if Schema.INCREMENT in self.schema.schema[key]: return False
            if theKey == []: theKey == entry[key]
            else: theKey = list(zip(entry[key], theKey))

        return theKey in self.usedKeys()

    def cross(self, other):
        sch = {}
        for name in self.schema.schema:
            if name in other.schema.schema:
                sch[getCol(self.name, *name.nameList).getName()] = self.schema.schema[name]
            else:
                sch[name.getName()] = self.schema.schema[name]
        for name in other.schema.schema:
            if name in self.schema.schema:
                sch[getCol(other.name, *name.nameList).getName()] = other.schema.schema[name]
            else:
                sch[name.getName()] = other.schema.schema[name]
        rel = Table("_" + self.name, Schema(sch))
        entries = [lentry + rentry for lentry in self.asRows() for rentry in other.asRows()]
        entries = list(map(lambda row: dict(zip(sch.keys(), row)), entries))
        for e in entries: rel.insert(e)

        return rel

    def printTable(self):
        c = console.Console()
        t = [[x for x in self.table]] + list(zip(*list(self.table.values())))
        c.grid(t, True)
