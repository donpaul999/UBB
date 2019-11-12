'''
Create an app for a car rental business using a console based user interface. The app must allow keeping records of the company's list of clients, existing car pool
and rental history. The app must allow its users to manage clients, cars and rentals in the following ways:

* Clients
 - Add a new client. Each client is a physical person having a unique ID, name, age and driver license series.
 - Update the data for cleitn. 
 - Remove a client from active clients. Note that removing a client will also remove their entire rental history.
 - Search for clients based on ID and nme.
 - ALl client operations must undergo proper validation!

* Cars
 - Add a new car to the car pool. Each car must have a valid license plate number, a make and model taken from a list of makes and models. In addition, each car will 
 have color.
 - Search for cars based on license number, make, model and color.
 - All car operations must undergo proper validation!

* Rentals
 - An existing client can rent one or several cars from the car pool for a determined period. When rented, a car becomes unavailable for further renting.
 - When a car is returned, it becomes available for renting.
 - Search the rental history of a given client, car, or all rentals during any given period.

'''


