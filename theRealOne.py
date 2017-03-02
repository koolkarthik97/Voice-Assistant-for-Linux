from piwho import recognition,vad
import sys
import os
import speech_recognition as sr
import pynotify
import time
context=""


def alert(msg):
    pynotify.init("mpd-notify")
    notice = pynotify.Notification('Terminal Response : ', msg)
    notice.show()
    return


def find_speaker():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
	os.system("beep")
        print("Speaker needs to be identified. Say something..")
        audio = r.listen(source)
	s="results.wav"
	with open(s, "wb") as f:
    		f.write(audio.get_wav_data())    
    recog = recognition.SpeakerRecognizer()
    name = []
    name = recog.identify_speaker('results.wav')
    dictn=recog.get_speaker_scores()
    i = float(dictn.get(name[0]))
    #print("Voice close to "+name[0])
    if(i>0.55):
	print("Voice not secure enough to proceed")
	os.system("streamer -f jpeg -o INTRUDER.jpeg")
	os.system("espeak -s 150 'Intruder alert , Intruder alert , Intruder alert .'")
	exit(0)
    
    alert("Hello there !!")
  




def call_bing():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
	os.system("beep")
        #os.system("espeak -s 150 -v en+f4 'What is your command ?'")
        audio = r.listen(source)
	s="results.wav"
	with open(s, "wb") as f:
    		f.write(audio.get_wav_data())
        os.system("espeak -s 150 -v en+f4 'Waiting for response from bing.'")
    BING_KEY = "d6d1d65306e845d5bb14fdaf4944755c" # Microsoft Bing Voice Recognition
    try:
        var1=r.recognize_bing(audio, key=BING_KEY)
        print("Microsoft Bing Voice Recognition thinks you said " + var1)
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
	var1 = ""
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
	var1=""
    return var1

def get_commands(var):
	if(var=="chrome"): #cmds for chrome
		while(True):
			#os.system("beep")			
			cmd = call_bing()
			if(cmd=="time"):
				alert(time.ctime())
			if("esktop" in cmd):
				os.system("xdotool key super+d")
				return
			f = open("chrome_cmds.txt","r")
			for line in f:
				command = line.split(":")
				if(command[0] == cmd):
					os.system(command[1])
					if(command[0]=="switch to document editor"):
						context="gedit"
						get_commands(context)
				if(cmd == "exit chrome"):
					os.system("xdotool key alt+F4")
					return;
			f.close()


	if(var=="music"): #cmds for VLC
		while(True):
			#os.system("beep")			
			cmd = call_bing()
			if(cmd=="time"):
				alert(time.ctime())
			if("esktop" in cmd):
				os.system("xdotool key super+d")
				return
			f = open("music_cmds.txt","r")
			for line in f:
				command = line.split(":")
				if(command[0] == cmd):
					os.system(command[1])
					if(command[0]=="switch to document editor"):
						context="gedit"
						get_commands(context)
				if(cmd == "exit player"):
					os.system("xdotool key alt+F4 && sleep 2 && xdotool type exit && xdotool key Return")
					return;
			f.close()
		
	if(var=="gedit"): #cmds for gedit
		while(True):
			#os.system("beep")
			cmd = call_bing()
			if(cmd=="time"):
				alert(time.ctime())

			if("esktop" in cmd):
				os.system("xdotool key super+d")
				return
			if(cmd=="enter"):
				text=call_bing()
				temp = "xdotool type "+text
				os.system(temp)
				continue
			if(cmd=="save"):
				os.system("xdotool key ctrl+s")
				time.sleep(1)
				os.system("xdotool key BackSpace")
				name=call_bing();
				os.system("xdotool type "+name)
				time.sleep(1)
				os.system("xdotool key Return")		
			f = open("gedit_cmds.txt","r")
			for line in f:
				command = line.split(":")
				if(command[0] == cmd):
					os.system(command[1])
					if(command[0]=="switch to chrome"):
						context="chrome"
						get_commands(context)
				
				if(cmd == "exit editor"):
					os.system("xdotool key alt+F4")
					return;
		f.close()

	if(var=="terminal"): #cmds for terminal
		while(True):
			#os.system("beep")			
			cmd = call_bing()
			if(cmd=="time"):
				alert(time.ctime())
			if("desktop" in cmd):
				os.system("xdotool key super+d")
				return
			f = open("terminal_cmds.txt","r")
			for line in f:
				command = line.split(":")
				if(command[0] == cmd):
					os.system(command[1])
					if(command[0]=="switch to document editor"):
						context="gedit"
						get_commands(context)
					if(command[0]=="switch to chrome"):
						context="chrome"
						get_commands(context)
				if(cmd == "create directory"):
					d=call_bing()
					if(d!=""):
						os.system("mkdir "+d)
				if(cmd == "delete directory"):
					d=call_bing()
					if(d!=""):
						os.system("rmdir "+d)
				if(cmd == "exit terminal"):
					os.system("xdotool key alt+F4")
					return;
			f.close()

	if(var=="nautilus"): #cmnds for nautilus
		while(True):
			cmd=call_bing()
			if(cmd=="time"):
				alert(time.ctime())
			if("desktop" in cmd):
				os.system("xdotool key super+d")
				return
			f = open("nautilus_cmds.txt","r")
			for line in f:
				command = line.split(":")
				if(command[0] == cmd):
					os.system(command[1])
				if(command=="switch to chrome"):
					context="chrome"
					get_commands(context)
					return
				if(command=="switch to edit"):
					context="gedit"
					get_commands(context)
					return
				if(cmd=="exit files"):
					os.system("xdotool key ctrl+q")
					return;
			f.close()



	


#main function
if __name__ == "__main__":
	os.system("espeak -s 150 -v en+f4 'Welcome . Please verify your voice ID'")
	find_speaker()
	os.system("espeak -s 150 -v en+f4 'Successful Login'")			
	while(True):
		os.system("espeak -s 150 -v en+f4 'Main Command please'")
		response = call_bing()
		if("love" in response):
			os.system("espeak -s 150 -v en+f4 'i am not good at love advice .'")
			print("i am not good at love advice .")
		if("best voice assistant" in response):
			os.system("espeak -s 150 -v en+f4 'Hello . What am i then ?'")
			print("Hello . What am i then ?")
		if("sad" in response or "happy" in response or "cry" in response):
			os.system("espeak -s 150 -v en+f4 'i cannot respond to your feeling . But , you can pour it out .'")
			print("i cannot respond to your feeling . But , you can pour it out .")
		if("joke" in response):
			os.system("espeak -s 150 -v en+f4 'Go look in a mirror .'")
			print("Go look in a mirror .")
		if("world" in response and "end" in response):
			os.system("espeak -s 150 -v en+f4 'January , 2038 . Unix runs out then .'")
			print("January 2038 . Unix runs out then .")
		
		if("life" in response):
			os.system("espeak -s 150 -v en+f4 'Seems funny .'")
			print("Funny .")
			
		if("chrome" in response):
			os.system("google-chrome &")
			context="chrome"		
			get_commands(context)

		if("document" in response):
			os.system("gedit &")
			context="gedit"
			os.system("xdotool click 1")
			time.sleep(1)		
			get_commands(context)

		if("desktop" in response):
				os.system("xdotool key super+d")

		if("terminal" in response):
			os.system("xdotool key ctrl+alt+t &")
			context="terminal"		
			get_commands(context)

		if("music" in response):
			os.system("xdotool key ctrl+alt+t && sleep 2 && xdotool type vlc && xdotool key Return")
			context="music"		
			get_commands(context)

		if("file" in response):
			os.system("nautilus &")
			context="nautilus"		
			get_commands(context)
		
		if("picture" in response):
			os.system("espeak -s 150 -v en+f4 'Say cheese .'")
			os.system("guvcview &")
			time.sleep(3)
			os.system("xdotool key i")
			time.sleep(2)
			os.system("xdotool key alt+F4")	

		if("google" in response):
			os.system("google-chrome www.google.com &")
			os.system("xdotool keydown ctrl+shift+period")
			os.system("sleep 3")
			os.system("xdotool keyup ctrl+shift+period")
			get_commands("chrome")
		
		
		if("android" in response or "phone" in response or "offline" in response):
			os.system("espeak -s 150 -v en+f4 'Open mobile application and run it .'")
			time.sleep(1)
			os.system("xdotool key ctrl+shift+n &")
			time.sleep(2)
			os.system("xdotool type 'python Offline.py 192.168.43.28' && xdotool key Return")
		
		if("stop" in response):
			break;    
	os.system("espeak -s 150 -v en+f4 'Have a good day !'")	
	print("Thanks for using OAK assistant")
