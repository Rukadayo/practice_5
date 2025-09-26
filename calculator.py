import streamlit as st

# 앱 제목 설정
st.title("📱 디지털 계산기")

# st.session_state 초기화
# 'expression' 키가 세션 상태에 없으면 빈 문자열로 초기화합니다.
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# 계산기 화면(Display) 부분
# disabled=True로 설정하여 사용자가 직접 입력하는 것을 막고, 값만 보여주는 용도로 사용합니다.
st.text_input("계산식", value=st.session_state.expression, disabled=True, label_visibility="collapsed")


# 버튼 레이아웃 구성
# st.columns를 사용하여 버튼을 가로로 배열합니다.
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", use_container_width=True):
        st.session_state.expression += "7"
    if st.button("4", use_container_width=True):
        st.session_state.expression += "4"
    if st.button("1", use_container_width=True):
        st.session_state.expression += "1"
    if st.button("0", use_container_width=True):
        st.session_state.expression += "0"

with col2:
    if st.button("8", use_container_width=True):
        st.session_state.expression += "8"
    if st.button("5", use_container_width=True):
        st.session_state.expression += "5"
    if st.button("2", use_container_width=True):
        st.session_state.expression += "2"
    if st.button("C", use_container_width=True): # Clear 버튼
        st.session_state.expression = ""

with col3:
    if st.button("9", use_container_width=True):
        st.session_state.expression += "9"
    if st.button("6", use_container_width=True):
        st.session_state.expression += "6"
    if st.button("3", use_container_width=True):
        st.session_state.expression += "3"
    if st.button("=", use_container_width=True): # Equals 버튼
        try:
            # eval 함수로 문자열 형태의 수식을 계산합니다.
            result = eval(st.session_state.expression)
            st.session_state.expression = str(result)
        except Exception as e:
            st.session_state.expression = "Error"

with col4:
    if st.button("÷", use_container_width=True):
        st.session_state.expression += "/"
    if st.button("×", use_container_width=True):
        st.session_state.expression += "*"
    if st.button("-", use_container_width=True):
        st.session_state.expression += "-"
    if st.button("+", use_container_width=True):
        st.session_state.expression += "+"