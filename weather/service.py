import requests

API_KEY = "8ae25b1f361fa0f7543c15b1ab1fc643"

def get_weather(city: str):
    try:
        # Request to OpenWeather API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Prepare the response
            weather_info = {
                "city": city,
                "temperature": temperature,
                "weather": weather_description,
                "humidity": humidity,
                "wind_speed": wind_speed
            }

            return weather_info
        else:
            return {"error": f"Failed to retrieve data for {city}. API error: {response.status_code}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
