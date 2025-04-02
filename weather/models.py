from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    weather: str
    humidity: int
    wind_speed: float
