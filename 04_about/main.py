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


def main(debug):
    initialization()

    ## Body ##
    st.markdown("""
        【結婚式二次会情報】


        日時: 2022年3月26日 (土)

        会場: 未定
    """)

if __name__ == "__main__":
    main(debug)
