def create_horse(hid, c,w,h):
    '''
    function that creates a horse based on its identifiers (hid), colour(c),weight(w), height(h)
    input: hid - integer, c - string, w - float, h - float
    output: h - a horse
    '''
    return [hid,c,w,h]

def get_hid(h):
    '''
    function that gets the id of the horse h
    input: h - horse
    output: id - the integer value representing the id of the horse
    '''
    return h[0]

def get_colour(h):
    '''
    function that gets the colour of the horse h
    input: h - horse
    output: c - the integer value representing the colour of the horse
    '''
    return h[1]

def get_weight(h, val):
    '''
    function that gets the weight of the horse h
    input: h - horse
    output:  w - the integer value representing the  weight of the horse
    '''
    h[2] = val

def test_horse():
    h = create_horse(1,"green", 1500, 3.0)
    assert(get_hid(h) == 1)
    assert(get_color(h) == "green")
    assert(get_weight(h) == 1500)
    set_weight(h, 1515)
    assert(get_weight(h) == 1515)
