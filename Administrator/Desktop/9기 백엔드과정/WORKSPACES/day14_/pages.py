import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


data =load_data()
data[:200]
def home():
    st.title("Home")
def period():
    st.title("시기별")
def age():
    st.title("연령별")
def sido():
    st.title("지역별")
    # 데이터 구성

    # tmp.AGE_GROUP=tmp.AGE_GROUP.astype('int)
    titles = ['OpenStreetMap', 'CartoDB positron', 'CartoDB dark_matter']
    with st.sidebar:
        st.divider()
        t = st.sidebar.radio('Map', titles)
        col = st.selectbox('분석  컬럼 선택',)
    