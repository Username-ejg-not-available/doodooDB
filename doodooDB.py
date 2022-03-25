from table import *
import interpret
import parser.sqlparser as p

leave = False
while not leave:
    
    ui = input('> ')
    if ui.upper() == "QUIT":
        leave = True
    else:
        print(p.p.Parser(ui).parse())
