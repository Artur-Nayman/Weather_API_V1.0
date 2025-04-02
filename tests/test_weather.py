from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_weather():
    response = client.get("/weather?city=London")
    assert response.status_code == 200
    assert "temperature" in response.json()
    assert "weather" in response.json()
    assert "humidity" in response.json()
    assert "wind_speed" in response.json()
