import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key securely
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city="Mumbai"):
    
    if not WEATHER_API_KEY:
        return "Weather service is not configured properly"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "Sorry, I could not fetch the weather right now"

        data = response.json()
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        return (
            f"The weather in {city} is "
            f"{temperature} degrees Celsius with {condition}"
        )

    except requests.exceptions.RequestException:
        return "Network error while fetching weather"
