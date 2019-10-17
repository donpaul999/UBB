#APARTMENT BUILDING ADMINISTRATOR


def validate_data(ap_id, type_e, amount, type_list): # Validate input data
    if ap_id <= 0 : #Apartment id should be > 0
        return "Invalid apartament id!"
    if amount <= 0: #The cost should be > 0
        return "Invalid cost!"
    ok = 0
    for t in type_list: #Type of expense should be found in the list
        if type_e == t:
            ok = 1
    if ok == 0:
        return "Type of expense is not on the list!"
    return None

def create_apartment(ap_id, type_e, amount): #Create an apartment
    return{"ap_id":ap_id, type_e:amount}



def add_apartment(ap_id, type_e, amount, type_list, apartmentList):
    msg = validate_data(ap_id, type_e, amount, type_list)
    if msg is not None:
        print(msg)
    else:
        apartment = create_apartment(ap_id, type_e, amount)
        apartmentList.append(apartment)



def get_ap_id(apartment):
    return apartment["ap_id"]

def get_ap_amount_for_type(apartment, type_e):
    try:
        return apartment[type_e]
    except:
        return 0
    
def get_total_expenses(apartment, type_e):
    sum = 0 
    for i in type_e:
        sum += get_ap_amount_for_type(apartment, i)
    return sum


def set_apartment_expense(apartment, type_e, amount): #Set the expense amount
        apartment[type_e] = amount



def init_apartments(): #Initialize apartments
    res = []
    res.append(create_apartment(25, "gas", 100))
    res.append(create_apartment(24, "gas", 131))
    res.append(create_apartment(21, "gas", 1))
    res.append(create_apartment(10, "water", 52))
    res.append(create_apartment(12, "gas", 21))
    res.append(create_apartment(2, "gas", 21))
    res.append(create_apartment(6, "gas", 92))
    res.append(create_apartment(1, "gas", 10))
    res.append(create_apartment(100, "gas", 11))
    return res


def init_expenses(): #Initialize expenses types
    res = []
    res.append("gas")
    res.append("water")
    res.append("electricity")
    res.append("heat")
    res.append("other")
    return res

def  add_apartment_expense_ui(apartments, params,type_list):
    if len(params) != 3:
        print("Bad apartment parameters!")
        return

    ok = 0
    for ap in apartments:
        if int(get_ap_id(ap)) == int(params[0]):
            set_apartment_expense(ap, params[1], int(get_ap_amount_for_type(ap, params[1])) + int(params[2]))
            ok = 1  
    if ok == 0:        
        add_apartment(int(params[0]), params[1], int(params[2]), type_list, apartments)

        
def replace_apartment_ui(apartments,params, type_list):
    if len(params) != 4:
       print_replace_error()
       return
    for ap in apartments:
        if int(get_ap_id(ap)) == int(params[0]):
            set_apartment_expense(ap, params[1], int(params[3]))


def print_remove_error():
    print("Bad remove parameters!")

def print_replace_error():
    print("Bad replacement parameters!")

def print_list_error():
    print("Invalid listing parameters!")


def remove_apartments(apartments, start, end):
    ok = 0
    for i in range(len(apartments)):
      if int(get_ap_id(apartments[i])) >= start and int(get_ap_id(apartments[i])) <= end:
          del apartments[i]
          ok = 1
          break
    if ok == 1:
        remove_apartments(apartments, start, end)

def remove_apartment_ui(apartments, params, expenses):
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




def print_apartments(apartments, type_list, start, end):
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
          if get_total_expenses(i, type_list) != 0 :
              if start <= get_ap_id(i) and end >= get_ap_id(i) or end == -1:
                print ("Apartment id: " + str(get_ap_id(i)) , end=" ")
                ok = 1
                for  j in type_list:
                    if get_ap_amount_for_type(i,j) is not None and get_ap_amount_for_type(i,j) != 0:
                        print(j + ": " + str(get_ap_amount_for_type(i,j)), end = " ")
          if ok == 1:
              print ('\n')
    else:
        print("There is no apartment with this id!")
    print("**********************")



def print_apartments_expense(apartments, expenses, comparison, amount):
    print("**********************")
    ok = 0
    if comparison == '<':
        for ap in apartments:
            if get_total_expenses(ap, expenses) < amount:
                ok = 1
                print("Apartment id: " + str(get_ap_id(ap)) + " Total: " + str(get_total_expenses(ap, expenses)))
    elif comparison == '=':
        for ap in apartments:
            if get_total_expenses(ap, expenses) == amount:
                ok = 1
                print("Apartment id: " + str(get_ap_id(ap)))

    elif comparison == '>':
        for ap in apartments:
            if get_total_expenses(ap, expenses) > amount:
                ok = 1
                print("Apartment id: " + str(get_ap_id(ap)) + " Total: " + str(get_total_expenses(ap, expenses)))
    else:
        print_list_error()
    print("**********************")            
             
    

def print_apartments_ui(apartments, params, type_list):
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

def print_help_menu():
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
        elif cmd == 'exit':
            break
        else:
            print("Invalid command!")

start()
