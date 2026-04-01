import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Streamlit 요소 데모", page_icon="🎛️", layout="wide")

st.title("🎨 Streamlit 요소 데모 페이지")
st.write("이 페이지는 Streamlit에서 자주 쓰는 컴포넌트를 한눈에 보여줍니다.")

st.header("1. 텍스트 & 마크다운")
st.markdown("### 마크다운 제목\n- 리스트 항목 1\n- 리스트 항목 2\n\n**굵은 텍스트**와 *기울임 텍스트* 를 보여줍니다.")
st.caption("caption: 추가 설명 텍스트")

st.header("2. 입력 위젯")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("이름 입력", "홍길동")
    bio = st.text_area("소개글", "여기에 소개글을 작성해 보세요.")
    agree = st.checkbox("약관 동의")
    gender = st.radio("성별", ["남성", "여성", "기타"])

with col2:
    age = st.slider("나이", min_value=10, max_value=100, value=25)
    favorite = st.selectbox("좋아하는 색", ["빨강", "파랑", "초록", "노랑"])
    hobbies = st.multiselect("취미 선택", ["독서", "운동", "코딩", "여행"], default=["코딩"])
    birthdate = st.date_input("생년월일", datetime(1990,1,1))

if st.button("입력 결과 보기"):
    st.success("입력 정보가 잘 입력되었습니다!")
    st.write({
        "이름": name,
        "소개": bio,
        "동의": agree,
        "성별": gender,
        "나이": age,
        "좋아하는 색": favorite,
        "취미": hobbies,
        "생년월일": birthdate,
    })

st.header("3. 파일 업로드 / 다운로드")
uploaded = st.file_uploader("파일 업로드", type=["csv", "txt"])
if uploaded:
    st.write("업로드된 파일 이름:", uploaded.name)
    if uploaded.type == "text/csv":
        df = pd.read_csv(uploaded)
        st.dataframe(df.head())

with st.expander("샘플 다운로드"):
    st.markdown("`st.download_button`를 통해 텍스트/바이너리 데이터를 저장할 수 있습니다.")
    st.download_button("샘플 CSV 다운로드", data="a,b,c\n1,2,3", file_name="sample.csv")

st.header("4. 상태 표시기")
progress = st.progress(0)
for i in range(0, 101, 20):
    progress.progress(i)
    st.write(f"진행률 {i}%")

st.metric("오늘 온도", "23°C", "+1.2°C")

st.header("5. 레이아웃 및 컨테이너")
with st.expander("이 확장 영역을 클릭하면 열립니다"):
    st.write("Expander 안의 내용입니다.")

tabs = st.tabs(["탭 1", "탭 2", "탭 3"])
with tabs[0]:
    st.write("탭 1 내용")
with tabs[1]:
    st.line_chart(pd.DataFrame({"x": range(10), "y": [i**2 for i in range(10)]}))
with tabs[2]:
    st.write("탭 3 내용")

st.header("6. 데이터 프레임과 차트")
chart_df = pd.DataFrame({"A": [10, 20, 30], "B": [5, 15, 25]})
st.dataframe(chart_df)
st.bar_chart(chart_df)

st.write("모든 요소를 잘 보고 있으시면 Streamlit 기본 위젯 이해가 완료되었습니다!")
