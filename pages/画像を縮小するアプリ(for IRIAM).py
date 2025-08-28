import os
import streamlit as st
from PIL import Image
from enum import Enum


IMG_PATH = 'image'


class Choice(Enum):
    def __str__(cls):
        return cls.name
    立ち絵 = 1
    ミニキャラ = 0

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


def crop_image(file_path, save_path):
    im = Image.open(file_path)
    cropped = im.crop(im.getbbox())
    cropped.save(save_path)

def get_size(file_path):
    im = Image.open(file_path)
    w, h = im.size
    return w, h

def resize_image(file_path, save_path, width, height):
    im = Image.open(file_path)
    w, h = im.size
    if w < width and h < height:
        return True
    im.thumbnail((width, height), Image.LANCZOS)
    im.save(save_path)

def main():
    delete_files()
    st.subheader('画像を縮小するアプリ(for IRIAM)')
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

        flag_crop = False
        if st.checkbox("余白を除去する"):
            flag_crop = True

        is_choice = st.radio("リサイズの大きさを選択してください", Choice, horizontal=True)
        st.write(is_choice)

        if is_choice.value == 1:
            st.write("横:2,000px、縦:4,000px以内にリサイズします。")
            w = 2000
            h = 4000
        elif is_choice.value == 0:
            st.write("横:600px、縦:600px以内にリサイズします。")
            w = 600
            h = 600

        if st.button("リサイズ実行"):
            if flag_crop:
                crop_image(FILE_PATH, SAVE_PATH)
                FILE_PATH = SAVE_PATH
            resize_image(FILE_PATH, SAVE_PATH, w, h)
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
    st.markdown(
        f"""
        <div style='text-align: center;'>
            Copyright © 2024-2025 <a href="{url}">たたたぬき</a> #たぬきツールズ
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
