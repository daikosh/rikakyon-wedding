import streamlit as st
from PIL import Image, ImageOps
import os
import datetime

## Parameters ##


## functions ##
def initialization():
    pass

def open_radio_expander(title, imgpath, mp3path, expanded):
    with st.beta_expander(title, expanded=expanded):
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="jpeg", use_column_width="auto")
        if os.path.exists(mp3path):
            audio_file = open(mp3path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')

def write_text(text, fontsize, align):
    new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main(debug):
    initialization()

    st.markdown("""
    マツイキョースケのオールナイトニッポンは結婚式二次会へ向けてなんやかんややっていく番組です。

    毎回ステキなゲストとともにお送りしています！
    """)

    st.write("おたよりは[こちらのフォーム](https://forms.gle/2HiMwgmzzhrxTJ5BA)から募集しています！")

    imgpath = "line.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")

    ## Body ##
    NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
    RELEASE_TIME = datetime.datetime(2021, 8, 14, 13, 00)
    if RELEASE_TIME < NOW_TIME or debug is True: # リリース時間になったとき
        open_radio_expander("#1 「人材紹介業Feeとりがち〜そうだ、顎削ろう〜」【ゲスト: 林寛人、松岡大起】 (2021.5.29 収録)",\
                            '02_radio/01_radio_no1.jpg', '02_radio/01_radio_no1.mp3', False)
        open_radio_expander("#2 「珍名字東京大決戦〜城之内死す〜」【ゲスト: 阿久澤拓也、吉種伸彰】 (2021.6.12 収録)",\
                            '02_radio/02_radio_no2.jpg', '02_radio/02_radio_no2.mp3', False)
        with st.beta_expander("#3 「聴取率を爆上げしたいので、弦のカリスマをゲストに呼びました。」【ゲスト: 和久あさぎ、毛利真夕】 (2021.7.22 収録)", expanded=True):
            image = Image.open('02_radio/03_radio_no3.jpg')
            st.image(image, output_format="jpeg", use_column_width="auto")
            st.write("Part 1/3 「今野さん、毛利さん、お久しぶりです。」 ")
            audio_file = open('02_radio/03_radio_no3.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            # st.write("Part 2/3 「あさぎもーりの今」 ")
            # audio_file = open('02_radio/03_radio_no3.mp3', 'rb')
            # audio_bytes = audio_file.read()
            # st.audio(audio_bytes, format='audio/mp3')
            # st.write("Part 3/3 「あさぎもーりの今」 ")
            # audio_file = open('02_radio/03_radio_no3.mp3', 'rb')
            # audio_bytes = audio_file.read()
            # st.audio(audio_bytes, format='audio/mp3')
    else:
        open_radio_expander("#1 「人材紹介業Feeとりがち〜そうだ、顎削ろう〜」 【ゲスト: 林寛人、松岡大起】 (2021.5.29 収録)",\
                                '02_radio/01_radio_no1.jpg', '02_radio/01_radio_no1.mp3', False)
        open_radio_expander("#2 「珍名字東京大決戦〜城之内死す〜」 【ゲスト: 阿久澤拓也、吉種伸彰】 (2021.6.12 収録)",\
                            '02_radio/02_radio_no2.jpg', '02_radio/02_radio_no2.mp3', True)


    write_text("To be continued ...", 16, "left")
    #open_radio_expander("#3 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/03_radio_no3.jpg', '02_radio/03_radio_no3.mp3', True)
    #open_radio_expander("#4 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/04_radio_no4.jpg', '02_radio/04_radio_no4.mp3', True)
    #open_radio_expander("#5 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/05_radio_no5.jpg', '02_radio/05_radio_no5.mp3', True)
    #open_radio_expander("#6 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/06_radio_no6.jpg', '02_radio/06_radio_no6.mp3', True)
    #open_radio_expander("#7 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/07_radio_no7.jpg', '02_radio/07_radio_no7.mp3', True)
    #open_radio_expander("#8 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/08_radio_no8.jpg', '02_radio/08_radio_no8.mp3', True)
    #open_radio_expander("#9 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/09_radio_no9.jpg', '02_radio/09_radio_no9.mp3', True)
    #open_radio_expander("#10 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/10_radio_no10.jpg', '02_radio/10_radio_no10.mp3', True)


if __name__ == "__main__":
    main(debug)
