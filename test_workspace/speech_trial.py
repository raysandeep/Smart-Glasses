import azure.cognitiveservices.speech as speechsdk
import boto3
import json

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "2fd9721033d44e02bd3dd3dcc7e53c1d", "westus2"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

#print("Say something...")


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.


a=1
comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')
while a==1:
    print("Say something...")
    result = speech_recognizer.recognize_once()

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        #print("Recognized: {}".format(result.text))
        if result.text is not None:
            #print(json.dumps(comprehend.detect_syntax(Text=result.text, LanguageCode='en'), sort_keys=True, indent=4))
            x = comprehend.detect_syntax(Text=result.text, LanguageCode='en')
            pos = x["SyntaxTokens"]
            for i in pos:
                print(i["PartOfSpeech"]["Tag"],'   THE TEXT WAS:', i["Text"])

        if  'bye' in result.text:
            a=0
        else:
            a=1
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))