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

def open_radio_expander(title, imgpath, mp3path):
    with st.beta_expander(title, expanded=True):
        col1, col2, col3 = st.beta_columns(3)
        image = Image.open(imgpath)
        #image = ImageOps.flip(image)
        #image = ImageOps.mirror(image)
        col2.image(image, output_format="jpeg", width=400)
        if os.path.exists(mp3path):
            audio_file = open(mp3path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
        else:
            st.write("準備中です！！！")

def main():
    initialization()

    ## Body ##
    st.title("マツイキョースケのオールナイトニッポン")
    open_radio_expander("#1 〜ついに結婚します！〜 【ゲスト: 林寛人、松岡大起】 (2021.5.29 収録)", '02_radio/01_radio_no1.jpg', '02_radio/01_radio_no1.mp3')
    open_radio_expander("#2 〜離婚の危機！？〜 【ゲスト: 阿久澤拓也、吉種伸彰】 (2021.6.12 収録)", '02_radio/02_radio_no2.jpg', '02_radio/02_radio_no2.mp3')

if __name__ == "__main__":
    main()
