#Game
import random 


class Game:
    
    def __init__(self):
        self._guesses = []
        self._done = 0
        self._bulls = 0
        self._cows = 0

    def _generateNumber(self):
        '''
        Generate a valid number
        '''
        ok = 0
        while ok == 0:
            n = random.randint(1022,9877)
            x = n
            ok = 1
            c = [] 
            while n != 0:
                c.append(n % 10)
                n //= 10
            for i in range(0,4):
                for j in range(i + 1,4):
                    if c[i] == c[j]:
                        ok = 0
                        break
        #print(x) - to check the generated number when you doesn't know how to win efficiently ;)
        return x
                   


    def newGame(self):
        self._done = 0
        self._guesses.clear()
        self._number = self._generateNumber()


    def test_input(self, no):
        try:
            no = int(no)
        except:
            raise ValueError("Invalid input! Try again!")
        leng = 0
        x = no
        while x != 0:
            x //= 10
            leng += 1
        if leng != 4:
            raise ValueError("Invalid input! Try again!")
        
        x = no
        c = []
        while x != 0:
            c.append(x % 10)
            x //= 10
        for i in range(0,4):
            for j in range(i + 1,4):
                if c[i] == c[j]:
                    raise ValueError("Invalid input! Try again!")

    def isRepeatedGuess(self, no):
        '''
        if yes => game lost
        '''
        for i in self._guesses:
            if i == no:
                self._done = 1
                raise ValueError("Repetead Guess! Game lost!")
        self._guesses.append(no)


    def guess(self, userGuess):
        '''
        compute cows and bulls
        '''
        self._bulls = self.compute_bulls(userGuess)
        self._cows = self.compute_cows(userGuess)
        if self._bulls == 4:
            self._done = 1
            raise ValueError("You won! Congrats!")
    
        

    def compute_bulls(self, usrguess):
        x = int(self._number)
        y = int(usrguess)
        bulls = 0
        while x != 0:
            if x % 10 == y % 10:
                bulls += 1
            x //= 10
            y //= 10
        return bulls

    def compute_cows(self, usrguess):
        x = int(self._number)
        y = int(usrguess)
        cows = 0
        c = []
        v = []

        while x != 0:
                c.append(x % 10)
                x //= 10
        x = y
        while x != 0:
                v.append(x % 10)
                x //= 10

        for i in range(0,4):
            for j in range(0,4):
                if c[i] == v[j] and i != j:
                    cows += 1
        return cows
