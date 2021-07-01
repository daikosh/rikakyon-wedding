import streamlit as st
import os
from PIL import Image

## Parameters ##


## functions ##
def initialization():
    pass

def write_text(text, fontsize, color, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; color:{}; font-size: {}px;">{}</p>'.format(align, color, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main(debug):
    initialization()

    ## Body ##
    write_text("響介&理香子 結婚式二次会特設サイトにアクセスいただきありがとうございます。", 20, "black", "left")
    write_text("二次会に参加する人もしない人も楽しんで頂けるような様々なコンテンツを配信していきます。", 20, "black", "left")
    write_text("要望、リクエスト等があれば是非LINEへメッセージを送ってください。<br><br>", 20, "black", "left")
    write_text("運営メンバー　一同", 20, "black", "right")
if __name__ == "__main__":
    main(debug)
