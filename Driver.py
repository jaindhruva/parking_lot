class Driver:
    def __init__(self, id, vehicle):
        self._id = id
        self._vehicle = vehicle
        self._amount_due = 0

    def getVehicle(self):
        return self._vehicle

    def getId(self):
            return self._id

    def charge(self, amount):
        self._amount_due += amount