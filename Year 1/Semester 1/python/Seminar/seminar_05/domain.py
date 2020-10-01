'''
starry nights
stars have a location (x,y,z) distance at least 1ly between 2 stars,
weight (in solar masses, between [0,1,50]) and apparent magnitude (between [-1,15])
    1. Add a new star to the catalogue (generated some stars)
    2. Show all stars, sorted by any of the parameters
    3. Which starts are dangerous for earth? (weight > 10 Sm, AppMagnitude < 3 )
'''
import math

class Location:
    '''
    x,y,z - integers
    '''
    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z

    # properties without setter are called read-only

    @property
    def X(self):
        return self._x
    @property
    def Y(self):
        return self._y
    @property
    def Z(self):
        return self._z
    @X.setter
    def X(self, value):
        self._x = value
    @Y.setter
    def Y(self, value):
        self._y = value
    @Z.setter
    def Z(self, value):
        self._z = value

    # self - location
    def __sub__(self, loc):
        return sqrt((self.X - loc.X) ** 2 + (self.Y - loc.Y) ** 2 + (self.Z - loc.Z) ** 2)

    def __str__(self):
        return '('  + str(self.X) + ", " + str(self.Y) + ", " + str(self.Z) + ")"



def test_location():
    alderaan = Location(1, 2, 3) # Function call operator
    assert alderaan.X == 1 and alderaan.Y  == 2 and alderaan.Z == 3
    alderaan.X = 10
    assert alderaan.X == 10
    alderaan.Y += 5
    assert alderaan.Y == 7

    '''
    alderaan.get_x()

    # allows me to validate star's position
    alderaan.set_x() # you run code, so you can validate
    alderaan.set_x(alderaan.get_x() + 50) # ok, but ugly
    #Python properties to the resq!
    alderaan.X += 50 # cide runsm so you can validate, and looks reasonable

    #alderaan._x = 5 # no code runs, so no validations possiblw
    '''


test_location()

class Star:
    '''
    location, mass, magnitude
    '''
    def __init__(self, loc, mass, mag):
        self.Location = loc
        self.Mass = mass
        self.Magnitude = mag

    @property
    def Location(self):
        return self._loc

    @Location.setter
    def Location(self, value):
        self._loc = value

    @property
    def Mass(self):
        return self._mass

    @Mass.setter
    def Mass(self, value):
        if value < 0.1 or value > 50:
            raise ValueError("Star mass must be in [0.1, 50]")
        self._mass = value

    @property
    def Magnitude(self):
        return self._mag

    @Magnitude.setter
    def Magnitude(self, value):
        if value < -1 or value > 15:
            raise ValueError("Star magnitude must be in [-1, 50]")
        self._mag = value
