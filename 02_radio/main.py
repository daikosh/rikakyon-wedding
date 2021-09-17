import os
import datetime

import streamlit as st
from PIL import Image, ImageOps


# メインクラス
class Radio(object):
    def __init__(self, debug):
        self.debug = debug

    def is_release(self, release_time):
        """公開時刻になったとき"""

        # 現在時刻
        current_time = datetime.datetime.now() + datetime.timedelta(hours=9)

        # 現在時刻がリリース時間になった場合
        if current_time >= release_time or self.debug is True:
            return True

        # 現在時刻がリリース時間になっていない場合
        else:
            return False

    def show_image(self, imgpath):
        """画像を表示"""
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")

    def open_radio(self, mp3path):
        """ラジオを表示"""
        if os.path.exists(mp3path):
            audio_file = open(mp3path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')

    def open_radio_expander(self, title, imgpath, mp3path, expanded):
        """ラジオエクスパンダーを表示"""
        with st.beta_expander(title, expanded=expanded):
            self.show_image(imgpath)
            self.open_radio(mp3path)

    def write_text(self, text, fontsize, align):
        """テキストを表示"""
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open(self):
        """コンテンツページを表示"""

        # 説明文を表示
        st.markdown("""
        マツイキョースケのオールナイトニッポンは結婚式二次会へ向けてなんやかんややっていく番組です。

        毎回ステキなゲストとともにお送りしています！
        """)
        st.write("おたよりは[こちらのフォーム](https://forms.gle/2HiMwgmzzhrxTJ5BA)から募集しています！")
        self.show_image("line.png")

        # ラジオ1回目を表示
        self.open_radio_expander(
            "#1 「人材紹介業Feeとりがち〜そうだ、顎削ろう〜」【ゲスト: 林寛人、松岡大起】 (2021.5.29 収録)",
            '02_radio/01_radio_no1.jpg',
            '02_radio/01_radio_no1.mp3',
            False
        )
        # ラジオ2回目を表示
        self.open_radio_expander(
            "#2 「珍名字東京大決戦〜城之内死す〜」【ゲスト: 阿久澤拓也、吉種伸彰】 (2021.6.12 収録)",
            '02_radio/02_radio_no2.jpg',
            '02_radio/02_radio_no2.mp3',
            False
        )
        # ラジオ3回目を表示
        with st.beta_expander(
            "#3 「聴取率を爆上げしたいので、弦のカリスマをゲストに呼びました。」【ゲスト: 和久あさぎ、毛利真夕】 (2021.7.22 収録)",
            expanded=True):
            self.show_image("02_radio/03_radio_no3.jpg")
            st.write("◯Part 1/3 「今野さん、毛利さん、お久しぶりです。」")
            self.open_radio('02_radio/03_radio_no3.mp3')
            st.write("◯Part 2/3 「君はバレンティンを憶えているか？」")
            self.open_radio('02_radio/04_radio_3-2.mp3')

            if self.is_release(datetime.datetime(2021, 9, 18, 13, 00)):
                st.write("◯Part 3/3 「おじさんがハマってるものは大抵たのしい。」")
                self.open_radio('02_radio/04_radio_3-3.mp3')


        # To be continued ... を表示
        self.write_text("To be continued ...", 16, "left")


# メイン関数
def main(debug):
    # インスタンスを生成
    radio = Radio(debug)
    radio.open()

if __name__ == "__main__":
    main(debug)
