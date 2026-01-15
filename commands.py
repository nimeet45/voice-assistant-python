import webbrowser
import datetime
import wikipedia
from modules.weather import get_weather
from modules.custom_commands import handle_custom_command

def process_command(command):
    command = command.lower().strip()

    # ---------- OPEN GOOGLE ----------
    if "open" in command and "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    # ---------- TIME ----------
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    # ---------- WEATHER ----------
    elif "weather" in command:
        return get_weather("Mumbai")

    # ---------- WIKIPEDIA ----------
    elif command.startswith("who is") or "tell me about" in command:
        query = (
            command.replace("who is", "")
            .replace("tell me about", "")
            .strip()
        )

        if not query:
            return "Please say the name again"

        try:
            info = wikipedia.summary(query, sentences=2)
            return info
        except:
            return "Sorry, I could not find information"
        
        # ---------- CUSTOM COMMANDS ----------
    custom_response = handle_custom_command(command)
    if custom_response:
        return custom_response
    
    # ---------- THANK YOU ----------
    elif "thank you" in command or "thanks" in command:
        return "You're welcome"

    # ---------- EXIT ----------
    elif "exit" in command or "quit" in command:
        return "__exit__"

    # ---------- UNKNOWN ----------
    else:
        return "Sorry, I did not understand that command"
