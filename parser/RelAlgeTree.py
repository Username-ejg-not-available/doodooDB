
class Algebra:
    def __init__(self):
        pass

class Projection(Algebra):
    def __init__(self, cols, tree: Algebra):
        self.columns = cols
        self.subtree = tree

    def __repr__(self):
        return "PROJECT(" + ','.join(self.columns) + " FROM " + str(self.subtree) + ")"

class Selection(Algebra):
    def __init__(self, tree: Algebra, predicate: Algebra):
        self.subtree = tree
        self.predicate = predicate
    
    def __repr__(self):
        return "SELECT(" + str(self.subtree) + " WHERE " + str(self.predicate) + ")"

class CrossProduct(Algebra):
    def __init__(self, left: Algebra, right: Algebra):
        self.leftSubtree = left
        self.rightSubtree = right

    def __repr__(self):
        return "CROSS(" + str(self.leftSubtree) + ", " + str(self.rightSubtree) + ")"

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

class Number(Predicate):
    def __init__(self, num) -> None:
        self.num = num

class Boolean(Predicate):
    def __init__(self, val) -> None:
        self.val = val