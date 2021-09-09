import streamlit as st
from PIL import Image, ImageOps
import os
import datetime

## Parameters ##
NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
RELEASE_TIME = datetime.datetime(2021, 7, 24, 19, 00)

## functions ##
class Cat(object):
    def __init__(self, debug):
        self.debug = debug

    def show_image(self, imgpath):
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")

    def write_text(self, text, fontsize=18, align="left"):
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open(self):
        st.markdown("""
            みなさんに投稿していただいたご自宅のにゃんこ、道端で見かけたにゃんこ、フリー素材のにゃんこなど、癒やされるにゃんこたちを公開中です。
        """)
        st.write("にゃんこたちの写真は[こちらのフォーム](https://forms.gle/rPJk87YdzdhvVTxr6)で募集しています！")
        self.show_image("line.png")

        ## Body ##
        st.write("投稿者: 🐱")
        st.write("よそ様の猫トップ5")
        st.image("08_cat/img/05.jpeg", caption="フライング猫")
        st.image("08_cat/img/06.jpeg", caption="ジャストフィット猫")
        st.image("08_cat/img/07.jpeg", caption="脱走常習猫")
        st.image("08_cat/img/08.jpeg", caption="寝子")
        st.image("08_cat/img/09.jpeg", caption="くせになる猫")
        st.image("line.png", use_column_width="auto")

        st.write("投稿者: なおたろう")
        st.write("伏見稲荷大社には下り坂の途中で猫たちがいっぱい生活してるよ")
        st.image("08_cat/img/10.jpeg")
        st.image("08_cat/img/11.jpeg")
        st.image("08_cat/img/12.jpeg")
        st.image("line.png", use_column_width="auto")

        st.write("投稿者: ごっちん")
        st.write("何撮ってんだよ？のガン飛ばしシリーズです。")
        st.image("08_cat/img/13.jpeg", caption="しずく")
        st.image("08_cat/img/14.jpeg", caption="そら")

        st.write("投稿者: おみそ")
        st.image("08_cat/img/01_cat.jpeg", caption="王者の風格")
        st.image("line.png", use_column_width="auto")

        st.write("投稿者: べ")
        st.image("08_cat/img/02_cat.png", caption="だるまにされた猫です")
        st.image("line.png", use_column_width="auto")

        st.write("投稿者: ごっちん")
        st.write("猫のねころがりシリーズです。")
        st.image("08_cat/img/03_cat.jpeg", caption="しずく")
        st.image("08_cat/img/04_cat.jpeg", caption="そら")
        st.image("line.png", use_column_width="auto")

def main(debug):
    neko = Cat(debug)
    neko.open()

if __name__ == "__main__":
    main(debug)
