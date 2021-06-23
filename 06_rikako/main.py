import streamlit as st
from PIL import Image, ImageOps
import os
## Parameters ##


## functions ##
def initialization():
    pass

def show_image(imgpath, type):
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format=type, use_column_width="auto")

def write_text(text, fontsize=18, align="left"):
    new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main():
    initialization()

    ## Body ##
    with st.beta_expander("Vol.1 梅雨を楽しむ紫陽花", expanded=True):
        dir_path = "06_rikako/vol.1/"
        for n in range(1, 28):
            show_image(dir_path + str(n).zfill(2) + ".jpg", "jpg")

            if n == 2:
                write_text("先日、奈良のお寺、「長弓寺」に早朝散歩に出掛けた。")
                write_text("あいにくの雨。")
                write_text("でも紫陽花を撮るなら悪くないなと、雨の日ならではの写真を撮ろうと意気込んで行った。")
            elif n == 4:
                write_text("カタツムリを発見！")
                write_text("超ミニサイズ。(寄りすぎて分からない)")
                write_text("よくみるといっぱいいる。")

            elif n == 5:
                write_text("カタツムリはマクロレンズで寄っても逃げないのでとても撮りやすい。")

            elif n == 6:
                write_text("うなだれてしまった。")
                write_text("")
                write_text("")
                write_text("かなりアクセスは悪いけど穴場スポット。")

            elif n == 7:
                write_text("次は、同じ場所かと思いきや、こちらはかの有名な清水寺。")

            elif n == 8:
                write_text("寄りで撮ったらどこで撮っても場所は関係ない。")
                write_text("というわけで清水寺の紫陽花は以上。")

            elif n == 9:
                write_text("続きましてこちらは京都の三室戸寺。")

            elif n == 10:
                write_text("最近なんか花が小さい？ような気もするけど、だいぶ何年も撮りに出掛けた場所。")
                write_text("(厳密にいうと花ではなくガク)")

            elif n == 11:
                write_text("多種多様な紫陽花に圧倒される。")

            elif n == 12:
                write_text("マクロレンズを手に入れるまではこれ以上寄るとピントが合わないのでこれが精一杯。")
                write_text("でも壁紙には良いかも？と思って定番ショット化していた。")
                write_text("が、なかなか画角一杯にまっすぐ入るような立派な紫陽花を見つけるのがまた難しい。")

            elif n == 13:
                write_text("紫陽花を見た帰りに近くのカフェへ。")
                write_text("炭酸水を入れると色が変わる、紫陽花ドリンク。")
                write_text("")
                write_text("さっきの写真となんとなくアプリで二重露出してみると…")

            elif n == 14:
                write_text("あらなんとまあ爽やかなドリンク！")
                write_text("二重露出編の集に目覚めたきっかけのショット。")

            elif n == 15:
                write_text("一緒に食べたたまごサンドが美味でした…")
                write_text("")
                write_text("宇治の三室戸寺近くのカフェ。")
                write_text("RAKU CAFE")
                write_text("京都府宇治市宇治又振65 ")
                write_text("")
                write_text("女子受け間違いなし。")

            elif n == 17:
                write_text("続きましては再び奈良へ。")

            elif n == 18:
                write_text("ここ最近見つけた新たな紫陽花スポット。")
                write_text("奈良の「矢田寺」。")

            elif n == 20:
                write_text("大きな紫陽花が山一面に咲き誇っていて紫陽花のトンネルのよう。")

            elif n == 21:
                write_text("紫陽花と着物。素敵。")

            elif n == 23:
                write_text("風呂敷もまたよく合う。")
                write_text("個人的意見ですが、服を持ち運ぶ時は基本風呂敷を使う派です。")
                write_text("袋だと出し入れしにくい一方、風呂敷はさっと広げて綺麗に収納出来る上に、嵩張らない。おすすめです。")

            elif n == 25:
                write_text("服に限らず、バッグや水筒代わりに。")

            elif n == 26:
                write_text("そんなこんなで矢田寺は本当におすすめです。")

            elif n == 27:
                write_text("以上紫陽花だけのコラムでした。")
                write_text("")
                write_text("梅雨の時期も紫陽花の時期ももうすぐ終わりますが、まだ間に合う！")
                write_text("寄りで撮れば道端の紫陽花でも十分綺麗です。")
                write_text("是非梅雨の花に目を向けてみてはいかがでしょうか。")
                write_text("")
                write_text("次回コラムもお楽しみに！")
                write_text("理香子", align="right")

if __name__ == "__main__":
    main()
