import streamlit as st
from PIL import Image, ImageOps
import os
import datetime
## Parameters ##


## functions ##
def initialization():
    pass

def show_image(imgpath):
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, use_column_width="auto")

def write_text(text, fontsize=18, align="left"):
    new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main(debug):
    initialization()

    st.markdown("""
        みなさんに投稿していただいたご自宅のにゃんこ、道端で見かけたにゃんこ、フリー素材のにゃんこなど、癒やされるにゃんこたちを公開予定です。
    """)

    st.write("にゃんこたちの写真は[こちらのフォーム](https://forms.gle/rPJk87YdzdhvVTxr6)で募集しています！")

    imgpath = "line.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")

    ## Body ##
    NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
    RELEASE_TIME = datetime.datetime(2022, 7, 10, 19, 00)
    if RELEASE_TIME < NOW_TIME or debug is True: # リリース時間になったとき
        st.write("投稿者: おみそ")
        st.image("08_cat/img/01_cat.jpeg", caption="王者の風格")

        st.write("投稿者: べ")
        st.image("08_cat/img/02_cat.png", caption="だるまにされた猫です")


    else: # リリース前
        st.markdown("""
            Coming soon...
        """)



if __name__ == "__main__":
    main(debug)
