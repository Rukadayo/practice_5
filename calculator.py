import streamlit as st

# 앱 제목 설정
st.title("📱 디지털 계산기 (수정版)")

# st.session_state 초기화
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# 계산기 화면(Display) 부분
st.text_input("계산식", value=st.session_state.expression, disabled=True, label_visibility="collapsed")


# 버튼 레이아웃 구성
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", use_container_width=True):
        st.session_state.expression += "7"
        st.rerun() # 스크립트를 다시 실행하여 즉시 반영
    if st.button("4", use_container_width=True):
        st.session_state.expression += "4"
        st.rerun()
    if st.button("1", use_container_width=True):
        st.session_state.expression += "1"
        st.rerun()
    if st.button("0", use_container_width=True):
        st.session_state.expression += "0"
        st.rerun()

with col2:
    if st.button("8", use_container_width=True):
        st.session_state.expression += "8"
        st.rerun()
    if st.button("5", use_container_width=True):
        st.session_state.expression += "5"
        st.rerun()
    if st.button("2", use_container_width=True):
        st.session_state.expression += "2"
        st.rerun()
    if st.button("C", use_container_width=True): # Clear 버튼
        st.session_state.expression = ""
        st.rerun()

with col3:
    if st.button("9", use_container_width=True):
        st.session_state.expression += "9"
        st.rerun()
    if st.button("6", use_container_width=True):
        st.session_state.expression += "6"
        st.rerun()
    if st.button("3", use_container_width=True):
        st.session_state.expression += "3"
        st.rerun()
    if st.button("=", use_container_width=True): # Equals 버튼
        try:
            result = eval(st.session_state.expression)
            st.session_state.expression = str(result)
            st.rerun()
        except Exception as e:
            st.session_state.expression = "Error"
            st.rerun()

with col4:
    if st.button("÷", use_container_width=True):
        st.session_state.expression += "/"
        st.rerun()
    if st.button("×", use_container_width=True):
        st.session_state.expression += "*"
        st.rerun()
    if st.button("-", use_container_width=True):
        st.session_state.expression += "-"
        st.rerun()
    if st.button("+", use_container_width=True):
        st.session_state.expression += "+"
        st.rerun()