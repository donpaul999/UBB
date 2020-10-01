from TextRepo import *


class UI:
    def __init__(self, Service):
        self._service = Service

    def inputComm(self):
        command = input()
        command = command.split(' ')
        try:
            if command[0] == "undo":
                self._service.undo()
            elif command[0] == "swap":
                if len(command) != 5:
                    raise ValueError("Bad parameters!")
                self._service.swap(command[1], command[2], command[3], command[4])
            else:
                raise ValueError("Bad command!")
        except ValueError as e:
            print(e)

    def isOk(self, obj):
        if self._service.score(obj) > 0:
            return True
        return False

    def verify(self, obj):
        return self._service.verify(obj)

    def WonOrLose(self, obj):
        return self.isOk(obj)

    def selectS(self):
        return self._service.selectS()

    def start(self):
        string = self._service.selectS()
        self._service.calcScore(string)
        self._service.shuffle(string)
        print(string)
        while True and self.isOk(string) and self._verify(string) == False:
            print("**********")
            print(string)
            self._inputComm()
            print("**********")

        if self.WonOrLose(string) == False:
            print("You Won! :)")
        else:
            print("You lose! :(")