import table
from parser.sqlparser import p, RAT

def interpret(sql):
    tree = p.Parser(sql).parse()
    return walk(tree)

def walk(tree: RAT.Algebra) -> table.Table:
    if isinstance(tree, RAT.CrossProduct):
        left, right = None, None
        if isinstance(tree.leftSubtree, RAT.Identifier):
            left = table.tables[tree.leftSubtree.id]
        else:
            left = walk(tree.leftSubtree)
        if isinstance(tree.rightSubtree, RAT.Identifier):
            right = table.tables[tree.rightSubtree.id]
        else:
            right = walk(tree.rightSubtree)
        return left.cross(right)
    elif isinstance(tree, RAT.Projection):
        return walk(tree.subtree).projection(*tree.columns)
    elif isinstance(tree, RAT.Selection):
        return walk(tree.subtree).selection(tree.predicate)
    elif isinstance(tree, RAT.Identifier):
        return table.tables[tree.id]
    elif isinstance(tree, list):
        return table.tables[tree[0]]