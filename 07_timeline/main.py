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
        地球上に、今さ、人口って何人いるか知ってる？76億人いるの。

        76億人に、一人に一秒しか会わなくても240年かかるの。

        それが俺たちどう？もう出会って8年以上たってる。

        奇跡、乾杯！
    """)

    imgpath = "line.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")

    ## Body ##
    with st.beta_expander("第1章 幼少期", expanded=True):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    with st.beta_expander("第2章 中高校生", expanded=False):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    with st.beta_expander("第3章 大学1回生", expanded=False):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    with st.beta_expander("第4章 大学2回生", expanded=False):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    with st.beta_expander("第5章 大学3回生", expanded=False):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    with st.beta_expander("第6章 大学4回生", expanded=False):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    with st.beta_expander("第7章 社会人", expanded=False):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    with st.beta_expander("番外編 EVE祭", expanded=False):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    with st.beta_expander("番外編 プロポーズ", expanded=False):
        imgpath = "07_timeline/Timeline.png"
        show_image(imgpath, "png")
    # with st.beta_expander("第8章 新婚生活", expanded=True):
    #     imgpath = "07_timeline/Timeline.png"
    #     show_image(imgpath, "png")
    # with st.beta_expander("第9章 老後", expanded=True):
    #     imgpath = "07_timeline/Timeline.png"
    #     show_image(imgpath, "png")



if __name__ == "__main__":
    main(debug)
