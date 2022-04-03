
class SQL:
    def __init__(self): pass

class Drop(SQL):
    def __init__(self, table):
        self.table = table

    def __repr__(self):
        return "Drop(" + str(self.table) + ")"

class Truncate(SQL):
    def __init__(self, table):
        self.table = table

    def __repr__(self):
        return "Truncate(" + str(self.table) + ")"

class Create(SQL):
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema

    def __repr__(self):
        return "Create(" + str(self.table) + ", " + str(self.schema) + ")"

class Alter(SQL):
    def __init__(self, table, add: bool, thing):
        self.table = table
        self.add = add
        self.thing = thing

    def __repr__(self):
        return "Alter(" + str(self.table) + ", ADD:" + str(self.add) + ", " + str(self.thing) + ")"
        
class Insert(SQL):
    def __init__(self, table, entry):
        self.table = table
        self.entry = entry

    def __repr__(self):
        return "Insert(" + str(self.table) + ", " + str(self.entry) + ")"

class Projection(SQL):
    def __init__(self, cols, tree: SQL, distinct: bool):
        self.columns = cols
        self.subtree = tree
        self.distinct = distinct

    def __repr__(self):
        return "PROJECT(" + ','.join(map(lambda x: str(x), self.columns)) + " FROM " + str(self.subtree) + ")"

class Selection(SQL):
    def __init__(self, tree: SQL, predicate: SQL):
        self.subtree = tree
        self.predicate = predicate
    
    def __repr__(self):
        return "SELECT(" + str(self.subtree) + " WHERE " + str(self.predicate) + ")"

class NatJoin(SQL):
    def __init__(self, left, right):
        self.leftSubtree = left
        self.rightSubtree = right

    def __repr__(self):
        return "NATJOIN(" + str(self.leftSubtree) + ", " + str(self.rightSubtree) + ")"

class InnerJoin(SQL):
    def __init__(self, left, right, predicate):
        self.leftSubtree = left
        self.rightSubtree = right
        self.predicate = predicate

    def __repr__(self):
        return "INNERJOIN(" + str(self.leftSubtree) + ", " + str(self.rightSubtree) + ", " + str(self.predicate) + ")"

class Rename(SQL):
    def __init__(self, table, name):
        self.table = table
        self.name = name

    def __repr__(self):
        return "RENAME(" + str(self.table) + ", " + str(self.name) + ")"

class Predicate:
    def __init__(self) -> None:
        pass

class Binary(Predicate):
    def __init__(self, left, right, operator) -> None:
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self):
        return "(" + str(self.left) + self.operator + str(self.right) + ")"

class Unary(Predicate):
    def __init__(self, exp, operator) -> None:
        self.exp = exp
        self.operator = operator

    def __repr__(self):
        return "(" + self.operator + str(self.exp) + ")"

class Identifier(Predicate):
    def __init__(self, id) -> None:
        self.id = id

    def __repr__(self):
        return str(self.id)