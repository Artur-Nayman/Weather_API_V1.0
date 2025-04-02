from fastapi import FastAPI
import requests
import redis
import json
from datetime import timedelta

app = FastAPI()

# OpenWeather API key (replace with your actual API key)
API_KEY = "8ae25b1f361fa0f7543c15b1ab1fc643"

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


@app.get("/weather")
def get_weather(city: str):
    try:
        # Check if data exists in cache
        cached_weather = cache.get(city)
        if cached_weather:
            print(f"Using cached data for {city}")
            return json.loads(cached_weather)

        # If not in cache, fetch data from OpenWeather API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Construct the response
            weather_info = {
                "city": city,
                "temperature": temperature,
                "weather": weather_description,
                "humidity": humidity,
                "wind_speed": wind_speed
            }

            # Store the data in cache for 10 minutes
            cache.setex(city, timedelta(minutes=10), json.dumps(weather_info))
            return weather_info
        else:
            return {"error": f"Failed to retrieve data for {city}. API error: {response.status_code}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}