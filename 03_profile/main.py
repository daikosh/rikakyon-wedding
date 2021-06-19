import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import base64
import os
## Parameters ##


## functions ##
def initialization():
    pass

def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)
    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

def show_image(imgpath, type):
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format=type, use_column_width="auto")

def write_text(text, fontsize, color, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; color:{}; font-size: {}px;">{}</p>'.format(align, color, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main():
    initialization()
    ## Title ##
    write_text("響介・理香子 結婚式二次会 特設サイト", 32, "black", "center")
    imgpath = "03_profile/logo.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")

    ## Body ##
    #show_image("03_profile/21_directors.png", "png")
    with st.beta_expander("MAIN CAST", expanded=True):
    #st.header("取締役")
        col1, col2 = st.beta_columns(2)
        with col1:
            show_image("03_profile/01_kyosuke.png", "png")
            write_text("Kyosuke Matsui", "24", "Black", "center")
            #write_text("新郎", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
        with col2:
            show_image("03_profile/07_rikako.png", "png")
            write_text("Rikako Inukai", "24", "Black", "center")
            #write_text("新婦", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
    #show_image("03_profile/22_executive.png", "png")
    with st.beta_expander("PROJECT MEMBER", expanded=True):
    #st.header("執行役員")
        col1, col2 = st.beta_columns(2)

        with col1:
            show_image("03_profile/05_akuzawa.png", "png")
            write_text("Takuya Akuzawa", "24", "Black", "center")
            #write_text("変態", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
            show_image("03_profile/02_daikosh2.png", "png")
            write_text("daikosh", "24", "Black", "center")
            #write_text("婚活", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
        with col2:
            show_image("03_profile/04_rinrin.png", "png")
            write_text("Hiroto Hayashi", "24", "Black", "center")
            #write_text("IWSP", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
            show_image("03_profile/06_nobuaki.png", "png")
            write_text("Nobuaki Yoshitane", "24", "Black", "center")
            #write_text("教授", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")

if __name__ == "__main__":
    main()
