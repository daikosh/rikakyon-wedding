import streamlit as st
from PIL import Image, ImageOps
import os
## Parameters ##


## functions ##
def initialization():
    pass

def open_radio_expander(title, imgpath, mp3path):
    with st.beta_expander(title, expanded=True):
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, output_format="jpeg", use_column_width="auto")
        if os.path.exists(mp3path):
            audio_file = open(mp3path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/m4a')

def main(debug):
    initialization()

    st.markdown("""
        Still broader than our land of birth,

        We've learned the oneness of our Earth;

        Still higher than self-love we find

        The love and service of mankind.

        Dear Alma Mater, sons of thine

        Would strive to live the life divine;

        That we may with increasing years have stood

        For Kyosuke, for Rikako, and Brotherhood!
    """)
    st.write("おたよりは[こちらのフォーム](https://forms.gle/eNde9TRwbGpRWnu49)で募集しています！")

    imgpath = "line.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")

    ## Body ##
    open_radio_expander("#1 「恥ずかしながら帰ってまいりました。」 【出演: 阿久澤、松岡、林、松井】", '05_radio_glee/radio_1.jpg', '05_radio_glee/radio_1.m4a')
    st.write("To be continued ...")
    #open_radio_expander("#2 「珍苗字東京大決戦〜城之内死す〜」 【ゲスト: 阿久澤拓也、吉種伸彰】 (2021.6.12 収録)", '02_radio/02_radio_no2.jpg', '02_radio/02_radio_no2.mp3')
    #open_radio_expander("#3 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/03_radio_no3.jpg', '02_radio/03_radio_no3.mp3')
    #open_radio_expander("#4 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/04_radio_no4.jpg', '02_radio/04_radio_no4.mp3')
    #open_radio_expander("#5 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/05_radio_no5.jpg', '02_radio/05_radio_no5.mp3')
    #open_radio_expander("#6 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/06_radio_no6.jpg', '02_radio/06_radio_no6.mp3')
    #open_radio_expander("#7 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/07_radio_no7.jpg', '02_radio/07_radio_no7.mp3')
    #open_radio_expander("#8 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/08_radio_no8.jpg', '02_radio/08_radio_no8.mp3')
    #open_radio_expander("#9 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/09_radio_no9.jpg', '02_radio/09_radio_no9.mp3')
    #open_radio_expander("#10 「」 【ゲスト: ？？？】 (2021.?.? 収録)", '02_radio/10_radio_no10.jpg', '02_radio/10_radio_no10.mp3')


if __name__ == "__main__":
    main(debug)
