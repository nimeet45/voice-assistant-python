from modules.speech import listen
from modules.text_to_speech import speak
from modules.commands import process_command
import time

speak("Hello, I am your voice assistant. How can I help you?")

while True:
    command = listen()
    if not command:
        continue

    print("Command received:", command)

    response = process_command(command)
    print("Response:", response)

    if response == "__exit__":
        speak("Goodbye")
        time.sleep(1)
        break

    speak(response)
    time.sleep(1)
