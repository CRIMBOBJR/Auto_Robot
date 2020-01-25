# This is where we keep all the code that continuosly 
# looks at Firebase to see if there are any changes. 
# Then once it sees a change in Firebase it will call 
# on the corresponding motor function. 

from lib.motorCtrl import MotorControl

class FirebaseListener:
    def __init__(self, db):
        self.db = db
        self.motor = MotorControl()

    # This is the function that watches the collection of 
    # datapoints that corresponds to the forward function.
    def ForwardListener(self):
        doc_ref = self.db.collection(u'Motor').document(u'Forward')
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)

    # This is the function that watches the collection of 
    # datapoints that corresponds to the backward function.
    def BackListener(self):
        doc_ref = self.db.collection(u'Motor').document(u'Backward')
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)

    # This is the function that watches the collection of 
    # datapoints that corresponds to the right function. 
    def RightListener(self):
        doc_ref = self.db.collection(u'Motor').document(u'Right')
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)

    # This is the function that watches the collection of 
    # datapoints that corresponds to the left function.
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

            

            # This is the function that calls on the left motor function 
            # after is the function above sees a change in the left data points. 
            if doc.id == 'Left':
                print("Left : " + isOnStr)
                if isOn is True:
                    self.motor.Left(driveFor)
                    self.db.collection(u'Motor').document(u'Left').set({
                        u'isOn': False,
                        u'driveFor': 1
                    })

            # This is the function that calls on the right motor function 
            # after is the function above sees a change in the right data points.
            elif doc.id == 'Right':
                print("Right : " + isOnStr)
                if isOn is True:
                    self.motor.Right(driveFor)
                    self.db.collection(u'Motor').document(u'Right').set({
                        u'isOn': False,
                        u'driveFor': 1
                    })

            # This is the function that calls on the forward motor function 
            # after is the function above sees a change in the forward data points.
            elif doc.id == 'Forward':
                print("Forward : " + isOnStr)
                if isOn is True:
                    self.motor.Forward(driveFor)
                    self.db.collection(u'Motor').document(u'Forward').set({
                        u'isOn': False,
                        u'driveFor': 1
                    })

            # This is the function that calls on the backward motor function 
            # after is the function above sees a change in the backward data points.
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
            