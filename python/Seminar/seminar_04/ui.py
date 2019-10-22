'''
Menu-driven circles program !?
    - add circle (radius > 0, in the (+,+) first quadrant)
    - delete circles with radius < r
    - show circles
    - undo ?
    - exit
'''
'''
Everything that reads from/writes to the user (=console)
NB! Only module where input/print/ call functions that do that


function calls:
    ui -> functions
    ui -> domain 
    functions -> domain

'''
def add_circle_ui():
    pass

def show_circles_ui():
    pass

def printMenu():
    print("1. Add circle")
   #print("2. Delete circle")
    print("3. Show circles")
    print("0. Exit")

def start():
    circles = []
    # ~command design pattern
    commands = {'1':add_circle_ui, '3':show_circles_ui}
    
    
    while True:
        printMenu()
        cmd = input("command: ")
        if cmd == '0':
            return
        if cmd in commands.keys():
            commands[cmd]()
        else:
            print("Bad command!")

    

start()