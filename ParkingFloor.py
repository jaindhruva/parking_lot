from Vehicle import *

class ParkingFloor:
    def __init__(self, no_of_spots):
        self._spots = [0]*no_of_spots
        self._vehicle_spot_map = {}

    def park_vehicle(self, vehicle):
        l, r = 0, 0
        for i in range(len(self._spots)):
            if self._spots[r] != 0:
                l = r + 1
                continue
            if r-l+1 == vehicle._spot_size:
                # found a spot
                for j in range(l,r+1):
                    self._spots[j] = 1
                self._vehicle_spot_map[vehicle] = [l,r]
                return True
            r += 1
        return False

    def remove_vehicle(self,vehicle):
        l,r = self._vehicle_spot_map[vehicle]
        for i in range(l, r+1):
            self._spots[i] = 0
        self._vehicle_spot_map.pop(vehicle, None)
        return True

    def get_parking_spots(self):
        return self._spots

    def get_vehicle_spots(self, vehicle):
        return self._vehicle_spot_map[vehicle]