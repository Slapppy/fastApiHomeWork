from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class WeatherRequest(BaseModel):
    city: str


@app.get('/weather')
async def get_weather(city: str):
    url = f'https://api.weatherapi.com/v1/current.json'
    params = {
        'key': '0b6ab88564bc4cbc9b4130025230405',
        'q': city,
        'lang': 'en'
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    data = response.json()
    return {
        'city': data['location']['name'],
        'temperature': data['current']['temp_c'],
        'humidity': data['current']['humidity'],
        'description': data['current']['condition']['text']
    }
