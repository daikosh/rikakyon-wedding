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

## Parameters ##
USERNAME = "rikakyon"
PASSWORD = "0326"
NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
RELEASE_TIME = datetime.datetime(2021, 7, 3, 19, 00)

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
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
</style>
"""


st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(set_width_style, unsafe_allow_html=True)


def initialization():
    global PAGES, PAGES_DEBUG
    if RELEASE_TIME < NOW_TIME: # リリース時間になったとき
        PAGES = {
            "GREETING": homepage,
            "ABOUT": party,
            "PROFILE": profile,
            "マツイキョースケのオールナイトニッポン🍆📻": radio,
            #"同響グリーのオールナイトニッポン0🔞": radio_glee,
            "わんこ旅🐶📷": rikako
            #"二人と同響の年表": timeline
        }
    else:
        PAGES = {
            "GREETING": homepage,
            "ABOUT": party,
            "PROFILE": profile,
            "マツイキョースケのオールナイトニッポン🍆📻": radio,
            #"同響グリーのオールナイトニッポン0🔞": radio_glee,
            "わんこ旅🐶📷": rikako
            #"二人の軌跡": timeline
        }

    PAGES_DEBUG = {
        "GREETING": homepage,
        "ABOUT": party,
        "PROFILE": profile,
        "マツイキョースケのオールナイトニッポン🍆📻": radio,
        #"同響グリーのオールナイトニッポン0🔞": radio_glee,
        "わんこ旅🐶📷": rikako,
        "二人の軌跡": timeline
    }

def is_authenticated(username, password):
    if username == USERNAME and password == PASSWORD:
        return 1
    elif username == USERNAME and password == "0622":
        return 2
    else:
        return 0

def write_text(text, fontsize, color, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; color:{}; font-size: {}px;">{}</p>'.format(align, color, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def generate_blocks():
    main_title = st.empty()
    main_description = st.empty()
    main_description_eng = st.empty()
    return main_title, main_description, main_description_eng

def generate_text(blocks):
    imgpath = "logo.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        blocks[0].image(image, output_format="png", use_column_width="auto")

def clear_blocks(blocks):
    for block in blocks:
        block.empty()

def generate_logo_blocks():
    main_title = st.empty()
    main_description = st.empty()
    main_description_eng = st.empty()
    return main_title, main_description, main_description_eng

def generate_logo(blocks, page):
    imgpath = "{}logo.png".format(page)
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        blocks[0].image(image, output_format="png", use_column_width="auto")

def main():
    initialization()

    # Logo #
    blocks = generate_blocks()
    generate_text(blocks)

    ## Login Section ##
    login_expander = st.beta_expander("ログインセクション / Login Section", expanded=True)
    username = login_expander.text_input("ユーザ名 / Username")
    password = login_expander.text_input("パスワード / Password", value="", type="password")
    login_expander.markdown("""こちらは招待者専用のホームページです。URLやログイン情報は絶対に流出させないでください。""")

    if is_authenticated(username, password) == 1: # メイン
        clear_blocks(blocks)
        login_expander.success("Logged / ログインに成功しました。")
        debug = False

        ## Body ##
        write_text("響介&理香子<br>結婚式二次会<br>特設サイト", 34, "black", "center")
        logo_blocks = generate_logo_blocks()
        selection = st.radio("", list(PAGES.keys()))
        imgpath = "line.png"
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="png", use_column_width="auto")
        if selection == "GREETING":
            generate_logo(logo_blocks, "")
        elif selection == "ABOUT":
            generate_logo(logo_blocks, "04_about/")
        elif selection == "PROFILE":
            generate_logo(logo_blocks, "03_profile/")
        elif selection == "マツイキョースケのオールナイトニッポン🍆📻":
            generate_logo(logo_blocks, "02_radio/")
        elif selection == "わんこ旅🐶📷":
            generate_logo(logo_blocks, "06_rikako/")
        elif selection == "二人の軌跡":
            generate_logo(logo_blocks, "07_timeline/")
        elif selection == "同響グリーのオールナイトニッポン0🔞":
            generate_logo(logo_blocks, "05_radio_glee/")

        page = PAGES[selection]
        page.main(debug)

    elif is_authenticated(username, password) == 2: # デバッグモード時
        clear_blocks(blocks)
        login_expander.success("Debug Mode / デバッグモード！！！")
        debug = True

        st.write(RELEASE_TIME)
        st.write(NOW_TIME)
        if RELEASE_TIME < NOW_TIME:
            st.write("公開！！！！！！")
        else:
            st.write("公開前")

        ## Body ##
        write_text("響介&理香子<br>結婚式二次会<br>特設サイト", 34, "black", "center")
        logo_blocks = generate_logo_blocks()
        selection = st.radio("", list(PAGES_DEBUG.keys()))
        imgpath = "line.png"
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="png", use_column_width="auto")
        if selection == "GREETING":
            generate_logo(logo_blocks, "")
        elif selection == "ABOUT":
            generate_logo(logo_blocks, "04_about/")
        elif selection == "PROFILE":
            generate_logo(logo_blocks, "03_profile/")
        elif selection == "マツイキョースケのオールナイトニッポン🍆📻":
            generate_logo(logo_blocks, "02_radio/")
        elif selection == "わんこ旅🐶📷":
            generate_logo(logo_blocks, "06_rikako/")
        elif selection == "二人の軌跡":
            generate_logo(logo_blocks, "07_timeline/")
        elif selection == "同響グリーのオールナイトニッポン0🔞":
            generate_logo(logo_blocks, "05_radio_glee/")

        page = PAGES_DEBUG[selection]
        page.main(debug)

    ## Footer ##
    imgpath = "line.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")
    st.write("Copyright © 2021 EN-Jakee Association. All Rights Reserved.")


if __name__ == "__main__":
    main()
