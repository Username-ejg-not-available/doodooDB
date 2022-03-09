from datetime import datetime

class enum:
    def __init__(self, *args: str):
        self.values = set(args)

_types = [
    str,
    bool,
    int,
    float,
    datetime,
]

def verifyType(var):
    if isinstance(var, enum) or var in _types: return True
    return False

def getStartVal(t):
    if t == int: return 0
    raise Exception("Bad type in getStartVal: " + str(t))