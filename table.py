import doodooTypes
import console
import uuid
import parser.RelAlgeTree as RAT

tables = {}

class Cell:
    def __init__(self, data, coldef):
        self.data = data
        self.coldef = coldef

    def __repr__(self):
        return str(self.data)

class Column:
    def __init__(self, *name):
        self.nameList = list(name)

    def __add__(self, other):
        return self.nameList + other.nameList

    def __eq__(self, other):
        return self.nameList[-1] == other.nameList[-1]

    def __repr__(self):
        return self.getPartialName()

    def getName(self):
        return ".".join(self.nameList)   

    def getPartialName(self):
        return ".".join(self.nameList[1:])

class Schema:
    NULL = "NULL"
    NULLNT = "NULLNT"
    PRIMARY_KEY = "PRIMARY_KEY"
    INCREMENT = "INCREMENT"

    def __init__(self, schema):
        if not self.verify(schema): 
            raise Exception("Bad Schema!")
        self.pk = set({})
        for x in schema:
            if Schema.PRIMARY_KEY in schema[x]:
                self.pk.add(x)
            if Schema.NULL not in schema[x] and Schema.NULLNT not in schema[x]: 
                schema[x] += [Schema.NULLNT]
        self.schema = schema
        # Ex:
        # {
        #   "id": [int, Schema.PRIMARY_KEY, Schema.NULLNT],
        #   "name": [str]
        # }

    def verify(self, schema):
        return not (False in map(lambda x: doodooTypes.verifyType(schema[x][0]), schema))

class Table:
    def __init__(self, name, schema):
        self.name = name
        self.schema = Schema(schema)
        self.colnames = [ Column(name, x) for x in self.schema.schema ]
        self.columns = { x: [] for x in self.schema.schema }
        self.rows = []
        tables.update({ name: self })

    def insert(self, entry):
        for x in self.schema.schema:
            if (Schema.NULLNT in self.schema.schema[x] and Schema.INCREMENT not in self.schema.schema[x]) and x not in entry:
                raise Exception("Missing Column \'" + str(x) + "\': " + str(entry))

        for x in entry:
            if x not in self.schema.schema: raise Exception("Invalid column name: "+x)
            if not isinstance(entry[x], self.schema.schema[x][0]) and entry[x] != Schema.NULL: raise Exception("Bad type in column: "+x)

        if self.keyInTable(entry):
            raise Exception("Duplicate primary key: " + str(entry))
        
        for x in self.schema.schema:
            if x in self.schema.pk and Schema.INCREMENT in self.schema.schema[x]:
                if x in entry:
                    self.columns[x] += [Cell(entry[x], self.schema.schema[x])]
                elif self.columns[x] == []:
                    self.columns[x] += [doodooTypes.getStartVal(self.schema.schema[x][0])]
                else:
                    from functools import reduce
                    def red(y, z): 
                        if y == Schema.NULL and z == Schema.NULL: return 0
                        if y == Schema.NULL: return z
                        if z == Schema.NULL: return y
                        return max(y, z)
                    self.columns[x] += [reduce(red, self.columns[x]) + 1]
            else: 
                if x in entry: self.columns[x] += [entry[x]]
                else: self.columns[x] += [Schema.NULL]
        self.rows.append({ x: self.columns[x][len(self.columns[x]) - 1] for x in self.columns })

    def usedKeys(self):
        usedKeys = []
        for pk in self.schema.pk:
            if usedKeys == []: usedKeys = self.columns[pk]
            else: usedKeys = list(zip(self.columns[pk], usedKeys))
        return usedKeys

    def keyInTable(self, entry):
        theKey = []
        for key in self.schema.pk:
            if Schema.INCREMENT in self.schema.schema[key] and key not in entry: return False
            if theKey == []: theKey = entry[key]
            else: theKey = (entry[key], theKey)
        return theKey in self.usedKeys()

    def projection(self, *cols):
        # get schema in correct order
        schema = {}
        for x in cols:
            if x in self.schema.schema:
                schema[x] = self.schema.schema[x]
        res = Table(str(uuid.uuid4()), schema)
        # insert all the rows with only the correct columns
        for r in self.rows:
            res.insert(dict(filter(lambda x: x[0] in cols, r.items())))
        res.colnames = list(filter(lambda x: x.getPartialName() in schema, self.colnames))
        return res

    def selection(self, predicate):
        res = Table(str(uuid.uuid4()), self.schema.schema)
        for r in self.rows:
            if self._interpPred(r, predicate):
                res.insert(r)
        return res

    def _interpPred(self, row, pred) -> bool:
        if isinstance(pred, RAT.Boolean):
            return pred.val
        elif isinstance(pred, RAT.Identifier):
            return row[pred.id]
        elif isinstance(pred, RAT.Number):
            return pred.num
        elif isinstance(pred, RAT.Unary):
            if pred.operator == '-':
                return -self._interpPred(row, pred.exp)
            elif pred.operator == '+':
                return abs(self._interpPred(row, pred.exp))
            elif pred.operator == 'NOT':
                return not self._interpPred(row, pred.exp)
        elif isinstance(pred, RAT.Binary):
            if pred.operator == '+':
                return float(self._interpPred(row, pred.left)) + float(self._interpPred(row, pred.right))
            elif pred.operator == '-':
                return float(self._interpPred(row, pred.left)) - float(self._interpPred(row, pred.right))
            elif pred.operator == '*':
                return float(self._interpPred(row, pred.left)) * float(self._interpPred(row, pred.right))
            elif pred.operator == '/':
                return float(self._interpPred(row, pred.left)) / float(self._interpPred(row, pred.right))
            elif pred.operator == '>=':
                return float(self._interpPred(row, pred.left)) >= float(self._interpPred(row, pred.right))
            elif pred.operator == '<':
                return float(self._interpPred(row, pred.left)) < float(self._interpPred(row, pred.right))
            elif pred.operator == '>':
                return float(self._interpPred(row, pred.left)) > float(self._interpPred(row, pred.right))
            elif pred.operator == '<=':
                return float(self._interpPred(row, pred.left)) <= float(self._interpPred(row, pred.right))
            elif pred.operator == '=':
                return float(self._interpPred(row, pred.left)) == float(self._interpPred(row, pred.right))
            elif pred.operator == '<>':
                return float(self._interpPred(row, pred.left)) != float(self._interpPred(row, pred.right))
            elif pred.operator == '**':
                return float(self._interpPred(row, pred.left)) ** float(self._interpPred(row, pred.right))
            elif pred.operator == 'AND':
                return bool(self._interpPred(row, pred.left)) and bool(self._interpPred(row, pred.right))
            elif pred.operator == 'OR':
                return bool(self._interpPred(row, pred.left)) or bool(self._interpPred(row, pred.right))

    def cross(self, other):
        sch = {}
        cnames = []
        resname = str(uuid.uuid4())
        for col in self.colnames:
            if col in other.colnames:
                cnames.append(Column(resname, self.name, col.nameList[-1]))
                sch[self.name + "." + col.nameList[-1]] = self.schema.schema[col.nameList[-1]]
            else:
                cnames.append(Column(resname, col.nameList[-1]))
                sch[col.nameList[-1]] = self.schema.schema[col.nameList[-1]]
        for col in other.colnames:
            if col in self.colnames:
                cnames.append(Column(resname, other.name, col.nameList[-1]))
                sch[other.name + "." + col.nameList[-1]] = other.schema.schema[col.nameList[-1]]
            else:
                cnames.append(Column(resname, col.nameList[-1]))
                sch[col.nameList[-1]] = other.schema.schema[col.nameList[-1]]
        res = Table(resname, sch)
        res.colnames = cnames

        entries = [list(l.values()) + list(r.values()) for l in self.rows for r in other.rows]
        entries = [dict(zip(map(lambda x: x.getPartialName(), cnames), e)) for e in entries]
        for e in entries: res.insert(e)
        return res

    def __repr__(self):
        c = console.Console()
        out, _ = c.grid([[x for x in self.columns], *list(map(lambda x: list(x.values()), self.rows))], True)
        return self.name + "\n" + out
