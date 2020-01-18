
from lib.motorCtrl import MotorControl

class FirebaseListener:
    def __init__(self, db):
        self.db = db
        self.motor = MotorControl()

        
    def ForwardListener(self):
        doc_ref = self.db.collection(u'Motor').document(u'Forward')
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)

    def BackListener(self):
        doc_ref = self.db.collection(u'Motor').document(u'Backward')
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)

    def RightListener(self):
        doc_ref = self.db.collection(u'Motor').document(u'Right')
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)

    def LeftListener(self):
        doc_ref = self.db.collection(u'Motor').document(u'Left')
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)

    def on_snapshot(self,doc_snapshot, changes, read_time):
        for doc in doc_snapshot:
            print(doc.id)
            data = doc.to_dict()
            isOnStr = str(data['isOn'])
            isOn = data['isOn']
            driveFor = data['driveFor']

            


            if doc.id == 'Left':
                print("Left : " + isOnStr)
                if isOn is True:
                    self.motor.Left(driveFor)
                    self.db.collection(u'Motor').document(u'Left').set({
                        u'isOn': False,
                        u'driveFor': 1
                    })

            elif doc.id == 'Right':
                print("Right : " + isOnStr)
                if isOn is True:
                    self.motor.Right(driveFor)
                    self.db.collection(u'Motor').document(u'Right').set({
                        u'isOn': False,
                        u'driveFor': 1
                    })

            elif doc.id == 'Forward':
                print("Forward : " + isOnStr)
                if isOn is True:
                    self.motor.Forward(driveFor)
                    self.db.collection(u'Motor').document(u'Forward').set({
                        u'isOn': False,
                        u'driveFor': 1
                    })

            elif doc.id == 'Backward':
                print("Backward : " + isOnStr)
                if isOn is True:
                    self.motor.Backward(driveFor)
                    self.db.collection(u'Motor').document(u'Backward').set({
                        u'isOn': False,
                        u'driveFor': 1
                    })

            else: 
                print('there is nothhing')
            
            # right = data['Right']
            # left = data['Left']
            # forward = data['Forward']
            # backward = data['Backward']
            # setup = data['Setup']
            # print(u'Received document snapshot: {}'.format(data))