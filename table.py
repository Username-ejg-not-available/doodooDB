from datetime import datetime
import doodooTypes
import console

tables = {}

def getTable(name: str):
    if name not in tables: raise Exception("Table " + name + " does not exist")
    return tables[name]

class Column:
    def __init__(self, *name):
        self.nameList = list(name)

    def __add__(self, other):
        return self.nameList + other.nameList

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __key(self):
        return tuple(map(lambda x: ord(x), list(self.getName())))

    def __hash__(self):
        return hash(self.__key())

    def __repr__(self):
        return self.getPartialName()

    def getName(self):
        return ".".join(self.nameList)   

    def getPartialName(self):
        return ".".join(self.nameList[1:])

class Pred:
    def __init__(self, tokens):
        # assume the where token has already been removed and whitespace has been filtered
        self.tokens = tokens

# map from name to type
class Schema:
    NULL = "NULL"
    NULLNT = "NULLNT"
    PRIMARY_KEY = "PRIMARY_KEY"
    INCREMENT = "INCREMENT"

    def __init__(self, tableName, schema):
        if not self.verify(schema): 
            raise Exception("Bad Schema!")
        self.pk = set({})
        for x in schema:
            if Schema.PRIMARY_KEY in schema[x]:
                self.pk.add(Column(tableName, x))
            if Schema.NULL not in schema[x] and Schema.NULLNT not in schema[x]: 
                schema[x] += [Schema.NULLNT]
        self.schema = dict(zip(map(lambda x: Column(tableName, x), schema.keys()), schema.values()))
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
        tables[name] = self

    # Using map entry
    def insert(self,entry):
        if len(entry) > len(self.schema.schema): 
            raise Exception("Invalid entry: "+str(entry))
        for x in self.schema.schema:
            if (Schema.NULLNT in self.schema.schema[x] and Schema.INCREMENT not in self.schema.schema[x]) and x.getPartialName() not in entry:
                raise Exception("Missing Column \'" + str(x) + "\': "+str(entry))

        if self.keyInTable(entry):
            raise Exception("Duplicate primary key: " + str(entry))

        for x in entry:
            if Column(self.name, x) not in self.schema.schema: raise Exception("Invalid column name: "+x)
            if not isinstance(entry[x], self.schema.schema[Column(self.name, x)][0]): raise Exception("Bad type in column: "+x)

        for x in self.schema.schema:
            if x in self.schema.pk and Schema.INCREMENT in self.schema.schema[x]:
                if x.getPartialName() in entry:
                    self.table[x] += [entry[x.getPartialName()]]
                elif self.table[x] == []:
                    self.table[x] += [doodooTypes.getStartVal(self.schema.schema[x][0])]
                else:
                    from functools import reduce
                    def red(y, z): 
                        if y == Schema.NULL or z == Schema.NULL: return 0
                        return max(y, z)
                    self.table[x] += [reduce(red, self.table[x]) + 1]
            else: 
                if x.getPartialName() in entry: self.table[x] += [entry[x.getPartialName()]]
                else: self.table[x] += [Schema.NULL]

    def project(self, *colNames: str):
        if colNames[0] == "*": return self
        sch = {}
        for x in colNames:
            if Column(self.name, x) not in self.schema.schema:
                raise Exception("Bad projection!")
            sch[x] = self.schema.schema[Column(self.name, x)]
        rel = Table("_" + self.name, Schema("_" + self.name, sch))
        for x in sch:
            rel.table[Column("_" + self.name, x)] = self.table[Column(self.name, x)]
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
                sch[Column(self.name, *name.nameList).getName()] = self.schema.schema[name]
            else:
                sch[name.getName()] = self.schema.schema[name]
        for name in other.schema.schema:
            if name in self.schema.schema:
                sch[Column(other.name, *name.nameList).getName()] = other.schema.schema[name]
            else:
                sch[name.getName()] = other.schema.schema[name]
        rel = Table("_" + self.name, Schema("_" + self.name, sch))
        entries = [lentry + rentry for lentry in self.asRows() for rentry in other.asRows()]
        entries = list(map(lambda row: dict(zip(sch.keys(), row)), entries))
        for e in entries: rel.insert(e)

        return rel

    def printTable(self):
        c = console.Console()
        t = [[x for x in self.table]] + list(zip(*list(self.table.values())))
        c.grid(t, True)
