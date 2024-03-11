import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pages import *


# 상태 저장
if 'page' not in st.session_state:
    st.session_state['page'] = 'HOME'

@st.cache_data
def load_data():
    data = pd.read_csv("data.csv")
    return data
data =load_data()
data[:200]

# with st.sidebar:
#     if st.button("HOME", type='primary', use_container_width=True): st.session_state['page']='HOME'
#     if st.button("시기별"): st.session_state['page'] = 'period'
#     st.button("연도별")
#     st.button("지역별")

# if st.session_state['page']=='HOME':
#     home()
# elif st.session_state['page']=='period':
#     period()

menus = {"HOME":home, "시기별":period, "연령별":age, "지역별":sido}

with st.sidebar:
    for menu in menus.keys():
        if st.button(menu, use_container_width=True, type='primary' if st.session_state['page']==menu else 'secondary'):
            st.session_state['page']=menu
            st.rerun() # 클릭한 곳에 색깔을 입혀야되는 업데이트 코드
    st.title("LIKE LION")

st.sidebar.title("멋사")
for menu in menus.keys():
    if st.session_state['page']== menu:
        menus[menu]()
    