import random

class Navigate: 
    # def __init__(self, dirMoving, north, south, east, west, threshold):
    #     self.dirMoving = dirMoving
    #     self.north = north
    #     self.south = south
    #     self.west = west
    #     self.east = east
    #     self.threshold = threshold
    
    def update(self, dirMoving, north, south, east, west, threshold):
        self.dirMoving = dirMoving
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.threshold = threshold

    def determine(self):
        SensorList = [self.north, self.south, self.east, self.west]
        print([s.distance for s in SensorList])
        SensorList.sort(key=lambda x: x.distance)

        if SensorList[0].distance > self.threshold:
            return self.dirMoving
        else:
            d = [a for a in SensorList if a.distance > self.threshold]

            if len(d) > 0:
                ran = random.choice(d)
                return ran
            else:
                return SensorList[len(SensorList)-1]
            

        # print([s.distance from s in SensorList])

        
        
        


    
class SensorObj:
    def __init__(self,_direction = "", _distance = 0):
        self.direction = _direction
        self.distance = _distance
