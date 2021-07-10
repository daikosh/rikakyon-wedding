import streamlit as st
from PIL import Image, ImageOps
import os
## Parameters ##


## functions ##
def initialization():
    pass

def show_image(imgpath, type):
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format=type, use_column_width="auto")

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
    st.markdown("""
        Coming soon...
    """)


if __name__ == "__main__":
    main(debug)
