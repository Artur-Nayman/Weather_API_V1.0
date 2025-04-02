# Weather API Project

This project provides a simple weather API using the FastAPI framework. It retrieves weather data for a given city by querying the OpenWeather API and returns essential weather details such as temperature, weather description, humidity, and wind speed.

## Features

- Fetch current weather data for any city.
- Caching of weather data to reduce API calls and improve response time.
- Built with FastAPI for high performance.
- Simple error handling for failed requests.

## Technologies Used

- **FastAPI**: Framework for building the API.
- **requests**: Python library for making HTTP requests to the OpenWeather API.
- **OpenWeather API**: External service to fetch weather data.
- **Redis** (Optional): Used for caching weather data for 10 minutes to optimize repeated queries (can be removed if not needed).

## Installation
Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-api.git
   ```
Navigate to the project folder:
  ```bash
  cd weather-api
  ```
Create and activate a virtual environment (recommended):
  ```bash
  python -m venv venv
  # On Windows:
  venv\Scripts\activate
  # On macOS/Linux:
  source venv/bin/activate
  ```
Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
The server will start at http://127.0.0.1:8000

## Running the API

  ```bash
  uvicorn main:app --reload
  ```
## Endpoints
GET /weather: Retrieve current weather for a given city.
## Query Parameters:
city (string): The name of the city to fetch weather data for (e.g., London, New York).

Example request:

  ```bash
GET http://127.0.0.1:8000/weather?city=London
  ```

  ```json
{
  "city": "London",
  "temperature": 15.5,
  "weather": "clear sky",
  "humidity": 78,
  "wind_speed": 3.2
}

  ```
## Error Handling
If an error occurs while fetching weather data, the API will return a JSON response with an error message. Example:

```json
{
  "error": "Failed to retrieve data for London. API error: 401"
}
```

