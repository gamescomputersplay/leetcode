''' https://leetcode.com/problems/design-parking-system/
'''

class ParkingSystem:

    def __init__(self, big, medium, small):
        self.capacity = [big, medium, small]

    def addCar(self, carType):
        if self.capacity[carType - 1]:
            self.capacity[carType - 1] -= 1
            return True
        return False
