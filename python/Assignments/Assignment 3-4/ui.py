#APARTMENT BUILDING ADMINISTRATOR - UI
from domain import *
from functions import *

def add_apartment_expense_ui(apartments, params,type_list):
    '''
    Input - list of apartments, parameters given by user, expenses list
    Output - Nothing
    The function adds the apartment to the list if is not already there, or appends to the apartment a new expense
    '''
    if len(params) != 3:
        print_adding_error()
        return
    ok = 0
    if validate_expense(params[1], type_list) == 1:
        for ap in apartments:
            if int(get_ap_id(ap)) == int(params[0]):
                try:
                    set_apartment_expense(ap, params[1], int(get_ap_amount_for_type(ap, params[1])) + int(params[2]))
                except:
                    print_adding_error()
                ok = 1
    if ok == 0:
        add_apartment(int(params[0]), params[1], int(params[2]), type_list, apartments)



def replace_apartment_ui(apartments,params, type_list):
    '''
    If the apartment exists in the list and the expense is in the expenses list too, it will update the amount of money to be paid
    for that expense
    '''
    ok = 0
    if len(params) != 4 or params[2] != 'with':
       print_replace_error()
       return
    for ap in apartments:
        if int(get_ap_id(ap)) == int(params[0]):
            if validate_expense(params[1], type_list) == 1:
                set_total_expenses(ap, (-1) * get_ap_amount_for_type(ap, params[1]))
                set_apartment_expense(ap, params[1],  int(params[3]))
            ok = 1
    if ok == 0:
        print_apartment_error()

#Error printing functions
def print_type_error():
    print("The expense is not in the list!")
def print_apartment_error():
    print("Apartment is not in the list!")
def print_adding_error():
    print("Bad apartment parameters!")
def print_remove_error():
    print("Bad remove parameters!")
def print_replace_error():
    print("Bad replacement parameters!")
def print_list_error():
    print("Invalid listing parameters!")
def print_sum_error():
    print("Invalid sum parameters!")
def print_max_error():
    print("Invalid max parameters!")

#Error printing functions end

def sum_expense_ui(apartments, param, expenses):
    '''
    Input - list of apartments
          - list of parameters sent by user
          - list of expenses
    Output- prints the sum of the amounts from the apartments for the expense sent as parameter(if the data is valid)
    '''
    if len(param) != 1:
        print_sum_error()
    else:
        if validate_expense(param[0], expenses) == 1:
            print("The sum for " + param[0] + " is: " + str(sum_expense(apartments, param[0])))


def max_expense_ui(apartments, params, expenses):
    '''
    Input - list of apartments
          - parameters given by user
          - list of expenses
    Output- prints the the maximum expense for the apartment given by user(if the data is valid)
    '''
    if len(params) != 1:
        print_max_error()
    else:
        ok = 0
        try:
            int(params[0])
        except:
           print_max_error()
           return
        for i in apartments:
            if int(get_ap_id(i)) == int(params[0]):
                ok = 1
                break
        if ok == 1:
            print(max_expense(i, expenses))
        else:
            print_apartment_error()

    
def print_apartments(apartments, type_list, start, end):
    '''
    Print the list of apartments with the id >= start and <= end
    If there is no apartment with such an id, there is a message to show this
    '''
    print("**********************")
    if len(apartments) == 0:
        print("There are no apartments in the list!")
        print("**********************")
        return
    ok = 0
    for i in apartments:
        if start <= get_ap_id(i) and end >= get_ap_id(i) or end == -1:
            ok = 1
    if ok == 1:
        print("List of apartments:")
        for i in apartments:
          ok = 0
          if get_total_expenses(i) != 0 :
              if start <= get_ap_id(i) and end >= get_ap_id(i) or end == -1:
                print ("Apartment id: " + str(get_ap_id(i)) , end=" ")
                ok = 1
                for  j in type_list:
                    if get_ap_amount_for_type(i,j) is not None and get_ap_amount_for_type(i,j) != 0:
                        print(j + ": " + str(get_ap_amount_for_type(i,j)), end = " ")
          if ok == 1:
              print("Total: " + str(get_total_expenses(i)))
              print ('\n')
    else:
        print("There is no apartment with this id!")
    print("**********************")



def print_apartments_expense(apartments, expenses, comparison, amount):
    '''
    Print a list of apartments where the total expenses are in a relation of <,= or > than the amount given by the user
    If there is no apartment to have this property, there is a message to show this
    '''
    print("**********************")
    ok = 0
    if comparison == '<':
        for ap in apartments:
            if get_total_expenses(ap) < amount:
                ok = 1
                print("Apartment id: " + str(get_ap_id(ap)) + " Total: " + str(get_total_expenses(ap)))
    elif comparison == '=':
        for ap in apartments:
            if get_total_expenses(ap) == amount:
                ok = 1
                print("Apartment id: " + str(get_ap_id(ap)))

    elif comparison == '>':
        for ap in apartments:
            if get_total_expenses(ap) > amount:
                ok = 1
                print("Apartment id: " + str(get_ap_id(ap)) + " Total: " + str(get_total_expenses(ap)))
    else:
        print_list_error()
    print("**********************")



def print_apartments_ui(apartments, params, type_list):
    '''
    The command 'list' is processed:
    1. It prints a list of apartments with ids between 2 boundaries
    2. It prints a list of apartments with the total expense in a relation of <,= or > than an amount given by a user
    3. It prints only an apartment
    Also, the command inputed by the user is valided
    '''
    if int(len(params)) == 3:
        try:
            print_apartments(apartments, type_list, int(params[0]), int(params[2]))
        except:
            print_list_error()
    elif int(len(params)) == 2:
        try:
            print_apartments_expense(apartments, type_list, params[0], int(params[1]))
        except:
            print_list_error()
    elif int(len(params)) == 1:
          try:
              print_apartments(apartments, type_list, int(params[0]),int(params[0]))
          except:
              print_list_error()
    elif int(len(params)) == 0:
          print_apartments(apartments, type_list, -1, -1)
    else:
          print("Invalid parameters!")

def remove_apartment_ui(apartments, params, expenses):
    '''
    Here the command "remove" given by user is processed
    1.remove an expense from the list
    2.remove an apartment
    3.remove more than one apartments
    The parameters are validated first
    '''
    if len(params) == 1:
        if validate_expense(params[0], expenses) == 1:
            for i in apartments:
                set_total_expenses(i, (-1) * get_ap_amount_for_type(i, params[0]))
                set_apartment_expense(i,params[0], 0)
        else:
            try:
                for i in range(len(apartments)):
                    if int(get_ap_id(apartments[i])) == int(params[0]):
                        del apartments[i]
                        break
            except:
                print_remove_error()
    elif len(params) == 3:
        if params[1] == 'to':
            try:
                remove_apartments(apartments, int(params[0]), int(params[2]))
            except:
                print_remove_error()
        else:
            print_remove_error()
    else:
        print_remove_error()


def print_help_menu():
    print("**********************")
    print("1. Add a new transaction to the list.")
    print("add <apartment> <type> <amount>")
    print("e.g.")
    print("add 25 gas 100 – add to apartment 25 an expense for gas in amount of 100 RON.")
    print("2. Modify expenses from the list.")
    print("remove <apartment>")
    print("remove <start apartment> to <end apartment>")
    print("remove <type>")
    print("replace <apartment> <type> with <amount>")
    print("e.g.")
    print("remove 15 – remove all the expenses of apartment 15.")
    print("remove 5 to 10 – remove all the expenses from apartments between 5 and 10.")
    print("remove gas – remove all the expenses for gas from all apartments.")
    print("replace 12 gas with 200 – replace the amount of the expense with type gas for apartment 12 with 200 RON.")
    print("3. Write the expenses having different properties.")
    print("list")
    print("list <apartment>")
    print("list [ < | = | > ] <amount>")
    print("e.g.")
    print("list – write the entire list of expenses.")
    print("list 15 – write all expenses for apartment 15.")
    print("list > 100 - write all the apartments having total expenses > 100 RON.")
    print("list = 17 - write all the apartments having total expenses = 17 RON.")
    print("**********************")


def readCommand(): #Read and parse the user's command
    cmd = input("command: ")
    #1. Separate command word from list of params
    #2. Identify params
    #3. Return tuple
    idx = cmd.find(" ")
    if idx == -1:
        return (cmd, [])
    command = cmd[:idx]
    params = cmd[idx:]
    params = params.split(" ")
    params.pop(0)
    for i in range(len(params)):
        params[i] = params[i].strip()
    return (command, params)




def start():
    apartments = init_apartments()
    expenses = init_expenses()
    while True: #read user command
        cmdtuple = readCommand()
        cmd = cmdtuple[0]
        params = cmdtuple[1]
        if cmd == 'add':
            add_apartment_expense_ui(apartments, params, expenses)
        elif cmd == 'list':
            print_apartments_ui(apartments, params, expenses)
        elif cmd == 'replace':
            replace_apartment_ui(apartments, params, expenses)
        elif cmd == 'remove':
            remove_apartment_ui(apartments, params, expenses)
        elif cmd == 'help':
            print_help_menu()
        elif cmd == "sum":
            sum_expense_ui(apartments, params, expenses)
        elif cmd == "max":
            max_expense_ui(apartments, params, expenses)
        elif cmd == 'exit':
            break
        else:
            print("Invalid command!")

test_add_apartment()
start()
