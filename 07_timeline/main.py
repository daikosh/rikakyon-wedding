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

def write_text(text, fontsize=18, align="left"):
    new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main(debug):
    initialization()

    st.markdown("""
        地球上に、今さ、人口って何人いるか知ってる？63億人いるの。63億人に、一人に一秒しか会わなくても180年かかるの。それが俺たちどう？もう出会って8年以上たってる。奇跡、乾杯！
    """)

    imgpath = "line.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")

    ## Body ##
    with st.beta_expander("誕生〜小学生", expanded=True):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")

if __name__ == "__main__":
    main(debug)
