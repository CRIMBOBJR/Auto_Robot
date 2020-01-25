const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);


function getSeconds(request) {
    let seconds  = 1;
    try {
        seconds = parseInt(request.body.seconds);
    } catch (e) {
        console.log("error getting seconds");
    }
    if (isNaN(seconds) == true || seconds == null || seconds == undefined) {
        seconds = 1;
    }

    if(seconds > 4){
        seconds = 4
    }
    return seconds;
}



exports.driveForward = functions.https.onRequest(async (request, response) => {
    await admin.firestore().collection('Motor').doc('Forward').set({
            'isOn': true,
            'driveFor': getSeconds(request)
        }).then(() => {
            response(true);
        })
        .catch(e => {
            response(false);
        });
});

exports.driveBackward = functions.https.onRequest(async (request, response) => {
    await admin.firestore().collection('Motor').doc('Backward').set({
            'isOn': true,
            'driveFor': getSeconds(request)
        }).then(() => {
            response(true);
        })
        .catch(e => {
            response(false);
        });
});

exports.driveLeft = functions.https.onRequest(async (request, response) => {
    await admin.firestore().collection('Motor').doc('Left').set({
            'isOn': true,
            'driveFor': getSeconds(request)
        }).then(() => {
            response(true);
        })
        .catch(e => {
            response(false);
        });
});

exports.driveRight = functions.https.onRequest(async (request, response) => {
    await admin.firestore().collection('Motor').doc('Right').set({
            'isOn': true,
            'driveFor': getSeconds(request)
        }).then(() => {
            response(true);
        })
        .catch(e => {
            response(false);
        });
});


exports.Routine_1 = functions.https.onRequest(async (request, response) => {
    await admin.firestore().collection('Command').doc('routine-1').update({
            execute: new Date()
        }).then(() => {
            response(true);
        })
        .catch(err => {
            response(false);
        });
});


exports.Routine_2 = functions.https.onRequest(async (request, response) => {
    await admin.firestore().collection('Command').doc('routine-2').update({
            execute: new Date()
        }).then(() => {
            response(true);
        })
        .catch(err => {
            response(false);
        });
});

exports.Routine_3 = functions.https.onRequest(async (request, response) => {
    await admin.firestore().collection('Command').doc('routine-3').update({
            execute: new Date()
        }).then(() => {
            response(true);
        })
        .catch(err => {
            response(false);
        });
});

exports.Routine_4 = functions.https.onRequest(async (request, response) => {
    await admin.firestore().collection('Command').doc('routine-4').update({
            execute: new Date()
        }).then(() => {
            response(true);
        })
        .catch(err => {
            response(false);
        });
});