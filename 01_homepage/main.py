import streamlit as st
import os
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import base64

## Parameters ##


## functions ##
def initialization():
    pass

def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)
    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

def write_text(text, fontsize, color, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; color:{}; font-size: {}px;">{}</p>'.format(align, color, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main():
    initialization()
    ## Title ##
    #write_text("響介・理香子　結婚式二次会　特設サイト", 32, "black", "center")
    imgpath = "01_homepage/logo.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")


    ## Body ##
    st.write("お久しぶりです。")
    st.write("結婚式二次会特設サイトにアクセスいただきありがとうございます。")
    st.write("二次会に参加する人もしない人も楽しんで頂けるような様々なコンテンツを配信していきます。")
    st.write("要望、リクエスト等があれば是非LINEへメッセージを送ってください。")
    st.write("")
    write_text("EN-Jakeeプロジェクトメンバー　一同", 16, "black", "right")
if __name__ == "__main__":
    main()
