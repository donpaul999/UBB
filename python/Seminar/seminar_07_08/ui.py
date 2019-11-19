'''
Create an application for a car rental business using a console based user interface. The application must  allow keeping records of the companyâs list of clients, existing car pool and rental history. The application must allow its users to manage clients, cars and rentals in the following ways:

* Clients

 - Add a new client. Each client is a physical person having a unique ID, name and age

 - Update the data for any client.

 - Remove a client from active clients. Note that removing a client must not remove existing car rental statistics.

 - Search for clients based on ID and name.

 - All client operations must undergo proper validation!

* Cars

 - Add a new car to the car pool. Each car must have a valid license plate number, a make, a model and a color.

 - Remove a car from the car pool.

 - Search for cars based on license number, make and model and color.

 - All car operations must undergo proper validation!

* Rentals

 - An existing client can rent one or several cars from the car pool for a determined period. When rented, a car becomes unavailable for further renting.

 - When a car is returned, it becomes available for renting once again.

* Statistics

 - All cars in the car pool sorted by number of days they were rented.

 - The list of clients sorted descending by the number of cars they have rented.

'''


class UI:
    pass