from piwho import recognition
from piwho import vad
import speech_recognition as sr

def find_speaker():
    recog = recognition.SpeakerRecognizer()

    # Record voice until silence is detected.
    # save WAV file
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
    vad.record()
    # use newly recorded file.
    name = []
    name = recog.identify_speaker()
    dictn=recog.get_speaker_scores()
    print (dictn)
    return name

if __name__ == "__main__":
    speaker = find_speaker()	
    print(speaker[0])
