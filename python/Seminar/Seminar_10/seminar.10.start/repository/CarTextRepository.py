from repository.Repository import *
from domain.Car import *
class CarTextRepository(Repository):
    '''
    A text-file backed repository for cars
    What do we want?
        1. Works the same as the Repository
            - your program can change between Repository and  CarTextRepository without changes to the source code
            => Modules are interchangeable and independent
            => this class has the same methods as Repository
        2. Load the cars from a text file when we build the repository
        3. Save all car changes to the text file
    '''
    def __init__(self, fileName):
        super().__init__()
        self._fileName = fileName
        # Load the car data from give file
        self._loadFile()

    '''
    This is a private method -> must not be called from outside class
    '''

    def _loadFile(self):
        '''
        1. Open self._fileName for text file reading
        2. For each file in input file
            a. Separate into tokens(by commas)
            b. Build the car object
            c. Store it in Repository
        3. Close input file
        '''
        f = open(self._fileName,'r')
        while True:
            s = f.readline().strip()
            if not s:
                break
            list = s.split(',')
            car = Car(*list)
            self.store(car)
        f.close()

    def store(self, object):
        '''
        1. Do the same thing as Repository.store
        2. Save the cars to file
        '''
        Repository.store(self, object) #this calls the in-memory store function
        '''
        2 options:
            #1 Repo.store worked, you have a new car stored => save it to file
            #2 RepositoryException in Repository.store => car will not be saved
        '''
        self._saveFile()

    '''
    Save the car into a file
    '''
    
    def _saveFile(self):
        pass

