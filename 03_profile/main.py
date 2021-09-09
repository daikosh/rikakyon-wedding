import streamlit as st
from PIL import Image, ImageOps
import os
## Parameters ##


## functions ##
class Profile(object):
    def __init__(self, debug):
        self.debug = debug

    def show_image(self, imgpath, type):
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format=type, use_column_width="auto")

    def write_text(self, text, fontsize, align):
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open(self):
        ## Body ##
        st.markdown("響介&理香子と愉快な仲間たちをご紹介。")

        imgpath = "line.png"
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="png", use_column_width="auto")

        st.title("MAIN CAST")
        self.show_image("03_profile/01_kyosuke.png", "png")
        self.write_text("Kyosuke Matsui", "24", "center")
        self.show_image("03_profile/07_rikako.png", "png")
        self.write_text("Rikako Inukai", "24", "center")

        st.title("PROJECT MEMBER")
        self.show_image("03_profile/05_akuzawa.png", "png")
        self.write_text("Takuya Akuzawa", "24", "center")
        self.show_image("03_profile/02_daikosh2.png", "png")
        self.write_text("daikosh", "24", "center")
        self.show_image("03_profile/04_rinrin.png", "png")
        self.write_text("Hiroto Hayashi", "24", "center")
        self.show_image("03_profile/06_nobuaki.png", "png")
        self.write_text("Nobuaki Yoshitane", "24", "center")

def main(debug):
    profile = Profile(debug)
    profile.open()

if __name__ == "__main__":
    main(debug)
