import streamlit as st
import importlib
import os
from PIL import Image
import datetime

homepage = importlib.import_module("01_homepage.main")
radio = importlib.import_module("02_radio.main")
profile = importlib.import_module("03_profile.main")
party = importlib.import_module("04_about.main")
radio_glee = importlib.import_module("05_radio_glee.main")
rikako = importlib.import_module("06_rikako.main")
timeline = importlib.import_module("07_timeline.main")
cat = importlib.import_module("08_cat.main")

## Parameters ##
USERNAME = "rikakyon"
PASSWORD = "0326"
NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
RELEASE_TIME = datetime.datetime(2021, 8, 21, 13, 00)

## Page Config ##
st.set_page_config(
    page_title="結婚式二次会 特設サイト",
    page_icon="🎊",
    initial_sidebar_state="expanded"
)

## Hide Streamlit Official Menu ##
max_width = 1000
padding_top = 1
padding_right = 2.5
padding_left = 2.5
padding_bottom = 1
COLOR = "black"
BACKGROUND_COLOR = "white"
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
"""

set_width_style =f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(set_width_style, unsafe_allow_html=True)

class Mainpage(object):
    def __init__(self):
        self.pages = {
            "GREETING": homepage,
            "ABOUT": party,
            "PROFILE": profile,
            "TIMELINE": timeline,
            "マツイキョースケのオールナイトニッポン🍆📻": radio,
            "同響グリークラブのオールナイトニッポン０🕺🕺🕺🕺": radio_glee,
            "わんこ旅🐶📷": rikako,
            "みんなのにゃんこ🐱": cat
        }

    def is_authenticated(self, username, password):
        if username == USERNAME and password == PASSWORD:
            return 1
        elif username == USERNAME and password == "0622":
            return 2
        else:
            return 0

    def write_text(self, text, fontsize, align):
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def generate_blocks(self):
        main_title = st.empty()
        main_description = st.empty()
        main_description_eng = st.empty()
        return main_title, main_description, main_description_eng

    def generate_text(self, blocks):
        imgpath = "logo.png"
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            blocks[0].image(image, output_format="png", use_column_width="auto")

    def clear_blocks(self, blocks):
        for block in blocks:
            block.empty()

    def generate_logo_blocks(self):
        main_title = st.empty()
        main_description = st.empty()
        main_description_eng = st.empty()
        return main_title, main_description, main_description_eng

    def generate_logo(self, blocks, page):
        imgpath = "{}logo.png".format(page)
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            blocks[0].image(image, output_format="png", use_column_width="auto")

    def open(self):
        # Logo #
        blocks = self.generate_blocks()
        self.generate_text(blocks)

        ## Login Section ##
        login_expander = st.beta_expander("ログインセクション / Login Section", expanded=True)
        username = login_expander.text_input("ユーザ名 / Username")
        password = login_expander.text_input("パスワード / Password", value="", type="password")
        login_expander.markdown("""こちらは招待者専用のホームページです。URLやログイン情報は絶対に流出させないでください。""")

        if self.is_authenticated(username, password) == 1: # メイン
            self.clear_blocks(blocks)
            login_expander.success("Logged / ログインに成功しました。")
            self.debug = False

            ## Body ##
            self.write_text("響介&理香子<br>結婚式二次会<br>特設サイト", 34, "center")
            logo_blocks = self.generate_logo_blocks()
            selection = st.radio("", list(self.pages.keys()))
            imgpath = "line.png"
            if os.path.exists(imgpath):
                image = Image.open(imgpath)
                st.image(image, output_format="png", use_column_width="auto")
            if selection == "GREETING":
                self.generate_logo(logo_blocks, "")
            elif selection == "ABOUT":
                self.generate_logo(logo_blocks, "04_about/")
            elif selection == "PROFILE":
                self.generate_logo(logo_blocks, "03_profile/")
            elif selection == "マツイキョースケのオールナイトニッポン🍆📻":
                self.generate_logo(logo_blocks, "02_radio/")
            elif selection == "わんこ旅🐶📷":
                self.generate_logo(logo_blocks, "06_rikako/")
            elif selection == "みんなのにゃんこ🐱":
                self.generate_logo(logo_blocks, "08_cat/")
            elif selection == "TIMELINE":
                self.generate_logo(logo_blocks, "07_timeline/")
            elif selection == "同響グリークラブのオールナイトニッポン０🕺🕺🕺🕺":
                self.generate_logo(logo_blocks, "05_radio_glee/")

            page = self.pages[selection]
            page.main(self.debug)

        elif self.is_authenticated(username, password) == 2: # デバッグモード時
            self.clear_blocks(blocks)
            login_expander.success("Debug Mode / デバッグモード！！！")
            self.debug = True

            ## Body ##
            self.write_text("響介&理香子<br>結婚式二次会<br>特設サイト", 34, "center")
            logo_blocks = self.generate_logo_blocks()
            selection = st.radio("", list(self.pages.keys()))
            imgpath = "line.png"
            if os.path.exists(imgpath):
                image = Image.open(imgpath)
                st.image(image, output_format="png", use_column_width="auto")
            if selection == "GREETING":
                self.generate_logo(logo_blocks, "")
            elif selection == "ABOUT":
                self.generate_logo(logo_blocks, "04_about/")
            elif selection == "PROFILE":
                self.generate_logo(logo_blocks, "03_profile/")
            elif selection == "マツイキョースケのオールナイトニッポン🍆📻":
                self.generate_logo(logo_blocks, "02_radio/")
            elif selection == "わんこ旅🐶📷":
                self.generate_logo(logo_blocks, "06_rikako/")
            elif selection == "TIMELINE":
                self.generate_logo(logo_blocks, "07_timeline/")
            elif selection == "みんなのにゃんこ🐱":
                self.generate_logo(logo_blocks, "08_cat/")
            elif selection == "同響グリークラブのオールナイトニッポン０🕺🕺🕺🕺":
                self.generate_logo(logo_blocks, "05_radio_glee/")

            page = self.pages[selection]
            page.main(self.debug)

        ## Footer ##
        imgpath = "line.png"
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="png", use_column_width="auto")
        st.write("Copyright © 2021 EN-Jakee Association. All Rights Reserved.")


if __name__ == "__main__":
    mainpage = Mainpage()
    mainpage.open()
