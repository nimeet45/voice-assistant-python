import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()