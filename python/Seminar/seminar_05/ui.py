from service import Service

class UI:
    #Can the UI do jobs without a Service?
    #NO => it doesn't make sense to create UI without having a Service

    def __init__(self, service):
        self._service = service



    def addStar(self):
        #read star location, mass, magnitude
        #check star is valid
        #call service.Star(newStar)
        newStar = None
        self._service.Star(newStar)
    def sortStars(self):
        pass

    def start(self):
        print('Welcome to the star catalogue!')
        self.addStar()
        # Print menu, read user choice, etc
        # call addStart and sortStars methods
s = Service()
ui = UI(s)
ui.start()
