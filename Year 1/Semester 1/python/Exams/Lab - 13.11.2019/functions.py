from domain import *

def add_coffee(name, country, price, coffeeList):
    coffee = create_coffee(name, country, price)
    msg = validate_coffee(name, country, price, coffeeList)
    if msg is not None:
        print(msg)
    else:
        coffeeList.append(coffee)

def sort_coffee(coffeeList):
    for i in range(0, len(coffeeList)):
        for j in range(i + 1, len(coffeeList)):
            if get_coffee_country(coffeeList[i]) > get_coffee_country(coffeeList[j]):
                aux = coffeeList[i]
                coffeeList[i] = coffeeList[j]
                coffeeList[j] = aux
            elif get_coffee_country(coffeeList[i]) == get_coffee_country(coffeeList[j]) and get_coffee_price(coffeeList[i]) > get_coffee_price(coffeeList[j]):
                aux = coffeeList[i]
                coffeeList[i] = coffeeList[j]
                coffeeList[j] = aux

def filter_price(coffeeList, price):
    li = []
    for i in coffeeList:
        if get_coffee_price(i) < float(price):
            li.append(i)
    return li


def filter_country(coffeeList, country):
    li = []
    for i in coffeeList:
        if get_coffee_country(i) == country:
            li.append(i)
    return li

def remove_country(coffeeList, country):
    li = []
    for i in coffeeList:
        if get_coffee_country(i) != country:
            li.append(i)
    return li