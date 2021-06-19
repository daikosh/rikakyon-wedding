import streamlit as st
import importlib
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
        #"〇〇〇〇〇のオールナイトニッポン0": radio_glee
        #"二人の生い立ち": homepage,
        #"二人の家族構成": homepage,
        #"犬神家の歴史": homepage,
        #"松井家の歴史": homepage,
        #"同志社交響楽団": homepage,
        #"修道高校": homepage
    }


def is_authenticated(username, password):
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False

def generate_blocks():
    main_title = st.empty()
    main_description = st.empty()
    main_description_eng = st.empty()
    return main_title, main_description, main_description_eng

#def generate_text(blocks):
#    blocks[0].title("犬飼響介 結婚式 2次会専用HP")
#    blocks[1].info("Authorized Personnel Only")
#    blocks[2].subheader("こちらは招待者専用のホームページです。URLやログイン情報は絶対に流出させないでください。")

#def clear_blocks(blocks):
#    for block in blocks:
#        block.empty()

def write_text(text, fontsize, color, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; color:{}; font-size: {}px;">{}</p>'.format(align, color, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main():
    initialization()
    ## Login Section ##
    login_expander = st.beta_expander("ログインセクション / Login Section", expanded=True)
    username = login_expander.text_input("ユーザ名 / Username")
    password = login_expander.text_input("パスワード / Password", value="", type="password")
    #login_button = login_expander.button("ログイン / LOGIN")

    #login_expander.info("Authorized Personnel Only")
    login_expander.subheader("こちらは招待者専用のホームページです。URLやログイン情報は絶対に流出させないでください。")

    ## Body ##
    #blocks = generate_blocks()
    #generate_text(blocks)
    if is_authenticated(username, password):
        #clear_blocks(blocks)
        login_expander.success("Logged / ログインに成功しました。")
        write_text("松井響介・犬飼理香子 結婚式二次会 特設サイト", 32, "black", "center")
        write_text("〜MAY THE FORCE BE WITH YOU〜", 28, "black", "center")
        #st.title("")
        selection = st.radio("", list(PAGES.keys()))
        page = PAGES[selection]
        page.main()
    else:
        pass

    ## Footer ##
    st.write("Copyright © 2021 Inukai-Kyosuke Wedding Association. All Rights Reserved.")
    #st.sidebar.write("Copyright © 2021 Inukai-Kyosuke Wedding Association. All Rights Reserved.")

if __name__ == "__main__":
    main()
