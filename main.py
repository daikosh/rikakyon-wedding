import os
import datetime as dt
import importlib

import streamlit as st
from PIL import Image

homepage = importlib.import_module("01_homepage.main")
radio = importlib.import_module("02_radio.main")
profile = importlib.import_module("03_profile.main")
party = importlib.import_module("04_about.main")
radio_glee = importlib.import_module("05_radio_glee.main")
rikako = importlib.import_module("06_rikako.main")
timeline = importlib.import_module("07_timeline.main")
cat = importlib.import_module("08_cat.main")


# パラメータの設定
USERNAME = "rikakyon"
PASSWORD = "0326"


# ページ設定
st.set_page_config(
    page_title="結婚式二次会 特設サイト",
    page_icon="🎊",
    initial_sidebar_state="expanded"
)
max_width = 1000
padding_top = 1
padding_right = 2.5
padding_left = 2.5
padding_bottom = 1
COLOR = "black"
BACKGROUND_COLOR = "white"
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
st.markdown(set_width_style, unsafe_allow_html=True)


# Streamlitのメニューやフッターを隠す
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# メインクラス
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

    def is_released(self, release_time):
        """公開時刻になったとき"""

        # 現在時刻
        current_time = dt.datetime.now() + dt.timedelta(hours=9)

        # 現在時刻がリリース時間になった場合
        if current_time >= release_time or self.debug is True:
            return True

        # 現在時刻がリリース時間になっていない場合
        else:
            return False

    def is_authenticated(self, username, password):
        """認証"""
        if username == USERNAME and password == PASSWORD:
            return 1
        elif username == USERNAME and password == "0622":
            return 2
        else:
            return 0

    def write_text(self, text, fontsize, align):
        """テキストを表示"""
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def show_image(self, imgpath):
        """画像を表示"""
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")

    def show_logo(self, selection):
        """ロゴを表示"""
        if selection == "GREETING":
            self.logo.image(Image.open('logo.png'), use_column_width="auto")
        elif selection == "ABOUT":
            self.logo.image(Image.open('04_about/logo.png'), use_column_width="auto")
        elif selection == "PROFILE":
            self.logo.image(Image.open('03_profile/logo.png'), use_column_width="auto")
        elif selection == "マツイキョースケのオールナイトニッポン🍆📻":
            self.logo.image(Image.open('02_radio/logo.png'), use_column_width="auto")
        elif selection == "わんこ旅🐶📷":
            self.logo.image(Image.open('06_rikako/logo.png'), use_column_width="auto")
        elif selection == "みんなのにゃんこ🐱":
            self.logo.image(Image.open('08_cat/logo.png'), use_column_width="auto")
        elif selection == "TIMELINE":
            self.logo.image(Image.open('07_timeline/logo.png'), use_column_width="auto")
        elif selection == "同響グリークラブのオールナイトニッポン０🕺🕺🕺🕺":
            self.logo.image(Image.open('05_radio_glee/logo.png'), use_column_width="auto")

    def open(self):
        # メインロゴ (縁) を表示
        self.main_logo = st.empty()
        self.main_logo.image(Image.open('logo.png'), use_column_width="auto")
        st.title("このホームページは移転しました")
        st.write("[移転先のページ](https://enjakee-pj.herokuapp.com/)")

        # # ログインセクションを表示
        # login_expander = st.beta_expander("ログインセクション / Login Section", expanded=True)
        # username = login_expander.text_input("ユーザ名 / Username")
        # password = login_expander.text_input("パスワード / Password", value="", type="password")
        # login_expander.markdown("""こちらは招待者専用のホームページです。URLやログイン情報は絶対に流出させないでください。""")


        

        # 通常ログインした場合
        # if self.is_authenticated(username, password) == 1:
        #     # メインロゴ (縁) ブロックを消去
        #     self.main_logo.empty()
        #     # ログインに成功しましたと表示
        #     login_expander.success("Logged / ログインに成功しました。")
        #     # デバッグモードオフ
        #     self.debug = False

        #     # タイトルの表示
        #     self.write_text("響介&理香子<br>結婚式二次会<br>特設サイト", 34, "center")

        #     # ロゴの表示位置を固定
        #     self.logo = st.empty()

        #     # コンテンツメニューの表示
        #     selection = st.radio("", list(self.pages.keys()))
        #     self.show_image('line.png')

        #     # 選択肢に応じたロゴを固定した位置に表示
        #     self.show_logo(selection)

        #     # コンテンツページの表示
        #     page = self.pages[selection]
        #     page.main(self.debug)

        # # デバッグモードでログインした場合
        # elif self.is_authenticated(username, password) == 2:
        #     # メインロゴ (縁) を消去
        #     self.main_logo.empty()
        #     # デバッグモードと表示
        #     login_expander.success("Debug Mode / デバッグモード！！！")
        #     # デバッグモード音
        #     self.debug = True

        #     # タイトルの表示
        #     self.write_text("響介&理香子<br>結婚式二次会<br>特設サイト", 34, "center")

        #     # ロゴの表示位置を固定
        #     self.logo = st.empty()

        #     # コンテンツメニューの表示
        #     selection = st.radio("", list(self.pages.keys()))
        #     self.show_image('line.png')

        #     # 選択肢に応じたロゴを固定した位置に表示
        #     self.show_logo(selection)

        #     # コンテンツページの表示
        #     page = self.pages[selection]
        #     page.main(self.debug)

        # フッターの表示
        imgpath = "line.png"
        self.show_image(imgpath)
        st.write("Copyright © 2021 EN-Jakee Association. All Rights Reserved.")


if __name__ == "__main__":
    # インスタンスの生成
    mainpage = Mainpage()
    mainpage.open()
