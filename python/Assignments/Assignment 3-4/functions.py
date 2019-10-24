#APARTMENT BUILDING ADMINISTRATOR - Functions
from domain import *


#Set functions
def set_apartment_expense(apartment, type_e, amount): #Set the money to be payed(amount) by the apartment for an expense(type_e)
    apartment[type_e] = amount
#Set functions end


def add_apartment(ap_id, type_e, amount, type_list, apartmentList):
    '''
    If apartment is valid it can be added to the list
    ''' 
    msg = validate_data(ap_id, type_e, amount, type_list)
    if msg is not None:
        print(msg)
    else:
        apartment = create_apartment(ap_id, type_e, amount)
        apartmentList.append(apartment)


def test_add_apartment():
    aplist = []
    ap = create_apartment(39, "gas", 100)
    aplist.append(ap)
    assert get_ap_id(ap) == 39
    assert get_ap_amount_for_type(ap, "gas") == 100
    assert get_ap_amount_for_type(ap, "water") == 0
    assert len(aplist) == 1


def sum_expense(apartments, expense):
    '''
    Input - list of apartments
          - an expense from the list
    Output- returns sum of the amounts from apartments for the expense sent as parameter
    '''
    sum = 0
    for ap in apartments:
        sum += get_ap_amount_for_type(ap, expense)
    return sum  


def max_expense(apartment, expenses):
    '''
    Input - an apartment given by user
          - list of expenses
    Output- return the maximum expense for the apartment given by user
    '''
    maxi = 0
    max_ex = 0
    for ex in expenses:
       if get_ap_amount_for_type(apartment, ex) > maxi:
           maxi = get_ap_amount_for_type(apartment, ex)
           max_ex = ex
    if maxi == 0:
        return "There is no amount of money to be payed by this apartment"
    else:
        return str(max_ex) + ": " + str(maxi) 

      
            
def remove_apartments(apartments, start, end):
    '''
    The parameters start, end are given by user and if they are valid ->
    ->  Remove apartments from the list with the id >= start and <= end
    '''
    ok = 0
    for i in range(len(apartments)):
      if int(get_ap_id(apartments[i])) >= start and int(get_ap_id(apartments[i])) <= end:
          del apartments[i]
          ok = 1
          break
    if ok == 1:
        remove_apartments(apartments, start, end)

def remove_apartment_ui(apartments, params, expenses):
    '''
    Here the command "remove" given by user is processed
    1.remove an expense from the list
    2.remove an apartment
    3.remove more than one apartments
    The parameters are validated first
    '''
    if len(params) == 1:
        try:
            index = expenses.index(params[0])
            expenses.pop(index)
        except:
            try:
                for i in range(len(apartments)):
                    if int(get_ap_id(apartments[i])) == int(params[0]):
                        del apartments[i]
                        break
            except:
                print_remove_error()
    elif len(params) == 3:
        try:
            remove_apartments(apartments, int(params[0]), int(params[2]))
        except:
            print_remove_error()
    else:
        print_remove_error()
