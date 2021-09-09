import streamlit as st
import os
from PIL import Image

## Parameters ##


## functions ##
class Greeting(object):
    def __init__(self, debug):
        self.debug = debug

    def write_text(self, text, fontsize, align):
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open(self):
        ## Body ##
        st.markdown("""
        響介&理香子 結婚式二次会特設サイトにアクセスいただきありがとうございます。

        二次会に参加する人もしない人も楽しんで頂けるような様々なコンテンツを配信していきます。

        要望、リクエスト等があれば是非LINEへメッセージを送ってください。
        """)
        self.write_text("運営メンバー　一同", 16, "right")

def main(debug):
    greeting = Greeting(debug)
    greeting.open()

if __name__ == "__main__":
    main(debug)
