class UndoController:
    def __init__(self):
        # History of program operations (the undo-able ones)
        self._history = []

    def undo(self):
        pass

    def redo(self):
        pass



#remember which function to call and using which parameters
#Implementation of the command design pattern
class FunctionCall:
    def __init__(self, function, *parameters):
        self._function = function
        self._params = parameters

    #() -> function call operator
    def call(self):
        self._function(*self._params)

# undo/redo are the sides of the same coin

class Operation:
    '''
    Encodes an operation that happened in the program
    '''
    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction

    def undo(self):
        self._undo.call()

    def redo(self):
        self._redo.call()





'''
How do we implement undo/redo?
    1. Remember what we need to do for undo/redo
    (remember = what function to call and with which parameters)
    
    2.  Remember the order operations were made
    (remember = keep a list of program operations)
    
    3. Carry out the operations when user requests undo(), redo()
    (call the right function with the right parameters)
    
    
    

'''