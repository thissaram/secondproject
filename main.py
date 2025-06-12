import streamlit as st

from PIL import Image

# 빵 추천 데이터 (날씨별)
bread_recommendations = {
    "맑음": ["크루아상", "바게트", "식빵"],
    "비": ["브라우니", "초코빵", "카스텔라"],
    "눈": ["단팥빵", "치즈빵", "호두파이"],
    "흐림": ["모카빵", "시나몬롤", "베이글"],
    "바람": ["베이글", "호밀빵", "머핀"]
}

# 날씨에 맞는 이미지 URL (인터넷에서 퍼온 무료 아이콘 예)
weather_icons = {
    "맑음": "https://cdn-icons-png.flaticon.com/512/869/869869.png",
    "비": "https://cdn-icons-png.flaticon.com/512/414/414974.png",
    "눈": "https://cdn-icons-png.flaticon.com/512/642/642102.png",
    "흐림": "https://cdn-icons-png.flaticon.com/512/414/414927.png",
    "바람": "https://cdn-icons-png.flaticon.com/512/414/414974.png"
}

st.set_page_config(page_title="날씨별 빵 추천", page_icon="🥐", layout="centered")

st.markdown("""
    <style>
    .title {
        font-size: 48px;
        color: #FF6347;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .subtitle {
        font-size: 20px;
        color: #555;
        text-align: center;
        margin-bottom: 40px;
    }
    .recommendation {
        font-size: 28px;
        color: #008080;
        font-weight: 600;
        text-align: center;
        margin-top: 30px;
        font-family: 'Georgia', serif;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌤️ 오늘 날씨에 딱 맞는 빵 추천! 🥖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 오늘 날씨를 선택해 주세요!</div>', unsafe_allow_html=True)

weather = st.selectbox("날씨를 선택하세요:", options=["맑음", "비", "눈", "흐림", "바람"])

# 날씨 아이콘 보여주기
icon_url = weather_icons.get(weather)
if icon_url:
    st.image(icon_url, width=100)

# 추천 빵 리스트 출력
recommendations = bread_recommendations.get(weather, [])
if recommendations:
    st.markdown('<div class="recommendation">추천 빵:</div>', unsafe_allow_html=True)
    for bread in recommendations:
        st.markdown(f"- {bread}")

# 하단에 귀여운 배경 효과
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4e1 100%);
        animation: bgAnimation 20s ease infinite;
    }
    @keyframes bgAnimation {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
""", unsafe_allow_html=True)
