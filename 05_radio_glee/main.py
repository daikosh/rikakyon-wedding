import streamlit as st
from PIL import Image, ImageOps
import os
import datetime

## Parameters ##
NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
RELEASE_TIME = datetime.datetime(2021, 8, 7, 13, 00)

## functions ##
def initialization():
    pass

def open_radio_expander(title, imgpath, mp3path, format):
    with st.beta_expander(title, expanded=True):
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")
        if os.path.exists(mp3path):
            audio_file = open(mp3path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/{}'.format(format))

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

        我らの生まれた国よりもまだ広い、地球の一体性を我らは学んだ。
        我らが見つけた自己愛よりも高みにあるのは人類の愛と奉仕だ。
        親愛なる母校、貴方の息子。神聖な人生を送るために努力しよう。
        年を重ねるごとに、我らは立ち上がるのだ。
        響介、理香子、そして我ら兄弟たちのために！
    """)

    st.write("おたよりは[こちらのフォーム](https://forms.gle/eNde9TRwbGpRWnu49)で募集しています！")

    imgpath = "line.png"
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format="png", use_column_width="auto")

    ## Body ##
    if RELEASE_TIME < NOW_TIME or debug is True: # リリース時間になったとき
        open_radio_expander("#1 「恥ずかしながら帰ってまいりました。」【出演: 阿久澤、松岡、林、松井】", '05_radio_glee/radio_1.jpg', '05_radio_glee/radio_1.m4a', 'm4a')
        open_radio_expander("#2 「理香子は天才少女だった！？」〈TIMELINE連携型コンテンツ 幼少期編〉【出演: 犬飼、松井、松岡、阿久沢】", '05_radio_glee/radio_2.png', '05_radio_glee/radio_2.mp3', 'mp3')
        st.write("To be continued ...")
    else:
        open_radio_expander("#1 「恥ずかしながら帰ってまいりました。」【出演: 阿久澤、松岡、林、松井】", '05_radio_glee/radio_1.jpg', '05_radio_glee/radio_1.m4a')
        st.write("To be continued ...")


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
