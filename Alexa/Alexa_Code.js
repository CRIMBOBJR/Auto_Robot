// This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK (v2).
// Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
// session persistence, api calls, and more.
const Alexa = require('ask-sdk-core');
const https = require('https');
const request = require('request');

const LaunchRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'LaunchRequest';
    },
    handle(handlerInput) {
        const speakOutput = 'Welcome, you can say Hello or Help. Which would you like to try?';
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

function _piRobotCommandURL2(url, _data) {
    let options = {
        url: url, 
        form: _data
    };
    
    return new Promise((resolve, reject) => {
        request.post(options, (error, response, body) => {
            if (!error) {
                resolve(1);
            } else {
                reject(-1);
            }
        });
    });
}

function _RobotCommandURL(url) {
    return new Promise((resolve, reject) => {
        https.get(url,(res) =>{
           res.on('data', d =>{
               resolve(1);
           }); 
        })
        .on('error', (e) => {
            reject(-1);
        });
    });
}

const DriveForwardIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'driveForwardIntent';
    },
    async handle(handlerInput) {
        let sec = 0;
        sec = parseInt(Alexa.getSlotValue(handlerInput.requestEnvelope, 'driveFor'), 10);
        let alert = await _piRobotCommandURL2("https://us-central1-raspberry-4b563.cloudfunctions.net/driveForward",{ seconds:sec }).catch(e => e);
        let speakTxt = "";
        if(alert === -1){
            speakTxt = "oh no an error";
        }
        else{
            if(isNaN(sec) === false){
                speakTxt = "Robot is driving forward for " + sec + " seconds";
            }
            else {
            speakTxt = "We moving forward boys";
            }
        }
        return handlerInput.responseBuilder
            .speak(speakTxt)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const DriveBackwardIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'driveBackwardIntent';
    },
    async handle(handlerInput) {
         let sec = 0;
        sec = parseInt(Alexa.getSlotValue(handlerInput.requestEnvelope, 'driveFor'), 10);
        let alert = await _piRobotCommandURL2("https://us-central1-raspberry-4b563.cloudfunctions.net/driveBackward",{ seconds:sec }).catch(e => e);
        let speakTxt = "";
        if(alert === -1){
            speakTxt = "oh no an error";
        }
        else{
            if(isNaN(sec) === false){
                speakTxt = "Robot is driving backward for " + sec + " seconds";
            }
            else {
            speakTxt = "We moving backward boys";
            }
        }
        return handlerInput.responseBuilder
            .speak(speakTxt)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const DriveRightIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'driveRightIntent';
    },
    async handle(handlerInput) {
         let sec = 0;
        sec = parseInt(Alexa.getSlotValue(handlerInput.requestEnvelope, 'driveFor'), 10);
        let alert = await _piRobotCommandURL2("https://us-central1-raspberry-4b563.cloudfunctions.net/driveRight",{ seconds:sec }).catch(e => e);
        let speakTxt = "";
        if(alert === -1){
            speakTxt = "oh no an error";
        }
        else{
            if(isNaN(sec) === false){
                speakTxt = "Robot is driving right for " + sec + " seconds";
            }
            else {
            speakTxt = "We moving right boys";
            }
        }
        return handlerInput.responseBuilder
            .speak(speakTxt)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const DriveLeftIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'driveLeftIntent';
    },
    async handle(handlerInput) {
         let sec = 0;
        sec = parseInt(Alexa.getSlotValue(handlerInput.requestEnvelope, 'driveFor'), 10);
        let alert = await _piRobotCommandURL2("https://us-central1-raspberry-4b563.cloudfunctions.net/driveLeft",{ seconds:sec }).catch(e => e);
        let speakTxt = "";
        if(alert === -1){
            speakTxt = "oh no an error";
        }
        else{
           if(isNaN(sec) === false){
                speakTxt = "Robot is driving left for " + sec + " seconds";
            }
            else {
            speakTxt = "We moving left boys";
            }
        }
        return handlerInput.responseBuilder
            .speak(speakTxt)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const RoutineOneIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'RoutineOneIntent';
    },
    async handle(handlerInput) {
        let alert = await _RobotCommandURL("https://us-central1-raspberry-4b563.cloudfunctions.net/Routine_1").catch(e => e);
        let speakTxt = "";
        if(alert === -1){
            speakTxt = "oh no an error";
        }
        else{
            speakTxt = "Routine boys";
        }
        return handlerInput.responseBuilder
            .speak(speakTxt)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const HelloWorldIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'HelloWorldIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'Hello World!';
        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};
const HelpIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.HelpIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'You can say hello to me! How can I help?';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};
const CancelAndStopIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && (Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.CancelIntent'
                || Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.StopIntent');
    },
    handle(handlerInput) {
        const speakOutput = 'Goodbye!';
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .getResponse();
    }
};
const SessionEndedRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'SessionEndedRequest';
    },
    handle(handlerInput) {
        // Any cleanup logic goes here.
        return handlerInput.responseBuilder.getResponse();
    }
};

// The intent reflector is used for interaction model testing and debugging.
// It will simply repeat the intent the user said. You can create custom handlers
// for your intents by defining them above, then also adding them to the request
// handler chain below.
const IntentReflectorHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest';
    },
    handle(handlerInput) {
        const intentName = Alexa.getIntentName(handlerInput.requestEnvelope);
        const speakOutput = `You just triggered ${intentName}`;

        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

// Generic error handling to capture any syntax or routing errors. If you receive an error
// stating the request handler chain is not found, you have not implemented a handler for
// the intent being invoked or included it in the skill builder below.
const ErrorHandler = {
    canHandle() {
        return true;
    },
    handle(handlerInput, error) {
        console.log(`~~~~ Error handled: ${error.stack}`);
        const speakOutput = `Sorry, I had trouble doing what you asked. Please try again.`;

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

// The SkillBuilder acts as the entry point for your skill, routing all request and response
// payloads to the handlers above. Make sure any new handlers or interceptors you've
// defined are included below. The order matters - they're processed top to bottom.
exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(
        LaunchRequestHandler,
        HelloWorldIntentHandler,
        DriveLeftIntentHandler,
        DriveRightIntentHandler,
        DriveBackwardIntentHandler,
        DriveForwardIntentHandler,
        RoutineOneIntentHandler,
        HelpIntentHandler,
        CancelAndStopIntentHandler,
        SessionEndedRequestHandler,
        IntentReflectorHandler, // make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
    )
    .addErrorHandlers(
        ErrorHandler,
    )
    .lambda();
