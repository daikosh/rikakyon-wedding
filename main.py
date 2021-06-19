import streamlit as st
import importlib
import os
from PIL import Image
homepage = importlib.import_module("01_homepage.main")
radio = importlib.import_module("02_radio.main")
profile = importlib.import_module("03_profile.main")
party = importlib.import_module("04_party1.main")
radio_glee = importlib.import_module("05_radio_glee.main")

## Parameters ##
USERNAME = "rikakyon"
PASSWORD = "0326"

## Page Config ##
st.set_page_config(
    page_title="結婚式二次会 特設サイト",
    page_icon="🎊",
    #layout="wide",
    initial_sidebar_state="expanded"
)

## Hide Streamlit Official Menu ##
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def initialization():
    global PAGES
    PAGES = {
        "GREETING": homepage,
        "ABOUT": party,
        "PROFILES": profile,
        "マツイキョースケのオールナイトニッポン🍆📻": radio
    }


def is_authenticated(username, password):
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False

def generate_blocks():
    main_title = st.empty()
    main_description = st.empty()
    #main_description_eng = st.empty()
    return main_title, main_description#, main_description_eng

def generate_text(blocks):
    imgpath = "logo.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        blocks[0].image(image, output_format="png", use_column_width="auto")

def clear_blocks(blocks):
    for block in blocks:
        block.empty()

def write_text(text, fontsize, color, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; color:{}; font-size: {}px;">{}</p>'.format(align, color, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main():
    initialization()

    # Logo #
    blocks = generate_blocks()
    generate_text(blocks)

    ## Login Section ##
    login_expander = st.beta_expander("ログインセクション / Login Section", expanded=True)
    username = login_expander.text_input("ユーザ名 / Username")
    password = login_expander.text_input("パスワード / Password", value="", type="password")

    #login_expander.info("Authorized Personnel Only")
    login_expander.subheader("こちらは招待者専用のホームページです。URLやログイン情報は絶対に流出させないでください。")

    ## Body ##
    if is_authenticated(username, password):
        clear_blocks(blocks)
        login_expander.success("Logged / ログインに成功しました。")
        #write_text("響介・理香子 結婚式二次会 特設サイト", 32, "black", "center")
        selection = st.radio("", list(PAGES.keys()))
        page = PAGES[selection]
        page.main()
    else:
        pass

    ## Footer ##
    st.write("Copyright © 2021 EN-Jakee Association. All Rights Reserved.")

if __name__ == "__main__":
    main()
