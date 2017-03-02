from piwho import recognition,vad
import sys
import os
import speech_recognition as sr
import pynotify
import socket
import time
context=""
result=""

def call_android():
	HOST = sys.argv[1]   # Symbolic name, meaning all available interfaces
	PORT = 8888 #arbitrary non-privileged port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#print ('Socket created')
 
	#Bind socket to local host and port
	try:
		s.bind((HOST, PORT))
	except socket.error as msg:
		print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
		sys.exit()
     
	#print ('Socket bind complete')
 
	#Start listening on socket
	s.listen(10)
	os.system("espeak -s 150 -v en+f4 'android now listening'")
	#now keep talking with the client
	while 1:
	#wait to accept a connection - blocking call
		conn, addr = s.accept()
		#print ('Connected with ' + addr[0] + ':' + str(addr[1]))
		buf=conn.recv(64)
		result=buf.decode("utf-8")
		if result:
			print(result)
			break
	s.close()
	return result


def find_speaker():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        os.system("aplay beep.wav")
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
    if(i>0.65):
        print("Voice not secure enough to proceed")
        os.system("streamer -f jpeg -o INTRUDER.jpeg")
        os.system("espeak -s 150 'Intruder alert .'")
        exit(0)
    #print("Voice close to "+name[0])

def get_commands(var):
	if(var=="chrome"): #cmds for chrome
		while(True):
			#os.system("aplay beep.wav")			
			cmd = call_android()
			if("exit" in cmd):
					os.system("xdotool key alt+F4")
					return;
			f = open("chrome_cmds.txt","r")
			for line in f:
				command = line.split(":")
				if(command[0] == cmd):
					os.system(command[1])
					if(command[0]=="switch to document editor"):
						context="gedit"
						get_commands(context)
				
			f.close()


	if(var=="music"): #cmds for VLC
		while(True):
			#os.system("aplay beep.wav")			
			cmd = call_android()
			if(cmd=="show desktop"):
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
			#os.system("aplay beep.wav")
			cmd = call_android()
			if(cmd=="show desktop"):
				os.system("xdotool key super+d")
				return
			if(cmd=="enter"):
				text=call_android()
				temp = "xdotool type "+text
				os.system(temp)
				continue
			if(cmd=="save"):
				os.system("xdotool key ctrl+s")
				time.sleep(1)
				os.system("xdotool key BackSpace")
				name=call_android();
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
			cmd = call_android()
			if(cmd=="show desktop"):
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
					d=call_android()
					if(d!=""):
						os.system("mkdir "+d)
				if(cmd == "delete directory"):
					d=call_android()
					if(d!=""):
						os.system("rmdir "+d)
				if(cmd == "exit terminal"):
					os.system("xdotool key alt+F4")
					return;
			f.close()

	if(var=="nautilus"): #cmnds for nautilus
		while(True):
			cmd=call_android()
			if(cmd=="show desktop"):
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
	#os.system("espeak -s 150 -v en+f4 'Welcome . Please verify your voice ID'")
	#find_speaker()
	#os.system("espeak -s 150 -v en+f4 'Successful Login'")			
	while(True):
		os.system("espeak -s 150 -v en+f4 'Main Command please'")
		response = call_android()
		print(response)
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
			os.system("cheese &")
			time.sleep(3)
			os.system("xdotool key space")
			time.sleep(5)
			os.system("xdotool key alt+F4")	

		if("google" in response):
			os.system("google-chrome www.google.com &")
			os.system("xdotool keydown ctrl+shift+period")
			os.system("sleep 3")
			os.system("xdotool keyup ctrl+shift+period")
			get_commands("chrome")
		
		
		if(response == "stop listening"):
			break;    
		
	print("Thanks for using OAK")
