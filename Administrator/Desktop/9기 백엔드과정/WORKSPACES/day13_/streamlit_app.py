import streamlit as st

st.write("Hello, *World* :sunglasses:")

import streamlit as st
import pandas as pd

st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

import time
import numpy as np
import pandas as pd
import streamlit as st

_LOREM_IPSUM = """
MVP 개발 계획
이에, 우리는 아이디어의 우수성을 직접 보여줄 수 있는 최소 기능 제품(MVP: Minimal Value Product)을 개발하기로 했습니다. MVP는 우리 아이디어의 핵심 가치를 담으면서도, 개발에 소요되는 시간과 자원은 최소화하는 방향으로 설계될 것입니다. 이를 통해, 실제 작동하는 제품을 통해 아이디어를 시연함으로써 경영진에게 강력한 인상을 남기고자 합니다.

MVP 개발을 위한 도구 선택: Streamlit
MVP 개발을 위해, 우리는 Streamlit을 선택했습니다. Streamlit은 파이썬을 사용하여 데이터 애플리케이션을 신속하게 제작할 수 있게 해주는 오픈 소스 라이브러리입니다. 개발자로서 우리에게 익숙한 언어를 사용함으로써, 짧은 시간 내에 안정적이면서도 인상적인 MVP를 개발할 수 있을 것으로 기대됩니다.

MVP 개발의 주요 목표
핵심 기능 구현: 아이디어의 가치를 명확하게 전달할 수 있는 핵심 기능에 초점을 맞춥니다.
사용자 경험 중심 설계: 직관적이고 사용하기 쉬운 인터페이스를 통해 누구나 쉽게 아이디어의 가치를 이해할 수 있도록 합니다.
빠른 프로토타이핑: Streamlit을 활용하여 개발 기간을 단축시키고, 공모전 제출 기한 내에 MVP를 완성합니다.
기대 효과
MVP를 통해 경영진에게 우리 아이디어의 실제 가치와 시장에서의 잠재력을 보여줄 수 있을 것으로 기대됩니다. 이는 단순한 아이디어 제안을 넘어서, 회사의 비즈니스 전략에 실질적인 기여를 할 수 있는 기회를 마련해줄 것입니다. 또한, MVP의 성공적인 시연은 팀원들의 기술력과 혁신적 사고를 회사 내외적으로 입증하는 계기가 될 것입니다.
"""


def stream_data():
    for word in _LOREM_IPSUM.split():
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split():
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)


# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

# 마크다운
import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# 
import streamlit as st

st.metric(label="Temperature", value="70 °F", delta="1.2 °F") # 음수도 가능


# 버튼
import streamlit as st
# count = 1
# st.button("Reset", type="primary")
st.button("Reset", type="secondary", use_container_width=True)
if st.button('Say hello'):
    st.write('Why hello there')
    # count +=1
    # count  # 원하는 대로 숫자가 안올라갈 수 있다 주의해서 사용 
else:
    st.write('Goodbye')

# textinput
import streamlit as st

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


# status management
# 초기값 설정 후 안쓰임 겉으로보이지 않는 값 설정 시
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'