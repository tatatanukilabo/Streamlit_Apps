import os
import streamlit as st
from PIL import Image
from enum import Enum


IMG_PATH = 'image'


class Choice(Enum):
    def __str__(cls):
        return cls.name
    絵文字 = 1
    スタンプ = 0

def delete_files():
    for filename in list_imgs():
        os.remove(f"./{IMG_PATH}/{filename}")

def list_imgs():
    # IMG_PATH 内の画像ファイルを列挙
    return [
        filename
        for filename in os.listdir(IMG_PATH)
        if filename.split('.')[-1] in ['jpg', 'jpeg', 'png']
    ]

def crop_image(left, top, right, bottom, file_path, save_path):
    # 画像を開く
    image = Image.open(file_path)
    # 画像を切り抜く
    cropped_image = image.crop((left, top, right, bottom))
    # 切り抜いた画像を保存する
    cropped_image.save(save_path)

def resize_image(file_path, save_path, width, height):
    im = Image.open(file_path)
    w, h = im.size
    if w < width and h < height:
        return True
    im.thumbnail((width, height), Image.LANCZOS)
    im.save(save_path)

def get_size(file_path):
    im = Image.open(file_path)
    w, h = im.size
    return w, h

def main():
    delete_files()
    st.subheader('画像の一部を切り抜いて縮小するアプリ（for Discord）ver.0.1')
    file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
    if file:
        st.markdown(f'{file.name} をアップロードしました.')
        FILE_PATH = os.path.join(IMG_PATH, file.name)
        # 画像を保存する
        with open(FILE_PATH, 'wb') as f:
            f.write(file.read())
        im = Image.open(FILE_PATH)
        st.image(im, caption='変換前の画像')
        SAVE_PATH = f"image/resize_{file.name}"

        w = 0
        h = 0

        # 切り抜く範囲の左上と右下の座標
        st.write("切り抜く範囲を指定してください.")
        left = st.number_input("left(画像の左上基準に左から何pxか)", 1044)
        top = st.number_input("top(画像の左上基準に上から何pxか)", 951)
        wh = st.number_input("width & height(切り抜く幅と高さは何pxか)", value=900)
        right = wh + left
        bottom = wh + top

        is_choice = st.radio("リサイズの大きさを選択してください", Choice, horizontal=True)
        st.write(is_choice)

        if is_choice.value == 1:
            st.write("縦横128pxリサイズします。")
            w = 128
            h = 128
        elif is_choice.value == 0:
            st.write("縦横320pxリサイズします。")
            w = 320
            h = 320

        if st.button("クロップ＆リサイズ実行"):
            crop_image(left, top, right, bottom, FILE_PATH, SAVE_PATH)
            resize_image(SAVE_PATH, SAVE_PATH, w, h)
            im = Image.open(SAVE_PATH)
            st.image(im, caption='変換後の画像')
            # ダウンロード
            st.download_button(
                'ダウンロード',
                open(SAVE_PATH, 'br'),
                f"resize_{file.name}"
            )
            delete_files()

    url = "https://x.com/ta_ta_ta_nu_ki"
    st.write("Copyright © 2025 [たたたぬき](%s) #たぬきツール" % url)

if __name__ == '__main__':
    main()
