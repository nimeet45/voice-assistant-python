from modules.speech import listen
from modules.text_to_speech import speak

speak("Say something")
text = listen()

if text:
    speak("You said " + text)
else:
    speak("Sorry, I could not understand you")
