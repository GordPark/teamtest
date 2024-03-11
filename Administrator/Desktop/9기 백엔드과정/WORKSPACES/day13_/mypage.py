# Streamlit을 이용해서 자신의 소개 페이지를 제작해 봅시다.
# 여러 가지 기능을 이용해 봅시다.
# 소개말, 백엔드 과정을 통해서 이루고 싶은점
# 캡처 - 강의중 채널
# 11:20까지


import time
import numpy as np
import pandas as pd
import streamlit as st

'''
# 안녕하세요 박룡입니다. 마크다운을 적용한 제 페이지입니다
'''
st.markdown(":rainbow[***파이썬***]과 다양한 기능들을 습득하고자 노력하고")
str2 = st.markdown("프로젝트를 통해 실무 경험을 쌓고, 협업과 문제 해결 능력을 향상시키는 것을 목표로 하고 있습니다")
st.markdown("더 나은 개발자가 되고 싶습니다:exclamation:\
            :collision::dizzy: :dash::fire::alien:")


import streamlit as st

code = '''
# 코드기능

lunchgpt = """
GPT-점심메뉴추천
샐러드 바: 신선한 채소와 다양한 토핑으로 구성된 건강하고 가벼운 옵션입니다.
샌드위치: 다양한 재료로 만든 샌드위치는 편리하면서도 영양가 있는 선택입니다.
찜닭: 부드럽고 매콤한 찜닭은 한끼 식사로도 훌륭한 선택입니다.
비빔밥: 다양한 채소와 고기를 곁들여 맛있게 먹을 수 있는 옵션입니다.
"""

def ():
    for word in lunchgpt.split():
        yield word + " "
        time.sleep(0.03)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in lunchgpt.split():
        yield word + " "
        time.sleep(0.03)'''
st.code(code, language='python')

lunchgpt = """
GPT-점심메뉴추천
샐러드 바: 신선한 채소와 다양한 토핑으로 구성된 건강하고 가벼운 옵션입니다.\
샌드위치: 다양한 재료로 만든 샌드위치는 편리하면서도 영양가 있는 선택입니다.\
찜닭: 부드럽고 매콤한 찜닭은 한끼 식사로도 훌륭한 선택입니다.\
비빔밥: 다양한 채소와 고기를 곁들여 맛있게 먹을 수 있는 옵션입니다.
"""

def stream_data():
    for word in lunchgpt.split():
        yield word + " "
        time.sleep(0.03)

    for word in lunchgpt.split():
        yield word + " "
        time.sleep(0.03)

if st.button("Stream data"):
    st.write_stream(stream_data)


import streamlit as st

options = st.multiselect(
    '좋아하는 음식을 선택해주세요',
    ['샐러드', '샌드위치', '찜닭', '비빔밥', '초밥', '타코'],
    ['초밥', '초밥'])

st.write('You selected:', options)

st.image('gray.jpg', caption='gray')


