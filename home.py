import streamlit as st

st.set_page_config(page_title="変電Webアプリ", page_icon="📱", layout="centered")

st.title("たぬきツール")
st.write("X, IRIAM, Discordに使えるWebアプリ集です。サイドバーから機能を選択できます。")

center_align_html = """
<div style='text-align: center; color: gray; font-size: 16px;'>
  <br>
  <br>
  <p>© 2025 たたたぬき</p>
</div>
"""
st.markdown(center_align_html, unsafe_allow_html=True)
