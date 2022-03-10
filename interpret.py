import table

_stack = []

def interpret(sql):
    cols = []
    tables = []
    comp = []
    while sql != []:
        if sql[0].normalized == 'SELECT':
            cols = sql[1]
            sql = sql[2:]
        elif sql[0].normalized == 'FROM':
            tables = sql[1]
            sql = sql[2:]
        elif sql[0].normalized[:5].upper() == 'WHERE':
            comp = list(filter(lambda x: not x.is_whitespace, sql[0].tokens[-1].tokens))
            sql = sql[1:]

    # projection formatting
    if cols.value == "*" or ',' not in cols.value: cols = [cols]
    cols = list(filter(lambda x: x != ' ' and x != ',', map(lambda x: x.value, cols)))
    
    # tables (excluding joins)
    tables = list(filter(lambda x: x != ' ' and x != ',', map(lambda x: x.value, tables)))
    
    # do cross products
    rel = table.getTable(tables[0])
    for t in range(1, len(tables)):
        rel = rel.cross(table.getTable(tables[t]))

    # return projection
    return rel.project(*cols)
