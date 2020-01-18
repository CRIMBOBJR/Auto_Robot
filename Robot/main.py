# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# from lib.motorCtrl import MotorControl
# from lib.firebaseListner import FirebaseListener
# from lib.commands import Commands
# m = MotorControl()

from random import *

from lib.navigation import Navigate
from lib.navigation import SensorObj

n = Navigate()

northdir = randint(1, 220)

dirMoving = SensorObj("north", northdir)
north = SensorObj("north", northdir)
south = SensorObj("south", randint(1, 220))
east = SensorObj("east", randint(1, 220))
west = SensorObj("west", randint(1, 220))


n.update(dirMoving, north, south, east, west, 15)
print(n.determine().direction)

dirMoving = SensorObj("north", northdir)
north = SensorObj("north", northdir)
south = SensorObj("south", randint(1, 220))
east = SensorObj("east", randint(1, 220))
west = SensorObj("west", randint(1, 220))

n.update(dirMoving, north, south, east, west, 15)
print(n.determine().direction)

# def setup(): 
#     cred = credentials.Certificate('./lib/Key.json')
#     firebase_admin.initialize_app(cred)

#     fbl = FirebaseListener(firestore.client())
#     fbl.BackListener()
#     fbl.ForwardListener()
#     fbl.LeftListener()
#     fbl.RightListener()
   
#     c = Commands(firestore.client())
#     c.Routine_1()
#     c.Routine_2()
# def destroy(): 
#     m = MotorControl()
#     m.MotorCleanUp()
#     print("clean up")

# if __name__ == '__main__':
#     setup()
#     try:
#         print("running...")
#         t=input("Press any button to exit")
#     except KeyboardInterrupt:
#         destroy()