import os

import streamlit as st
from PIL import Image, ImageOps


# メインクラス
class Profile(object):
    def __init__(self, debug):
        self.debug = debug

    def show_image(self, imgpath):
        """画像を表示"""
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")

    def write_text(self, text, fontsize, align):
        """テキストを表示"""
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open(self):
        """コンテンツページを表示"""

        # 説明文を表示
        st.markdown("響介&理香子と愉快な仲間たちをご紹介。")
        self.show_image("line.png")

        # メインキャストを表示
        st.title("MAIN CAST")
        self.show_image("03_profile/01_kyosuke.png")
        self.write_text("Kyosuke Matsui", "24", "center")
        self.show_image("03_profile/07_rikako.png")
        self.write_text("Rikako Inukai", "24", "center")

        # プロジェクトメンバーを表示
        st.title("PROJECT MEMBER")
        self.show_image("03_profile/05_akuzawa.png")
        self.write_text("Takuya Akuzawa", "24", "center")
        self.show_image("03_profile/02_daikosh2.png")
        self.write_text("daikosh", "24", "center")
        self.show_image("03_profile/04_rinrin.png")
        self.write_text("Hiroto Hayashi", "24", "center")
        self.show_image("03_profile/06_nobuaki.png")
        self.write_text("Nobuaki Yoshitane", "24", "center")


# メイン関数
def main(debug):
    # インスタンスを生成
    profile = Profile(debug)
    profile.open()

if __name__ == "__main__":
    main(debug)
