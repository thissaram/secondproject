# streamlit_app.py
import streamlit as st
import requests
from PIL import Image
from datetime import datetime

# ----------- 설정 ------------
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # https://openweathermap.org/ 에서 발급
CITY = "Seoul"
UNITS = "metric"
LANG = "kr"
# ------------------------------

# ----- 날씨 정보 가져오기 -----
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={UNITS}&lang={LANG}"
    res = requests.get(url).json()
    return {
        "temp": res["main"]["temp"],
        "weather": res["weather"][0]["main"],
        "description": res["weather"][0]["description"]
    }

# ----- 빵 추천 로직 -----
def recommend_bread(weather):
    if weather == "Rain":
        return "크루아상", "비 오는 날엔 버터 향 가득한 크루아상이 최고죠 ☔", "https://cdn.pixabay.com/photo/2020/03/20/21/04/croissant-4951889_1280.jpg"
    elif weather == "Clear":
        return "소금빵", "맑고 청명한 날엔 담백한 소금빵! 🌞", "https://cdn.pixabay.com/photo/2022/04/06/13/57/bread-7113774_1280.jpg"
    elif weather == "Clouds":
        return "앙버터", "구름 낀 날엔 달콤하고 고소한 앙버터 어때요? ☁️", "https://cdn.pixabay.com/photo/2021/05/03/16/20/bread-6225786_1280.jpg"
    elif weather == "Snow":
        return "시나몬롤",
