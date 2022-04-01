from table import *
import interpret

leave = False
while not leave:
    
    ui = input('> ')
    if ui.upper() == "QUIT":
        leave = True
    else:
        print(interpret.interpret(ui))
