'''
1. Add a new star to the catalogue (generated some stars)
2. Show all stars, sorted by any of the parameters
3. Which starts are dangerous for earth? (weight > 10 Sm, AppMagnitude <3
'''


class Service:
    def _init(self):
        self._stars = []

    def addStar(self, star):
        '''
        Add the new start to the catalogue
        params:
            star - ...
        Raise ValueError if new star too close to existing ones
        '''
        pass

    def sortStars(self, cmp):
        '''
        Sort stars by given parameter
        params:
            cmp - Reference to a comparator function
        Return the sorted list of stars
        '''
        pass


    def dangerousStar(self):
        '''
        Return list of dangerous stars
        params:
            mass, mag
        '''