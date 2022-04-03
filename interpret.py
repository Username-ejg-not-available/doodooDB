from copy import deepcopy
import table
from parser.sqlparser import p, RAT

def interpret(sql):
    tree = p.Parser(sql).parse()
    return walk(tree)

def walk(tree: RAT.SQL) -> table.Table:
    if isinstance(tree, RAT.Drop):
        del table.tables[tree.table.id]
    elif isinstance(tree, RAT.Truncate):
        t = table.tables[tree.table.id]
        t.rows = []
        t.columns = { x: [] for x in t.schema.schema }
    elif isinstance(tree, RAT.Create):
        table.tables[tree.name.id] = table.Table(tree.name.id, tree.schema)
    elif isinstance(tree, RAT.Alter):
        if tree.add:
            table.tables[tree.table.id].schema = table.Schema({
                **table.tables[tree.table.id].schema.schema, 
                **tree.thing
            })
            table.tables[tree.table.id].colnames.append(table.Column(tree.table.id, list(tree.thing.keys())[0]))
            table.tables[tree.table.id].columns.update({ 
                list(tree.thing.keys())[0]: [table.Cell(table.Schema.NULL, list(tree.thing.values())[0]) for _ in table.tables[tree.table.id].rows] 
            })
            for r in range(len(table.tables[tree.table.id].rows)):
                table.tables[tree.table.id].rows[r].update({ 
                    list(tree.thing.keys())[0]: table.tables[tree.table.id].columns[list(tree.thing.keys())[0]][r]
                })
        else:
            if tree.thing.id in table.tables[tree.table.id].schema.pk:
                table.tables[tree.table.id].schema.pk.remove(tree.thing.id)
            if tree.thing.id in table.tables[tree.table.id].schema.schema:
                del table.tables[tree.table.id].schema.schema[tree.thing.id]
            if tree.thing.id in table.tables[tree.table.id].columns:
                del table.tables[tree.table.id].columns[tree.thing.id]
            for c in range(len(table.tables[tree.table.id].colnames)):
                if table.tables[tree.table.id].colnames[c].getPartialName() == tree.thing.id:
                    table.tables[tree.table.id].colnames = table.tables[tree.table.id].colnames[:c] + table.tables[tree.table.id].colnames[c + 1:]
                    break
            for r in range(len(table.tables[tree.table.id].rows)):
                del table.tables[tree.table.id].rows[r][tree.thing.id]
    elif isinstance(tree, RAT.Insert):
        table.tables[tree.table.id].insert(tree.entry)
    elif isinstance(tree, RAT.Projection):
        return walk(tree.subtree).projection(*map(lambda t: t.id, tree.columns))
    elif isinstance(tree, RAT.Selection):
        return walk(tree.subtree).selection(tree.predicate)
    elif isinstance(tree, RAT.Rename):
        t = deepcopy(walk(tree.table))
        for c in range(len(table.tables[t.name].colnames)):
            table.tables[t.name].colnames[c].nameList[0] = tree.name
        t.name = tree.name
        return t
    elif isinstance(tree, RAT.InnerJoin):
        return walk(tree.leftSubtree).cross(walk(tree.rightSubtree)).selection(tree.predicate)
    elif isinstance(tree, RAT.NatJoin):
        predicate = True
        return walk(tree.leftSubtree).cross(walk(tree.rightSubtree)).selection(predicate)
    elif isinstance(tree, RAT.Identifier):
        return table.tables[tree.id]
    elif isinstance(tree, list):
        t = table.tables[tree[0].id]
        for x in tree[1:]:
            t = t.cross(table.tables[x.id])
        return t