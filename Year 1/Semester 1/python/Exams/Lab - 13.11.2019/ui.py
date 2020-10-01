from domain import *
from functions import *



def print_menu():
    print("1. Add a coffee")
    print("2. Print all coffee")
    print("3. Filter coffee based on country of origin and price")
    print("4. Delete all coffee from a given country")
    print("5. Exit")


def add_coffee_ui(coffeeList):
    '''
    Add a new coffee to the list - if the coffe's characteristics are valid
    '''
    name = input("Name: ")
    country = input("Country of origin: ")
    price = input("Price: ")
    add_coffee(name, country, price, coffeeList)

def print_coffee_ui(coffeeList):
     print("***********")
     sort_coffee(coffeeList)
     id = 0
     for i in coffeeList:
         id += 1
         print(str(id) + ". Name: " + get_coffee_name(i) + ", Country of origin: " + get_coffee_country(i) + ", Price: " + str(get_coffee_price(i)))
         print("")
     print("***********")

def filter_coffee_ui(coffeeList):
    country = input("Country: ")
    price = input("Price: ")
    if country == '' and price == '':
        print("No such coffees!")
    elif country == '':
        li = filter_price(coffeeList, price)
        if len(li) > 0:
            print_coffee_ui(li)
        else:
            print("No such coffees!")
    elif price == '':
        li = filter_country(coffeeList, country)
        if len(li) > 0:
            print_coffee_ui(li)
        else:
            print("No such coffees!")
    else:
        li1 = filter_price(coffeeList, price)
        li2 = filter_country(li1, country)
        if len(li2) > 0:
            print_coffee_ui(li2)
        else:
            print("No such coffees!")

def delete_coffee_ui(coffeeList):
    country = input("Country: ")
    len_start = len(coffeeList)
    coffeeList = remove_country(coffeeList, country)
    if len_start == len(coffeeList):
        print("Nothing was deleted!")
    else:
        print_coffee_ui(coffeeList)
    return coffeeList

def start():
    coffeeList = init_coffee()
    while True:
        print_menu()
        choice = input(">")
        if choice == "1":
            add_coffee_ui(coffeeList)
        elif choice == "2":
            print_coffee_ui(coffeeList)
        elif choice == "3":
            filter_coffee_ui(coffeeList)
        elif choice == "4":
            coffeeList = delete_coffee_ui(coffeeList)
        elif choice == "5":
            return;
        else:
            print("Invalid command")


def test_add():
    c = create_coffee("Cappuccino", "India", 2.5)
    assert get_coffee_name(c) == "Cappuccino"
    assert get_coffee_country(c) == "India"
    assert get_coffee_price(c) == 2.5
    li = []
    try: 
        c = add_coffee("Irish", "Ireland", 10, li)
        assert True
    except:
        assert False
    
    msg = validate_coffee("yi","China", 0, li)
    if msg is None:
        assert False
    else:
        assert True        


test_add()
start()