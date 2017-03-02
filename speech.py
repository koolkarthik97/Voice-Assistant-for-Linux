import speech_recognition as sr

from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "turnoff.wav")


r = sr.Recognizer()
#with sr.Microphone(1) as source:                # use the default microphone as the audio source
 #   audio = r.listen(source) 


with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file



#recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "d6d1d65306e845d5bb14fdaf4944755c" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Bing recognition results:")
    print(r.recognize_bing(audio, key=BING_KEY, show_all=True))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
