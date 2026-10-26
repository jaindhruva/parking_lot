from ParkingFloor import ParkingFloor

class ParkingGarage:
    def __init__(self, noOfFloors, spotsPerFloor):
        self._parking_floors = [ParkingFloor(spotsPerFloor) for i in range(noOfFloors)]

    def park_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self,vehicle):
        for floor in self._parking_floors:
            if vehicle in floor._vehicle_spot_map:
                floor.remove_vehicle(vehicle)
                return True
        return False

