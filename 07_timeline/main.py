import streamlit as st
from PIL import Image, ImageOps
import os
import datetime

## Parameters ##
RELEASE_TIME = datetime.datetime(2021, 9, 11, 13, 00)
NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)

## functions ##
class Timeline(object):
    def __init__(self, debug):
        self.debug = debug

    def show_image(self, imgpath):
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")

    def write_text(self, text, fontsize=18, align="left"):
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open_timeline_expander(self, title, imgpath, expanded):
        with st.beta_expander(title, expanded=expanded):
            self.show_image(imgpath)

    def open(self):
        st.markdown("""
            地球上に、今さ、人口って何人いるか知ってる？76億人いるの。

            76億人に、一人に一秒しか会わなくても240年かかるの。

            それが俺たちどう？もう出会って8年以上たってる。

            奇跡、乾杯！
        """)
        self.show_image("line.png")

        ## Body ##
        self.open_timeline_expander("第1章 幼少期", "07_timeline/01.png", False)
        if RELEASE_TIME <= NOW_TIME or self.debug is True:
            with st.beta_expander("第2章 中高生時代", expanded=True):
                self.show_image("07_timeline/02_1.png")
                self.show_image("07_timeline/02_2.png")
                self.show_image("07_timeline/02_3.png")
        # self.open_timeline_expander("第3章 大学1回生", "07_timeline/01.png", True)
        # self.open_timeline_expander("第4章 大学2回生", "07_timeline/01.png", True)
        # self.open_timeline_expander("第5章 大学3回生", "07_timeline/01.png", True)
        # self.open_timeline_expander("第6章 大学4回生", "07_timeline/01.png", True)
        # self.open_timeline_expander("第7章 社会人", "07_timeline/01.png", True)
        # self.open_timeline_expander("番外編 EVE祭", "07_timeline/01.png", True)
        # self.open_timeline_expander("番外編 プロポーズ", "07_timeline/01.png", True)
        # self.open_timeline_expander("番外編 新婚生活", "07_timeline/01.png", True)
        # self.open_timeline_expander("番外編 老後", "07_timeline/01.png", True)

        st.write("To be continued ...")

def main(debug):
    timeline = Timeline(debug)
    timeline.open()

if __name__ == "__main__":
    main(debug)
