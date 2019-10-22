from domain import *
'''
Place functions which solve problem requirements
'''
def add_circle(circles, history, x, y, r):
    c = create_circle(x,y,r)
    history.append(circles[:]) #history[0], and circles are the same list
    circles.append(c) 
'''
Ways to implement undo
    1. keep a list of operations and their parameters and reverse them
        (efficent but complicated way)
    2. keep the history of program data in a list
'''
def undo(circles, history):
    #update circles with the last element of the history
    if len(history) == 0:
        raise ValueError("No more undos!")
    circles.clear()
    circles.extend(history.pop())
