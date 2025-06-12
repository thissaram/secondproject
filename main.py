import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="🎬 드라마 추천 페이지", page_icon="🎥", layout="centered")

# CSS로 간단히 꾸미기 (화려하게 보이도록 배경, 글씨, 카드 스타일)
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }
    .subtitle {
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
    }
    .card {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 25px rgba(255, 255, 255, 0.45);
    }
    .drama-title {
        font-size: 1.3rem;
        font-weight: 700;
    }
    .drama-desc {
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 제목 및 부제목
st.markdown('<div class="title">🎭 장르별 드라마 추천</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 취향에 맞는 최고의 드라마를 찾아보세요!</div>', unsafe_allow_html=True)

# 장르 선택지
genre = st.selectbox("장르를 선택하세요:", ["로맨스", "스릴러", "코미디", "판타지", "범죄"])

# 장르별 드라마 데이터 (샘플)
drama_data = {
    "로맨스": [
        {"title": "이태원 클라쓰", "desc": "열정과 사랑이 어우러진 청춘 이야기."},
        {"title": "도깨비", "desc": "불멸의 사랑을 그린 판타지 로맨스."},
        {"title": "별에서 온 그대", "desc": "외계인과 인간의 사랑 이야기."}
    ],
    "스릴러": [
        {"title": "비밀의 숲", "desc": "부패를 파헤치는 검사와 형사의 이야기."},
        {"title": "킹덤", "desc": "좀비와 정치 음모가 얽힌 사극 스릴러."},
        {"title": "시그널", "desc": "과거와 현재를 잇는 무전기의 미스터리."}
    ],
    "코미디": [
        {"title": "응답하라 1988", "desc": "가족과 친구들의 따뜻한 이야기."},
        {"title": "내 아이디는 강남미인", "desc": "성장과 웃음을 담은 캠퍼스 코미디."},
        {"title": "별에서 온 그대", "desc": "로맨스와 코믹이 어우러진 작품."}
    ],
    "판타지": [
        {"title": "호텔 델루나", "desc": "귀신과 인간이 공존하는 환상적인 이야기."},
        {"title": "도깨비", "desc": "불멸의 사랑을 그린 판타지 로맨스."},
        {"title": "알함브라 궁전의 추억", "desc": "증강현실 게임과 현실의 경계."}
    ],
    "범죄": [
        {"title": "나의 아저씨", "desc": "인생의 무게를 견디는 사람들의 이야기."},
        {"title": "보이스", "desc": "긴박한 범죄와 구조의 현장."},
        {"title": "비밀의 숲", "desc": "부패를 파헤치는 검사와 형사의 이야기."}
    ]
}

# 선택된 장르의 드라마 출력
st.markdown(f"### {genre} 장르 추천 드라마")

cols = st.columns(3)
for i, drama in enumerate(drama_data[genre]):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <div class="drama-title">🎬 {drama['title']}</div>
            <div class="drama-desc">{drama['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
