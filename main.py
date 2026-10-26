from ParkingGarage import ParkingGarage
from ParkingSystem import ParkingSystem
from Driver import Driver
from Vehicle import *


class main:

    def __init__(self):

        parkingGarage = ParkingGarage(5, 2)
        parkingSystem = ParkingSystem(parkingGarage, 5)

        driver1 = Driver(1, Car())
        driver2 = Driver(2, Limo())
        driver3 = Driver(3, SemiTruck())
        print('**')

        print(parkingSystem.park_vehicle(driver1))      # true
        print(parkingSystem.park_vehicle(driver2))      # true
        print(parkingSystem.park_vehicle(driver3))      # false
        print('**')

        print(parkingSystem.remove_vehicle(driver1))    # true
        print(parkingSystem.remove_vehicle(driver2))    # true
        print(parkingSystem.remove_vehicle(driver3))    # false

main()

