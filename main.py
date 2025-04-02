from fastapi import FastAPI
import requests
import redis
import json
from datetime import datetime, timedelta

app = FastAPI()

# API-ключ OpenWeather
API_KEY = "your_actual_openweather_api_key"

# Підключення до Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


@app.get("/weather")
def get_weather(city: str):
    # Перевірка, чи є відповідь у кеші
    cached_weather = cache.get(city)
    if cached_weather:
        print(f"Using cached data for {city}")
        return json.loads(cached_weather)

    # Якщо кешу немає, робимо запит до OpenWeather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Формуємо відповідь
        weather_info = {
            "city": city,
            "temperature": temperature,
            "weather": weather_description,
            "humidity": humidity,
            "wind_speed": wind_speed
        }

        # Кешуємо відповідь в Redis на 10 хвилин
        cache.setex(city, timedelta(minutes=10), json.dumps(weather_info))

        return weather_info
    else:
        return {"error": "City not found or invalid API key."}
