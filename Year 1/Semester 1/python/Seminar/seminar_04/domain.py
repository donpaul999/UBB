'''
Here your code everything about the domain
domain = circles, Q, Z, expenses, transactions, contest result, etc.
'''

#c = [0,0,1] unit circle  NOT valid in our program

def create_circle(x,y,r):
    '''
    Creates a circle centered in (x,y) with radius r
    params:
        x,y,r - ints, where x,y,r > 0 and circle in (+,+)
    Returns the circle
    Raises ValueError if circle is invalid
    '''
    if r <= 0:
        raise ValueError("Radius < 0!")
    if x < r or y < r:
        raise ValueError("Circle not in 1st quadrant!")
    

    return [x,y,r]
 

def get_x(c):
    return c[0]
def get_y(c):
    return c[1]
def get_r(c):
    return c[2]

#We can't print stuff here, so we convert to a string
#starts to look similar to python's own str() function      
def tostr(c):
    return(print("("+str(get_x(c)) + "," + str(get_y(c)) + "), r= " + str(get_r(c))))

def test_tostr():
    c = create_circle(2,2,1)
   # assert tostr(c) = '(2,2), r= 1'

#1. Write function specification
#2. Write a test function
#3. Run test function => it must fail
#4. Write function code 
#5. Run test function => it should pass (repeat 3-5)
#6. Optimize!
def test_init():
    circles = []
    circles.append(create_circle(1,1,1))
    circles.append(create_circle(2,1,1))
    circles.append(create_circle(3,1,1))
    circles.append(create_circle(1,1,1))
    return circles

def test_create_circle():
    #nice circle
    c = create_circle(1,1,1)
    assert get_x(c) == 1 and get_r(c) == 1 and get_y(c) == 1 
    # radius < 0
    try:
        c = create_circle(1,1,-1)
        assert False
    except ValueError:
        assert True
    
    #not in first quadrant
    try:
        c = create_circle(1,1,2)
        assert False
    except ValueError:
        assert True


test_create_circle() 