from domain import *
from Repository import *
'''
0. Writing domain classes
1. Unit testing the proper way
2. A new layer? - Repository
'''

'''
Assignment 01 - 05
-------------
    UI -> Service -> domain
    
    UI
        - user interface for entire program
    Service 
        - functions that solve the problem
    Repository
        - manage the list of domain entities
    Domain
        - Entities from problem domain

    UI -> Service -> Repository -> Domain
                  -> Domain 
        -> Domain

'''

clientRepo = ClientRepository()
#service needs a repo that stores entities
clientService = clientService(clientRepo)

ui = UI(clientService)
ui.start()