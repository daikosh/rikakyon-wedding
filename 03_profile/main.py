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

    ## Body ##
    #show_image("03_profile/21_directors.png", "png")
    with st.beta_expander("新郎・新婦", expanded=True):
    #st.header("取締役")
        col1, col2 = st.beta_columns(2)
        with col1:
            show_image("03_profile/01_kyosuke.png", "png")
            write_text("松井 響介", "24", "Black", "center")
            #write_text("新郎", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
        with col2:
            show_image("03_profile/07_rikako.png", "png")
            write_text("犬飼 理香子", "24", "Black", "center")
            #write_text("新婦", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
    #show_image("03_profile/22_executive.png", "png")
    with st.beta_expander("企画メンバー", expanded=True):
    #st.header("執行役員")
        col1, col2 = st.beta_columns(2)

        with col1:
            show_image("03_profile/05_akuzawa.png", "png")
            write_text("阿久澤 拓也", "24", "Black", "center")
            #write_text("変態", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
            show_image("03_profile/02_daikosh.png", "png")
            write_text("松岡 大起", "24", "Black", "center")
            #write_text("婚活", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
        with col2:
            show_image("03_profile/04_rinrin.png", "png")
            write_text("林 寛人", "24", "Black", "center")
            #write_text("IWSP", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")
            show_image("03_profile/06_nobuaki.png", "png")
            write_text("吉種 伸彰", "24", "Black", "center")
            #write_text("教授", "16", "Black", "center")
            #write_text("", "14", "Black", "justify")

if __name__ == "__main__":
    main()
