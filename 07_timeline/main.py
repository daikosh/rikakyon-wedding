import os
import datetime as dt

import streamlit as st
from PIL import Image, ImageOps


# メインクラスを表示
class Timeline(object):
    def __init__(self, debug):
        self.debug = debug

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

    def show_image(self, imgpath):
        """画像を表示"""
        if os.path.exists(imgpath):
            image = Image.open(imgpath)
            st.image(image, use_column_width="auto")

    def write_text(self, text, fontsize=18, align="left"):
        """テキストを表示"""
        new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
        st.markdown(new_text, unsafe_allow_html=True)

    def open_timeline_expander(self, title, imgpath, expanded):
        """タイムラインエクスパンダーを表示"""
        with st.beta_expander(title, expanded=expanded):
            self.show_image(imgpath)

    def open(self):
        """コンテンツページを表示"""

        # 説明文を表示
        st.markdown("""
            地球上に、今さ、人口って何人いるか知ってる？76億人いるの。

            76億人に、一人に一秒しか会わなくても240年かかるの。

            それが俺たちどう？もう出会って8年以上たってる。

            奇跡、乾杯！
        """)
        self.show_image("line.png")

        # 第1章幼少期を表示
        self.open_timeline_expander("第1章 幼少期編", "07_timeline/01.png", False)

        # 第2章中高生時代を表示
        with st.beta_expander("第2章 中高生編", expanded=True):
            self.show_image("07_timeline/02_1.png")
            self.show_image("07_timeline/02_2.png")
            self.show_image("07_timeline/02_3.png")

        # 第3章大学1回生を表示
        self.open_timeline_expander("第3章 大学1回生編", "07_timeline/03.png", True)
        # self.open_timeline_expander("第4章 大学編 2回生", "07_timeline/01.png", True)
        # self.open_timeline_expander("第5章 大学編 3回生", "07_timeline/01.png", True)
        # self.open_timeline_expander("第6章 大学編 4回生", "07_timeline/01.png", True)
        # self.open_timeline_expander("第7章 社会人", "07_timeline/01.png", True)
        # self.open_timeline_expander("番外編 EVE祭", "07_timeline/01.png", True)
        # self.open_timeline_expander("番外編 プロポーズ", "07_timeline/01.png", True)
        # self.open_timeline_expander("番外編 新婚生活", "07_timeline/01.png", True)
        # self.open_timeline_expander("番外編 老後", "07_timeline/01.png", True)

        # To be continued ... を表示
        st.write("To be continued ...")


# メイン関数
def main(debug):
    # インスタンスを生成
    timeline = Timeline(debug)
    timeline.open()


if __name__ == "__main__":
    main(debug)
