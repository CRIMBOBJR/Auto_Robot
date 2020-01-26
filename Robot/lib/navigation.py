#Uses sensor data to determine a path for the robot.

import random

class Navigate: 
    
    # Receives sensor data and stores data to be used.
    def update(self, dirMoving, north, south, east, west, threshold):
        self.dirMoving = dirMoving
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.threshold = threshold

    # Uses sensor data to determine a direction to move towards.
    def determine(self):
        SensorList = [self.north, self.south, self.east, self.west]
        print([s.distance for s in SensorList])
        # This sorts the the distances from lowest to highest
        SensorList.sort(key=lambda x: x.distance) 

        
        if SensorList[0].distance > self.threshold:
            return self.dirMoving
        else:
            d = [a for a in SensorList if a.distance > self.threshold]

            if len(d) > 0:
                # The random is used to pick a random 
                # direction the remaining distances 
                ran = random.choice(d)
                return ran
            else:
                return SensorList[len(SensorList)-1]


class SensorObj:
    def __init__(self,_direction = "", _distance = 0):
        self.direction = _direction
        self.distance = _distance
