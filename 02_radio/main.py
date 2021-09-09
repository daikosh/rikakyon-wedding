import streamlit as st
from PIL import Image, ImageOps
import os
import datetime

## Parameters ##
NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
RELEASE_TIME = datetime.datetime(2021, 8, 28, 13, 00)

## functions ##
class Radio(object):
    def __init__(self, debug):
        self.debug = debug

    def show_image(self, imgpath):
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")

    def open_radio(self, mp3path):
        if os.path.exists(mp3path):
            audio_file = open(mp3path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')

    def open_radio_expander(self, title, imgpath, mp3path, expanded):
        with st.beta_expander(title, expanded=expanded):
            self.show_image(imgpath)
            self.open_radio(mp3path)

    def write_text(self, text, fontsize, align):
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open(self):
        st.markdown("""
        マツイキョースケのオールナイトニッポンは結婚式二次会へ向けてなんやかんややっていく番組です。

        毎回ステキなゲストとともにお送りしています！
        """)
        st.write("おたよりは[こちらのフォーム](https://forms.gle/2HiMwgmzzhrxTJ5BA)から募集しています！")
        self.show_image("line.png")

        ## Body ##
        self.open_radio_expander(
            "#1 「人材紹介業Feeとりがち〜そうだ、顎削ろう〜」【ゲスト: 林寛人、松岡大起】 (2021.5.29 収録)",
            '02_radio/01_radio_no1.jpg',
            '02_radio/01_radio_no1.mp3',
            False
        )
        self.open_radio_expander(
            "#2 「珍名字東京大決戦〜城之内死す〜」【ゲスト: 阿久澤拓也、吉種伸彰】 (2021.6.12 収録)",
            '02_radio/02_radio_no2.jpg',
            '02_radio/02_radio_no2.mp3',
            False
        )
        with st.beta_expander(
            "#3 「聴取率を爆上げしたいので、弦のカリスマをゲストに呼びました。」【ゲスト: 和久あさぎ、毛利真夕】 (2021.7.22 収録)",
            expanded=True):
            self.show_image("02_radio/03_radio_no3.jpg")
            st.write("◯Part 1/3 「今野さん、毛利さん、お久しぶりです。」 ")
            self.open_radio('02_radio/03_radio_no3.mp3')
            st.write("◯Part 2/3 「君はバレンティンを憶えているか？」 ")
            self.open_radio('02_radio/04_radio_3-2.mp3')

        self.write_text("To be continued ...", 16, "left")


def main(debug):
    radio = Radio(debug)
    radio.open()

if __name__ == "__main__":
    main(debug)
