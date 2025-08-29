import streamlit as st
import base64

st.set_page_config(page_title="たぬきツールズ", layout="centered")

# 画像ファイルをBase64に変換
def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Base64画像をHTMLで表示
image_base64 = get_base64_image("data/logo.png")  # 先頭の / は不要
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="data:image/png;base64,{image_base64}" style="height: 3em; margin-right: 0.5em;">
        <h2 style="margin: 0;">たぬきツールズ</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("X, IRIAM, Discordに使えるWebアプリ集です。")

# アプリ情報のリスト
apps = [
    {
        "title": "スクショを1枚の画像に並べるアプリ(for X)",
        "description": "複数のスクショ画像（縦横比一定）を指定した列数に並べて1枚の画像に変換するアプリです。余白の背景色指定可能です。",
        "pages": "pages/スクショを1枚の画像に並べるアプリ(for X).py"
    },
    {
        "title": "画像の一部を切り抜いて縮小するアプリ(for Discord)",
        "description": "たぬきが書いたちびキャラのイラストの顔周辺を切り抜いてDiscordの絵文字サイズ(128x128px)、スタンプサイズ(320x320px)に変換するアプリです。",
        "pages": "pages/画像の一部を切り抜いて縮小するアプリ(for Discord).py"
    },
    {
        "title": "画像を4分割するアプリ(for X)",
        "description": "画像を4分割し、Xで4枚並べたときに元画像だけが見えるように上下(左右)に余白をつけるアプリです。分割画像はZIPファイルにまとめてダウンロードできます。余白の背景色指定可能です。",
        "pages": "pages/画像を4分割するアプリ(for X).py"
    },
    {
        "title": "画像を縮小するアプリ(for Discord)",
        "description": "画像をDiscordの絵文字サイズ(128x128px)、スタンプサイズ(320x320px)に縮小するアプリです。元画像の余白除去もできます。",
        "pages": "pages/画像を縮小するアプリ(for Discord).py"
    },
    {
        "title": "画像を縮小するアプリ(for IRIAM)",
        "description": "画像をIRIAMの立ち絵サイズ(2000x4000px以内)、ミニキャラサイズ(600x600px以内)に縮小するアプリです。元画像の余白除去もできます。",
        "pages": "pages/画像を縮小するアプリ(for IRIAM).py"
    },
]

# 検索バー
search_query = st.text_input("🔍 アプリ名やキーワードで検索", "")

# 検索結果の表示
for app in apps:
    if search_query.lower() in app["title"].lower() or search_query.lower() in app["description"].lower():
        st.subheader(f"🍃 {app['title']}")
        st.write(app["description"])
        st.page_link(app["pages"], label=f"・{app["title"]}へ移動")
        st.markdown("---")

url = "https://x.com/ta_ta_ta_nu_ki"
st.markdown(
    f"""
    <div style='text-align: center;'>
        <br>
        <br>
        Copyright © 2024-2025 <a href="{url}">たたたぬき</a> #たぬきツールズ
    </div>
    """,
    unsafe_allow_html=True
)
