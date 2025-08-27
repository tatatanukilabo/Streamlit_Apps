import streamlit as st

st.set_page_config(page_title="たぬきツール", layout="centered")

st.title("たぬきツール")
st.write("X, IRIAM, Discordに使えるWebアプリ集です。サイドバーから各アプリを選択できます。")

# アプリ情報のリスト
apps = [
    {
        "title": "スクショを1枚の画像に並べるアプリ(for X)",
        "description": "複数のスクショ画像（縦横比一定）を指定した列数に並べて1枚の画像に変換するアプリです。余白の背景色指定可能です。",
        "url": "https://tatatanuki-apps.streamlit.app/スクショを1枚の画像に並べるアプリ(for X)"
    },
    {
        "title": "画像の一部を切り抜いて縮小するアプリ(for Discord)",
        "description": "たぬきが書いたちびキャラのイラストの顔周辺を切り抜いてDiscordの絵文字サイズ(128x128px)、スタンプサイズ(320x320px)に変換するアプリです。",
        "url": "https://tatatanuki-apps.streamlit.app/画像の一部を切り抜いて縮小するアプリ(for Discord)"
    },
    {
        "title": "画像を4分割するアプリ(for X)",
        "description": "画像を4分割し、Xで4枚並べたときに元画像だけが見えるように上下(左右)に余白をつけるアプリです。分割画像はZIPファイルにまとめてダウンロードできます。余白の背景色指定可能です。",
        "url": "https://tatatanuki-apps.streamlit.app/画像を4分割するアプリ(for X)"
    },
    {
        "title": "画像を縮小するアプリ(for Discord)",
        "description": "画像をDiscordの絵文字サイズ(128x128px)、スタンプサイズ(320x320px)に縮小するアプリです。元画像の余白除去もできます。",
        "url": "https://tatatanuki-apps.streamlit.app/画像を縮小するアプリ(for Discord)"
    },
    {
        "title": "画像を縮小するアプリ(for IRIAM)",
        "description": "画像をIRIAMの立ち絵サイズ(2000x4000px以内)、ミニキャラサイズ(600x600px以内)に縮小するアプリです。元画像の余白除去もできます。",
        "url": "https://tatatanuki-apps.streamlit.app/画像を縮小するアプリ(for IRIAM)"
    },
]

# 検索バー
search_query = st.text_input("🔍 アプリ名やキーワードで検索", "")

# 検索結果の表示
for app in apps:
    if search_query.lower() in app["title"].lower() or search_query.lower() in app["description"].lower():
        #st.markdown(f"""### 📱 <a href="{app['url']}" target="_self" style="text-decoration: none; color: inherit;">{app['title']}</a>""", unsafe_allow_html=True)
        st.subheader(f"📱 {app['title']}")
        st.write(app["description"])
        #st.markdown(f"""<a href="{app['url']}" target="_self">開く</a>""", unsafe_allow_html=True)


center_align_html = """
<div style='text-align: center; color: gray; font-size: 16px;'>
  <br>
  <br>
  <p>© 2025 たたたぬき</p>
</div>
"""
st.markdown(center_align_html, unsafe_allow_html=True)
