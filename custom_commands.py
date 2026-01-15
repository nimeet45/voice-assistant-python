import webbrowser

CUSTOM_COMMANDS = {
    "open youtube": lambda: webbrowser.open("https://www.youtube.com"),
    "open gmail": lambda: webbrowser.open("https://mail.google.com"),
    "open linkedin": lambda: webbrowser.open("https://www.linkedin.com"),
    "open twitter": lambda: webbrowser.open("https://twitter.com"),
    "open github": lambda: webbrowser.open("https://github.com"),
    "say hello": lambda: "Hello! Hope you are having a great day"
}

def handle_custom_command(command):
    for key in CUSTOM_COMMANDS:
        if key in command:
            action = CUSTOM_COMMANDS[key]
            result = action()
            if isinstance(result, str):
                return result
            return f"{key.capitalize()} executed"
    return None