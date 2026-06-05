import streamlit as st

# 앱 제목 설정
st.title("🎡 놀이기구 탑승 가능 여부 확인기")
st.write("아이의 키를 입력하면 탑승 가능 여부를 알려드립니다.")

# 1. 키 입력 받기 (기본값: 120, 최소: 0, 최대: 250, 1단위 조절)
height = st.number_input("키를 입력하세요 (cm):", min_value=0, max_value=250, value=120, step=1)

# 분리선
st.divider()

# 2. 조건문 및 결과 출력
if height < 100:
    st.error("🚨 탑승 불가 (100cm 미만)")
elif 100 <= height < 130:
    st.warning("👨‍👩‍👦 보호자 동행 시 탑승 가능")
elif 130 <= height < 195:
    st.success("✅ 탑승 가능")
else:
    st.error("🚨 탑승 불가 (195cm 이상)")