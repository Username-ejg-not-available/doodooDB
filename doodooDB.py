import interpret
import readline

leave = False
while not leave:
    ui = input('> ')
    if ui.upper() == "QUIT":
        leave = True
    else:
        while len(ui) > 0 and ui[-1] != ';':
            ui += input(': ')
        res = interpret.interpret(ui)
        if res != None:
            print(res)