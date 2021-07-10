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

def write_text(text, fontsize, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main(debug):
    initialization()

    ## Body ##
    st.markdown("""
        響介&理香子と愉快な仲間たちをご紹介。
    """)

    imgpath = "line.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")

    st.title("MAIN CAST")
    show_image("03_profile/01_kyosuke.png", "png")
    write_text("Kyosuke Matsui", "24", "center")
    show_image("03_profile/07_rikako.png", "png")
    write_text("Rikako Inukai", "24", "center")

    st.title("PROJECT MEMBER")
    show_image("03_profile/05_akuzawa.png", "png")
    write_text("Takuya Akuzawa", "24", "center")
    show_image("03_profile/02_daikosh2.png", "png")
    write_text("daikosh", "24", center")
    show_image("03_profile/04_rinrin.png", "png")
    write_text("Hiroto Hayashi", "24", "center")
    show_image("03_profile/06_nobuaki.png", "png")
    write_text("Nobuaki Yoshitane", "24", "center")

if __name__ == "__main__":
    main(debug)
