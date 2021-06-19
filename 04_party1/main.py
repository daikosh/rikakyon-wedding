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
    with st.beta_expander("日時・会場", expanded=True):
        st.markdown('<p style="font-size: 28px">日時: 2022年3月26日 (土)', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 28px">会場: 未定 </p>', unsafe_allow_html=True)
        #show_image("04_party1/01_fortune_garden.png", "png")
        #st.markdown(
        #    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3267.7758221667495!2d135.7665824152407!3d35.012316480355665!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6001088d75e52813%3A0xfa711b5fcec57e9c!2z44OV44Kp44O844OB44Ol44Oz44Ks44O844OH44Oz5Lqs6YO9772cRk9SVFVORSBHQVJERU4gS1lPVE8!5e0!3m2!1sja!2sjp!4v1623846798297!5m2!1sja!2sjp" width="600" height="450" style="border:0;"allowfullscreen="" loading="lazy"></iframe>', unsafe_allow_html=True
        #    )



if __name__ == "__main__":
    main()
