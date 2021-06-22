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

def main():
    initialization()

    ## Body ##
    show_image("06_rikako/01_top.jpg", "jpg")

if __name__ == "__main__":
    main()
