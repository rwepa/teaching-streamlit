"""
File     : hello_streamlit\app.py
Title    : first streamlit app based R-shiny "01_hello"
Date     : 2023.01.07
Author   : Ming-Chang Lee
RWEPA    : http://rwepa.blogspot.tw/
YouTube  : https://www.youtube.com/@alan9956
Email    : alan9956@gmail.com
GitHub   : https://github.com/rwepa
Encoding : UTF-8
"""

# streamlit 執行方式
# 考慮建立 D:\streamlitdata\hello_streamlit\app.py
# 命令提示字元
# d:
# cd streamlitdata\hello_streamlit
# streamlit run app.py
# http://localhost:8501/

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

urls = 'https://raw.githubusercontent.com/rwepa/DataDemo/master/faithful.csv'

df = pd.read_csv(urls)
data = df['waiting']
st.markdown("""
<style>
.big-font {
    font-size:30px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="big-font">RWEPA | Python - </p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">Hello Streamlit!</p>', unsafe_allow_html=True)
    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        '**Number of bins**',
        1, 50, 30
    )
    st.write("Required packages:")
    st.markdown('+ streamlit', unsafe_allow_html=True)
    st.markdown('+ matplotlib', unsafe_allow_html=True)
    st.markdown('+ pandas', unsafe_allow_html=True)

# 'Bins selected: ', add_slider

fig, ax = plt.subplots()
ax.hist(data, bins=add_slider)
ax.set_xlabel('Waiting time to next eruption (in mins)')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of waiting times')
ax.grid(linewidth=0.6, linestyle="--")

st.pyplot(fig)
# end