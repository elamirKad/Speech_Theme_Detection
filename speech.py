import speech_recognition as sr
countI = 0
r = sr.Recognizer()
m = sr.Microphone()
while (True):
	if(input("")==""):
		while True:
			
			try:
			    print("A moment of silence, please...")
			    with m as source:
			        r.adjust_for_ambient_noise(source)
			    print("Set minimum energy threshold to {}".format(r.energy_threshold))
			    print("Say...\n")
			    with m as source:
			        audio = r.listen(source)
			    print("Got it! Now to recognize it...")
			    try:
			    	statement = r.recognize_google(audio, language="ru_RU")
			    	print("You said {}".format(statement))
			    	countI = 0
			    except:
			    	print("Ooops")
			    	countI += 1
			    if countI >= 4:
			    	break
			except:
				print("some problems")