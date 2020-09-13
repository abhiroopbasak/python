import pyttsx3
import os
import speech_recognition as sr
import pyaudio

pyttsx3.speak("Hi, This is Edgy, your own application guide. Let me help you with the applications on this computer")

while True:
	pyttsx3.speak("Which application would you like to open:")
	print("Which application would you like to open:")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Start speaking...")
		audio=r.listen(source)
		print("Speech recognized...")
	p=r.recognize_google(audio)
	print(p)

	if("run " in p) or ("open "in p):
		if("not " in p) or ("do not " in p) or ("dont " in p):
			exit()
		else:

			if ("notepad "in p) or ("text edittor"in p):
				pyttsx3.speak("opening notepad") 
				os.system("notepad")
			elif("notepad++"in p):
				pyttsx3.speak("opening Notepad++") 
				os.system("Notepad++")
			elif("wmplayer"in p):
				pyttsx3.speak("opening Windows Media Player") 
				os.system("wmplayer")
			elif("chrome"in p) or ("browser" in p):
				pyttsx3.speak("opening Google Chrome: Your internet browser") 
				os.system("chrome")
			elif("codeblocks"in p):
				pyttsx3.speak("opening Code Blocks: Your C compiler") 
				os.system("codeblocks")
			elif("Mozilla Firefox"in p) or ("mozilla firefox"in p) or ("firefox"in p):
				pyttsx3.speak("opening Mozilla Firefox: Your internet browser") 
				os.system("Mozilla Firefox")
			elif("Access"in p) or ("access"in p):
				pyttsx3.speak("opening Microsoft Access") 
				os.system("MSACCESS")
			elif("Excel"in p) or ("excel"in p):
				pyttsx3.speak("opening Microsoft Excel") 
				os.system("EXCEL")
			elif("Powerpoint"in p) or ("powerpoint"in p):
				pyttsx3.speak("opening Microsoft :Powerpoint") 
				os.system("POWERPNT")
			elif("Word"in p) or ("word"in p):
				pyttsx3.speak("opening Microsoft Word") 
				os.system("WINWORD")
			else:
				print("dont support")
				pyttsx3.speak("Please try again")
	elif("close"in p) or ("stop"in p) or ("exit"in p):
		pyttsx3.speak("Thank you for using me!")
		exit()
	elif("hi "in p) or ("hello"in p) or ("hey"in p):
		pyttsx3.speak("Hello user!! Please let me know which application you want to open.")
	else:
		pyttsx3.speak("I do not understand your command. Please repeat.")