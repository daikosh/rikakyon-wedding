import streamlit as st
from PIL import Image, ImageOps
import os
## Parameters ##


## functions ##
class About(object):
    def __init__(self, debug):
        self.debug = debug

    def open(self):
        ## Body ##
        st.markdown("""
            【結婚式二次会情報】

            日時: 2022年3月26日 (土)

            会場: 未定
        """)

def main(debug):
    about = About(debug)
    about.open()

if __name__ == "__main__":
    main(debug)
