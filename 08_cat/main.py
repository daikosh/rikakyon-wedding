import os
import datetime as dt

import streamlit as st
from PIL import Image, ImageOps


# メインクラス
class Cat(object):
    def __init__(self, debug):
        self.debug = debug

    def is_released(self, release_time):
        """公開時刻になったとき"""

        # 現在時刻
        current_time = dt.datetime.now() + dt.timedelta(hours=9)

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

    def write_text(self, text, fontsize=18, align="left"):
        """テキストを表示"""
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open(self):
        """コンテンツページを表示"""

        # 説明文を表示
        st.markdown("""
            みなさんに投稿していただいたご自宅のにゃんこ、道端で見かけたにゃんこ、フリー素材のにゃんこなど、癒やされるにゃんこたちを公開中です。
            ちなみに響介は犬派。
        """)
        st.write("にゃんこたちの写真は[こちらのフォーム](https://forms.gle/rPJk87YdzdhvVTxr6)で募集しています！")
        self.show_image("line.png")


        # 猫画像を表示
        if self.is_released(dt.datetime(2021, 9, 25, 13, 00)):
            st.write("投稿者: たくと")
            st.image("08_cat/img/15.jpg", caption="たくとと猫")

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


# メイン関数
def main(debug):
    # インスタンスを生成
    neko = Cat(debug)
    neko.open()


if __name__ == "__main__":
    main(debug)
