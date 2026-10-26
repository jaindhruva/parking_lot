from datetime import datetime
from math import ceil

from ParkingGarage import ParkingGarage


class ParkingSystem:
    def __init__(self, parkingGarage, hourlyRate):    
        self._parking_garage = parkingGarage
        self._hourly_rate = hourlyRate  
        self._time_parked = {} # driverId : time parked

    def park_vehicle(self, driver):
        if self._parking_garage.park_vehicle(driver.getVehicle()):
            self._time_parked[driver.getId()] = datetime.now().hour
            return True
        return False

    def remove_vehicle(self, driver):
        if driver.getId() not in self._time_parked:
            return False
        curr_hour = datetime.now().hour
        hours_parked = ceil(self._time_parked[driver.getId()] - curr_hour) 
        amount_due = self._hourly_rate * hours_parked
        driver.charge(amount_due) 
        self._time_parked.pop(driver.getId(), None)
        return self._parking_garage.remove_vehicle(driver.getVehicle())
        
