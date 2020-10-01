from domain import *
from functions import *
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
def add_circle_ui(circles, history):
    #additional validation for reading ints
    x = int(input("x= "))
    y = int(input("y= "))
    r = int(input("z= "))
    #surround with try...except
    add_circle(circles,history, x, y, r)


def show_circles_ui(circles, history):
    for c in circles:
        print(tostr(c))

def printMenu():
    print("1. Add circle")
   #print("2. Delete circle")
    print("3. Show circles")
    print("4. Undo")
    print("0. Exit")

def start():
    #circles
    #circles = []
    circles = test_init()
    history = []
    # ~command design pattern
    commands = {'1':add_circle_ui, '3':show_circles_ui, '4': undo}
    
    while True:
        printMenu()
        cmd = input("command: ")
        if cmd == '0':
            return
        if cmd in commands.keys():
            try:
              commands[cmd](circles,history)
            except ValueError as ve:
                #GUI
                #MessageBox.show(..., ve)
                print(ve)
        else:
            print("Bad command!")

    

start()