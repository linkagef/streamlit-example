"""
[実行方法] Anaconda Promptで streamlit環境を起動して
streamlit run simple_app.py
コマンドを実行する。
"""


import streamlit as st
import time
# タイトル表示
st.title("簡単な Streamlit アプリ")


# userにテキスト入力をしてもらう
name = st.text_input("あなたの名前を入力してください")


# userにスライダーで入力してもらう
age = st.slider("年齢を選んでください" , 0, 100, 25)


# 結果表示
if name:    # nameという変数がnull出なかったら
    st.write(f"こんにちは、{name}さん！あなたは{age}歳ですね。")
    st.write(f"プラチナにしか見えないですけどｗ")
    with st.spinner("計測中...", show_time=True):
        time.sleep(5)
    st.success("IQ3!w")
    st.button("Rerun")
else:
    st.write(f"上の入力欄に名前を入力してください")


