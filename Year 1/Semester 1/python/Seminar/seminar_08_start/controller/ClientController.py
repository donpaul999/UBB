# from controller.UndoController import FunctionCall, Operation, CascadedOperation
from domain.Client import Client
from controller.UndoController import *

class ClientController:
    def __init__(self, undoController, rentalController, validator, repository):
        self.__validator = validator
        self.__repository = repository
        self._rentalController = rentalController
        self._undoController = undoController

    def create(self, clientId, clientCNP, clientName):
        client = Client(clientId, clientCNP, clientName)
        self.__validator.validate(client)
        self.__repository.store(client)
        return client

    def delete(self, clientId):
        '''
            1. Delete the client
        '''
        client = self.__repository.delete(clientId)

        undo = FunctionCall(self.create, clientId, client.cnp, client.name)
        redo = FunctionCall(self.delete, clientId)
        op = Operation(undo, redo)
        self._undoController.recordOperation(op)

        '''
            2. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rentalController.filterRentals(client, None) 
        for rent in rentals:
            self._rentalController.deleteRental(rent.getId(), False)
           
        return client

    def getClientCount(self):
        return len(self.__repository)

    def update(self, car):
        '''
            NB! Undo/redo is also needed here
        '''
        pass
