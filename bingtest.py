#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import os
import speech_recognition as sr
import time
r = sr.Recognizer()
m = sr.Microphone()

def callback(recognizer,audio):
    BING_KEY = "d6d1d65306e845d5bb14fdaf4944755c" # Microsoft Bing Voice Recognition
    try:
        var=r.recognize_bing(audio, key=BING_KEY)
	print("audio listened...")
        print("Microsoft Bing Voice Recognition thinks you said " + var)
        if(var=="open chrome"):
            os.system("google-chrome")
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
    return

def call_bing():
# obtain audio from the microphone
  
  with m as source:
    print ("say something:")
    r.adjust_for_ambient_noise(source)
  stop_listening = r.listen_in_background(m,callback)
  for _ in range(60): time.sleep(0.1)
  stop_listening()

call_bing()
print "returned to main from bing function"
call_bing()
call_bing()




