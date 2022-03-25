
class Algebra:
    def __init__(self):
        pass

class Projection(Algebra):
    def __init__(self, cols, tree: Algebra):
        self.columns = cols
        self.subtree = tree

    def __repr__(self):
        return "SELECT " + ','.join(self.columns) + " FROM " + str(self.subtree)

class Selection(Algebra):
    def __init__(self, tree: Algebra, predicate: Algebra):
        self.predicate = predicate
        self.subtree = tree

class CrossProduct(Algebra):
    def __init__(self, left: Algebra, right: Algebra):
        self.leftSubtree = left
        self.rightSubtree = right