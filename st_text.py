# File     : st_text.py
# Date     : 2026.07.23
# Author   : Ming-Chang Lee
# YouTube  : https://www.youtube.com/@alan9956
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Email    : alan9956@gmail.com

# 匯入 streamlit 模組並使用別名 st
import streamlit as st
 
# 建立標題
st.title("First App", anchor="first_app", help="工具提示")

# 建立文字
st.text("年度銷售報表")

# 建立章節
st.header("業務部門:ALAN")

st.text("本年度受惠於AI、高效能運算(HPC)、智慧型手機、高速運算及車用電子需求持續成長，業務部門成功推動重點客戶量產計畫。年度營收達成率：108%，年成長率：+26%")
# end
