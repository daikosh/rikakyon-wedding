import streamlit as st
import importlib
homepage = importlib.import_module("01_homepage.main")
radio = importlib.import_module("02_radio.main")

## Parameters ##
USERNAME = "rikakyon"
PASSWORD = "0326"

## Page Config ##
st.set_page_config(
    page_title="犬飼響介 結婚式 2次会専用HP",
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
        "ご挨拶": homepage,
        "マツイキョースケのオールナイトニッポン🍆📻": radio
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

def generate_text(blocks):
    blocks[0].title("犬飼響介 結婚式 2次会専用HP")
    blocks[1].info("Authorized Personnel Only")
    blocks[2].subheader("こちらは招待者専用のホームページです。URLやログイン情報は流出させないでください。")

def clear_blocks(blocks):
    for block in blocks:
        block.empty()

def main():
    initialization()
    ## sidebar ##
    login_expander = st.beta_expander("ログインセクション / Login Section", expanded=True)
    username = login_expander.text_input("ユーザ名 / Username")
    password = login_expander.text_input("パスワード / Password", value="", type="password")
    login_checkbox = login_expander.checkbox("ログイン / LOGIN")

    ## Body ##
    blocks = generate_blocks()
    generate_text(blocks)
    if login_checkbox:
        if is_authenticated(username, password):
            clear_blocks(blocks)
            # login_expander.success("Logged / ログインに成功しました。")
            selection = st.radio("", list(PAGES.keys()))
            page = PAGES[selection]
            page.main()
        else:
            st.warning("ユーザ名またはパスワードが間違っています / Incorrect Username or Password")

    ## Footer ##
    st.write("Copyright © 2021 Inukai-Kyosuke Wedding Association. All Rights Reserved.")
    #st.sidebar.write("Copyright © 2021 Inukai-Kyosuke Wedding Association. All Rights Reserved.")

if __name__ == "__main__":
    main()
