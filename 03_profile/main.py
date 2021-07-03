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

def write_text(text, fontsize, color, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; color:{}; font-size: {}px;">{}</p>'.format(align, color, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main(debug):
    initialization()

    ## Body ##
    if debug is False:
        with st.beta_expander("MAIN CAST", expanded=True):
            col1, col2 = st.beta_columns(2)
            with col1:
                show_image("03_profile/01_kyosuke.png", "png")
                write_text("Kyosuke Matsui", "24", "Black", "center")
            with col2:
                show_image("03_profile/07_rikako.png", "png")
                write_text("Rikako Inukai", "24", "Black", "center")
        with st.beta_expander("PROJECT MEMBER", expanded=True):
            col1, col2 = st.beta_columns(2)
            with col1:
                show_image("03_profile/05_akuzawa.png", "png")
                write_text("Takuya Akuzawa", "24", "Black", "center")
                show_image("03_profile/02_daikosh2.png", "png")
                write_text("daikosh", "24", "Black", "center")
            with col2:
                show_image("03_profile/04_rinrin.png", "png")
                write_text("Hiroto Hayashi", "24", "Black", "center")
                show_image("03_profile/06_nobuaki.png", "png")
                write_text("Nobuaki Yoshitane", "24", "Black", "center")
    else:
        st.title("MAIN CAST")
        imgpath = "line.png"
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="png", use_column_width="auto")

        show_image("03_profile/01_kyosuke.png", "png")
        write_text("Kyosuke Matsui", "24", "Black", "center")
        show_image("03_profile/07_rikako.png", "png")
        write_text("Rikako Inukai", "24", "Black", "center")

        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="png", use_column_width="auto")
        st.title("PROJECT MEMBER")

        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="png", use_column_width="auto")

        show_image("03_profile/05_akuzawa.png", "png")
        write_text("Takuya Akuzawa", "24", "Black", "center")
        show_image("03_profile/02_daikosh2.png", "png")
        write_text("daikosh", "24", "Black", "center")
        show_image("03_profile/04_rinrin.png", "png")
        write_text("Hiroto Hayashi", "24", "Black", "center")
        show_image("03_profile/06_nobuaki.png", "png")
        write_text("Nobuaki Yoshitane", "24", "Black", "center")

if __name__ == "__main__":
    main(debug)
