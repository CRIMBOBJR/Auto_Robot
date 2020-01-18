from lib.motorCtrl import MotorControl
from time import sleep

class Commands:
    def __init__(self, db):
        self.db = db
        self.motor = MotorControl()


    def Routine_1(self):
        doc_ref = self.db.collection(u'Command').document(u'routine-1')
        doc_watch = doc_ref.on_snapshot(self.r_1_on_snapshot)

    def r_1_on_snapshot(self, dco_snapshot, changes, read_time):
        for doc in dco_snapshot:
            data = doc.to_dict()
            drive = (data['drive'])
            

            for driveDir in drive:
                d = driveDir
                direction = d['direction']
                driveFor = d['driveFor']

                if direction == 'N':
                    self.motor.Forward(driveFor)
                elif direction == 'S':
                    self.motor.Backward(driveFor)
                elif direction == 'E':
                    self.motor.Right(driveFor)
                elif direction == 'W':
                    self.motor.Left(driveFor)
                else:
                    print("nothing here")



                print('direction ' + direction + ' | driveFor :' + str(driveFor))
                sleep(driveFor)

            print(">>>>>END<<<<<")

    def Routine_2(self):
        doc_ref = self.db.collection(u'Command').document(u'routine-2')
        doc_watch = doc_ref.on_snapshot(self.r_2_on_snapshot)

    def r_2_on_snapshot(self, dco_snapshot, changes, read_time):
        for doc in dco_snapshot:
            data = doc.to_dict()
            drive = (data['drive'])
            

            for driveDir in drive:
                d = driveDir
                direction = d['direction']
                driveFor = d['driveFor']

                if direction == 'N':
                    self.motor.Forward(driveFor)
                elif direction == 'S':
                    self.motor.Backward(driveFor)
                elif direction == 'E':
                    self.motor.Right(driveFor)
                elif direction == 'W':
                    self.motor.Left(driveFor)
                else:
                    print("nothing here")



                print('direction ' + direction + ' | driveFor :' + str(driveFor))
                sleep(driveFor)

            print(">>>>>END<<<<<")

    def Routine_3(self):
        doc_ref = self.db.collection(u'Command').document(u'routine-3')
        doc_watch = doc_ref.on_snapshot(self.r_3_on_snapshot)

    def r_3_on_snapshot(self, dco_snapshot, changes, read_time):
        for doc in dco_snapshot:
            data = doc.to_dict()
            drive = (data['drive'])
            

            for driveDir in drive:
                d = driveDir
                direction = d['direction']
                driveFor = d['driveFor']

                if direction == 'N':
                    self.motor.Forward(driveFor)
                elif direction == 'S':
                    self.motor.Backward(driveFor)
                elif direction == 'E':
                    self.motor.Right(driveFor)
                elif direction == 'W':
                    self.motor.Left(driveFor)
                else:
                    print("nothing here")



                print('direction ' + direction + ' | driveFor :' + str(driveFor))
                sleep(driveFor)

            print(">>>>>END<<<<<")

    def Routine_4(self):
        doc_ref = self.db.collection(u'Command').document(u'routine-4')
        doc_watch = doc_ref.on_snapshot(self.r_4_on_snapshot)

    def r_4_on_snapshot(self, dco_snapshot, changes, read_time):
        for doc in dco_snapshot:
            data = doc.to_dict()
            drive = (data['drive'])
            

            for driveDir in drive:
                d = driveDir
                direction = d['direction']
                driveFor = d['driveFor']

                if direction == 'N':
                    self.motor.Forward(driveFor)
                elif direction == 'S':
                    self.motor.Backward(driveFor)
                elif direction == 'E':
                    self.motor.Right(driveFor)
                elif direction == 'W':
                    self.motor.Left(driveFor)
                else:
                    print("nothing here")



                print('direction ' + direction + ' | driveFor :' + str(driveFor))
                sleep(driveFor)

            print(">>>>>END<<<<<")
