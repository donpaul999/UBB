#UI
from game import Game

class UI:
    def __init__(self, game):
        self._game = game



    def print_start_menu(self):
        print("****************")
        print("Welcome to the Bulls and Cows!")
        print("****************")
        print("Choose an option from below:")
        print("1. New game!")
        print("2. Exit")

    def print_invalid(self):
        print("Invalid command!")

    def start_game(self):
        self._game.newGame()
        self._game._done = 0
        self._game._guesses.clear()
        while self._game._done == 0:
            number = input("Write a guess: ")
            try: 
                self._game.test_input(number)
                try:
                    self._game.isRepeatedGuess(number)
                except ValueError as e:
                    print(" ")
                    print(e)
                    print(" ")
                    return
                try:
                    self._game.guess(number)
                except ValueError as e:
                    print(" ")
                    print(e)
                    print(" ")
                print("Bulls: " + str(self._game._bulls) + " Cows: " + str(self._game._cows))
            except ValueError as e:
                print(e)
           
    


    def start(self):
        '''
        1. Print the menu:
            - Start new game
                - read user guess
                - self._game determines if repeated guess => game lost
                - self._game determines #bulls and #cows returned to the UI
            - Exit
        2. Once the game is over, print
        '''
        while True:
            self.print_start_menu()
            choice = input("> ")
            if choice == '1':
                self.start_game()
            elif choice == '2':
                return
            else:
                self.print_invalid()