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
        #col1, col2, col3 = st.beta_columns(3)
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="jpeg", width=700)
        if os.path.exists(mp3path):
            audio_file = open(mp3path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
        else:
            st.info("準備中です！！！")

def main():
    initialization()

    ## Body ##
    st.title("マツイキョースケのオールナイトニッポン🍆📻")
    open_radio_expander("#1 「人材紹介業フィーとりがち〜そうだ、顎削ろう〜」 【ゲスト: 林寛人、松岡大起】 (2021.5.29 収録)", '02_radio/01_radio_no1.jpg', '02_radio/01_radio_no1.mp3')
    open_radio_expander("#2 「珍苗字東京大決戦〜城之内死す〜」 【ゲスト: 阿久澤拓也、吉種伸彰】 (2021.6.12 収録)", '02_radio/02_radio_no2.jpg', '02_radio/02_radio_no2.mp3')
    open_radio_expander("#3 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/03_radio_no3.jpg', '02_radio/03_radio_no3.mp3')
    open_radio_expander("#4 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/04_radio_no4.jpg', '02_radio/04_radio_no4.mp3')
    open_radio_expander("#5 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/05_radio_no5.jpg', '02_radio/05_radio_no5.mp3')
    open_radio_expander("#6 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/06_radio_no6.jpg', '02_radio/06_radio_no6.mp3')
    open_radio_expander("#7 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/07_radio_no7.jpg', '02_radio/07_radio_no7.mp3')
    open_radio_expander("#8 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/08_radio_no8.jpg', '02_radio/08_radio_no8.mp3')
    open_radio_expander("#9 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/09_radio_no9.jpg', '02_radio/09_radio_no9.mp3')
    open_radio_expander("#10 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/10_radio_no10.jpg', '02_radio/10_radio_no10.mp3')


if __name__ == "__main__":
    main()
