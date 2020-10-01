
def create_coffee(name, country, price): #Create a new cofee
    return{"name" : name, "country_of_origin" : country, "price": float(price)}


def validate_coffee(name, country, price, coffeeList): 
    '''
    Validate if a coffee characteristics are valid or not.
    input - characteristics
    return - None if everything is ok 
           - an error message
    '''
    try:
        name = int(name)
        return "Coffee's name is not valid!"
    except:
        for i in coffeeList:
            if name == get_coffee_name(i):
                return "Coffee's name not unique!"
        if len(name) == 0:
            return "Coffee's name not valid!"
        try:
            country = int(country)
            return "Coffee's country is not valid!"
        except:
            if len(country) == 0:
                return "Coffee's country is not valid!"
            try:
                price = float(price)
                if price <= 0:
                    return "Coffee's price is not valid!"
            except:
                return "Coffee's price is not valid!"
    return None

def get_coffee_name(coffee):
    return coffee["name"]
def get_coffee_country(coffee):
    return coffee["country_of_origin"]
def get_coffee_price(coffee):
    return coffee["price"]


def init_coffee():
    li = []
    li.append(create_coffee("Green", "Brazil", 5.5))
    li.append(create_coffee("Black", "Colombia", 5.25))
    li.append(create_coffee("Gray", "Vietnam", 15.5))
    li.append(create_coffee("Irish Coffee", "Ireland", 5.9))
    li.append(create_coffee("Espresso", "US", 8.7))
    li.append(create_coffee("Tasty", "Brazil", 2.5))
    return li
