import streamlit as st

# 앱 제목 설정
st.title("📱 디지털 계산기 ")

# st.session_state 초기화
# 앱이 재실행되어도 'expression' 값을 기억하기 위해 사용합니다.
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# 계산기 화면(Display) 부분
# disabled=True로 사용자의 직접 입력을 막고, label_visibility="collapsed"로 라벨을 숨깁니다.
st.text_input("계산식", value=st.session_state.expression, disabled=True, label_visibility="collapsed")


# 버튼 레이아웃 구성 (4개의 세로 단으로 나눔)
col1, col2, col3, col4 = st.columns(4)

# 1열 버튼 (7, 4, 1, 0)
with col1:
    if st.button("7", use_container_width=True):
        st.session_state.expression += "7"
        st.rerun() # 버튼 클릭 즉시 화면을 새로고침
    if st.button("4", use_container_width=True):
        st.session_state.expression += "4"
        st.rerun()
    if st.button("1", use_container_width=True):
        st.session_state.expression += "1"
        st.rerun()
    if st.button("0", use_container_width=True):
        st.session_state.expression += "0"
        st.rerun()

# 2열 버튼 (8, 5, 2, C)
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

# 3열 버튼 (9, 6, 3, =)
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
            # eval() 함수로 문자열 수식을 계산
            result = eval(st.session_state.expression)
            st.session_state.expression = str(result)
            st.rerun()
        except Exception as e:
            st.session_state.expression = "Error"
            st.rerun()

# 4열 버튼 (연산자)
with col4:
    if st.button("÷", use_container_width=True):
        st.session_state.expression += "/"
        st.rerun()
    if st.button("×", use_container_width=True):
        st.session_state.expression += "*"
        st.rerun()
    # '+'와 '-'는 특수문자로 인식될 수 있어 앞에 '\'를 붙여 일반 문자로 처리
    if st.button("\-", use_container_width=True):
        st.session_state.expression += "-"
        st.rerun()
    if st.button("\+", use_container_width=True):
        st.session_state.expression += "+"
        st.rerun()