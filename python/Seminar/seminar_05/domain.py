'''
starry nights
stars have a location (x,y,z) distance at least 1ly between 2 stars,
weight (in solar masses, between [0,1,50]) and apparent magnitude (between [-1,15])
    1. Add a new star to the catalogue (generated some stars)
    2. Show all stars, sorted by any of the parameters
    3. Which starts are dangerous for earth? (weight > 10 Sm, AppMagnitude < 3 )
'''
class Location:
    '''
    x,y,z - integers
    '''
    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z
    pass

def test_location():
    alderaan = Location(1, 2, 3) # x,y,z

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
    pass