import streamlit as st
from PIL import Image, ImageOps
import os
import datetime

## Parameters ##
NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
RELEASE_TIME = datetime.datetime(2021, 8, 7, 13, 00)

class RadioGlee(object):
    def __init__(self, debug):
        self.debug = debug

    def show_image(self, imgpath):
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")

    def open_radio(self, mp3path, format):
        if os.path.exists(mp3path):
            audio_file = open(mp3path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/{}'.format(format))

    def open_radio_expander(self, title, imgpath, mp3path, format, expanded):
        with st.beta_expander(title, expanded=expanded):
            self.show_image(imgpath)
            self.open_radio(mp3path, format)


    def open(self):
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
        self.show_image("line.png")

        ## Body ##
        self.open_radio_expander(
            '#1 「恥ずかしながら帰ってまいりました。」【出演: 阿久澤、松岡、林、松井】',
            '05_radio_glee/radio_1.jpg',
            '05_radio_glee/radio_1.m4a', 'm4a',
            False)
        self.open_radio_expander(
            '#2 「〈TL第1章〉楽器を始めてなかった頃。」【出演: 犬飼、松井、松岡、阿久澤】',
            '05_radio_glee/radio_2.png',
            '05_radio_glee/radio_2.mp3', 'mp3',
            True)
        st.write("To be continued ...")

def main(debug):
    radio_glee = RadioGlee(debug)
    radio_glee.open()

if __name__ == "__main__":
    main(debug)
