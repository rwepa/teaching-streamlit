# RWEPA | Python - streamlit

## Streamlit 簡介

Streamlit 是一個以 Python 為核心的開源框架，內建常用的網頁操作控制項，讓你可以用很少的程式碼，快速把 Python 腳本變成互動式 Web 應用程式，特別適合：

+ 資料分析與視覺化
+ 機器學習模型展示（ML Demo）
+ AI 應用（如 LLM Chatbot）
+ 企業級儀表板 (Dashboard)
+ 快速原型（Prototype）
+ 建置互動式決策支援系統並協助決策者即時分析售價變動對整體營運的影響
+ 功能與 R 語言的 shiny 套件類似
+ streamlit: A faster way to build and share data apps

**Streamlit Community Cloud (包括免費/付費佈署 Streamlit):**

  https://streamlit.io/cloud

**Anaconda 2025.12-2 以後版本已經包括 Streamlit 模組, 不用額外安裝**

**conda 安裝 streamlit 方法:**

  conda install -c conda-forge streamlit

**pip 安裝 streamlit 方法:**

  pip install streamlit

## 範例1: hello_streamlit 

+ YouTube: https://youtu.be/FW-dl-flLvk

+ 本地端執行方式

考慮建立 D:\streamlitdata\hello_streamlit\app.py

命令提示字元輸入以下內容:

d:

cd streamlitdata\hello_streamlit

streamlit run app.py

![image](https://github.com/rwepa/teaching-streamlit/blob/main/images/hello_streamlit_run.png)

+ 執行成果

執行後將自動開啟瀏覽器或於瀏覽器輸入 http://localhost:8501/

![image](https://github.com/rwepa/teaching-streamlit/blob/main/images/hello_streamlit_result.png)

+ Python程式碼

https://github.com/rwepa/teaching-streamlit/tree/main/hello_streamlit

+ Cloud 佈署成果

  + 佈署時, 須在 app.py 目錄中新增 requirements.txt, 該檔案記錄 app.py 所使用的模組名稱.

  + requirements.txt 範例 [https://github.com/rwepa/teaching-streamlit/blob/main/hello_streamlit/requirements.txt]

  + https://rwepahello.streamlit.app/

## 參考資料

1. Streamlit 官網: https://streamlit.io/
2. shiny for Python (Python 使用 shiny 模組教學): http://rwepa.blogspot.com/2022/10/shiny-for-python.html
3. shiny package 網路應用: http://rwepa.blogspot.com/2013/01/shiny-package.html
