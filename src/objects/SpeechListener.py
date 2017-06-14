#!/usr/bin/env python3

import speech_recognition as sr

class SpeechListener:
    def __init__(self, base):
        self.base = base

    def listen(self):
        # obtain audio from the microphone
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = rec.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio,
            # key="GOOGLE_SPEECH_RECOGNITION_API_KEY")` instead of `r.recognize_google(audio)`
            msg = rec.recognize_google(audio)
            self.base.log("heard: "+ msg)
        except sr.UnknownValueError:
            self.base.err_log("Google Speech Recognition could not understand audio")
        except sr.RequestError as err:
            self.base.err_log("Could not request results from Google Speech Recognition " \
                              "service; {0}".format(err))
        return msg
