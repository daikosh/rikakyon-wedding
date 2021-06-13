import streamlit as st
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

def main():
    initialization()

    ## Body ##
    st.title("犬飼響介 結婚式 2次会専用HP")
    st.subheader("招待者専用のホームページです。流出しないでね。")
    st.info("Authorized Personnel Only")
    st.write("サイドバーの'Choose Apps'からコンテンツを選ぶんじゃ。")

if __name__ == "__main__":
    main()