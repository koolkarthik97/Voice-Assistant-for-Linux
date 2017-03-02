from piwho import recognition,vad
import sys
speaker = sys.argv[1]
recog = recognition.SpeakerRecognizer()		
recog.speaker_name = speaker
recog.train_new_data('adharsh/')
print(recog.get_speakers())

