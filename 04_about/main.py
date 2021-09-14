import os

import streamlit as st
from PIL import Image, ImageOps


# メインクラス
class About(object):
    def __init__(self, debug):
        self.debug = debug

    def open(self):
        """コンテンツページを表示"""

        # 結婚式二次会情報を表示
        st.markdown("""
            【結婚式二次会情報】

            日時: 2022年3月26日 (土)

            会場: 未定
        """)


# メイン関数
def main(debug):
    # インスタンスを生成
    about = About(debug)
    about.open()


if __name__ == "__main__":
    main(debug)
