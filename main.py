from fastapi import FastAPI
from weather.service import get_weather

app = FastAPI()

@app.get("/weather")
def weather(city: str):
    return get_weather(city)
