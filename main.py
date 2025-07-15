import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

st.title("⚖️ 질량중심 시뮬레이션 (한글 확인용)")

# 폰트 경로 설정
font_path = "NanumGothic.ttf"

# 현재 폴더 파일 확인
st.subheader("📂 현재 폴더 파일 목록:")
st.write(os.listdir())

# 폰트 적용
try:
    fontprop = fm.FontProperties(fname=font_path)
    plt.rc('font', family=fontprop.get_name())
    plt.rcParams['axes.unicode_minus'] = False

    # 테스트 그래프
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [3, 5, 2])
    ax.set_title("🌟 질량에 따른 중심의 이동")
    ax.set_xlabel("시간")
    ax.set_ylabel("위치")
    st.pyplot(fig)

except Exception as e:
    st.error(f"❌ 폰트 로딩 실패: {e}")
# 제목
st.title("⚖️ 질량중심법칙 시뮬레이션")

st.markdown("""
두 물체가 서로 끌어당기며 공전할 때, 그 중심은 어디일까요?
질량에 따라 **질량중심**이 어떻게 바뀌는지 시각화해보세요!
""")

# 슬라이더: 두 물체의 질량 조절
mass1 = st.slider("물체 A의 질량 (kg)", 1, 100, 50)
mass2 = st.slider("물체 B의 질량 (kg)", 1, 100, 50)

# 기준 거리 설정 (두 물체 간 거리)
distance = 10  # 예: 10m 떨어져 있음

# 질량중심 계산
center_from_mass1 = (mass2 / (mass1 + mass2)) * distance
center_from_mass2 = distance - center_from_mass1

# 좌표 설정
pos1 = 0
pos2 = distance
barycenter = pos1 + center_from_mass1

# 시각화
fig, ax = plt.subplots(figsize=(8, 2))
ax.plot([pos1, pos2], [0, 0], 'ko', markersize=15)
ax.plot(barycenter, 0, 'r*', markersize=20)

ax.text(pos1, 0.1, f"A (질량={mass1}kg)", ha='center')
ax.text(pos2, 0.1, f"B (질량={mass2}kg)", ha='center')
ax.text(barycenter, -0.2, "⚖️ 질량중심", ha='center', color='red')

ax.set_xlim(-2, distance + 2)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("두 물체 사이의 질량중심 위치")
ax.axis('off')
st.pyplot(fig)
