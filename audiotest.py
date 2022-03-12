import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
#recognize_bing() : Microsoft Bing Speech

#recognize_google() : Google Web Speech

#recognize_google_cloud() : Google Cloud Speech

#recognize_houndify() : Houndify Speech

#recognize_ibm() : IMB Speech

#recognize_wit() : Wit.ai Speech
