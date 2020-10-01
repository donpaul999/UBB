class Order:
    def __init__(self, ID, km):
        self._ID = ID
        self._km = km

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = int(value)

    @property
    def km(self):
        return self._km

    @km.setter
    def km(self, value):
        self._km = int(value)

class Driver:
    def __init__(self, ID, name):
        self._ID = ID
        self._name = name

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = int(value)

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._Name = Name
