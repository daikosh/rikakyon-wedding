import streamlit as st
from PIL import Image, ImageOps
import os
import datetime
## Parameters ##


## functions ##
def initialization():
    pass

def show_image(imgpath, type):
    if os.path.exists(imgpath):
        image = Image.open(imgpath)
        st.image(image, output_format=type, use_column_width="auto")

def write_text(text, fontsize=16, align="left"):
    new_text = '<p style="font-family:sans-serif; text-align: {}; font-size: {}px;">{}</p>'.format(align, fontsize, text)
    st.markdown(new_text, unsafe_allow_html=True)

def main(debug):
    initialization()

## Vol.1 ##
    with st.beta_expander("Vol.1 梅雨を楽しむ紫陽花", expanded=False):
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

    NOW_TIME = datetime.datetime.now() + datetime.timedelta(hours=9)
    RELEASE_TIME = datetime.datetime(2022, 7, 4, 19, 00)
    if RELEASE_TIME < NOW_TIME or debug is True: # リリース時間になったとき
## Vol.2 ##
            with st.beta_expander("Vol.2 住むように過ごす 京都STAY 1", expanded=True):
                dir_path = "06_rikako/vol.2/"
                for n in range(1, 23):
                    show_image(dir_path + str(n).zfill(2) + ".jpg", "jpg")
                    if n == 1:
                        st.markdown("""
                            今回のコラムは京都のホテル#1

                            近年異常な程、京都にホテルが増えている。
                            スタイリッシュで近代的な設えの宿もあれば、古き良き風情を残している宿もある。が、全て共通して「京都らしさ」は大事にされている印象を受ける。

                            海外旅行に行けなくなり、国内でゆったり過ごす所謂「大人旅」をするようになり、食の開拓にも若干飽きつつある中(といっても開拓し続けているが)、ホテル巡りが最近の私のブーム。

                            旅行に特化したクレジットカードを造り、あらゆる旅行アプリを駆使し、ポイントと特典で良いホテルに泊まるスキルが極まってきた。

                            今回は、これまで私が泊まったことのある京都のホテルを紹介。たくさんあるため次回vol.3に続く2回シリーズでお届けします。

                            京都に訪れた、又は戻ってきた時の旅の候補、そして3月26日の宿泊先の候補としても参考になれば幸いです。
                        """)
                    elif n == 2:
                        st.markdown("""
                            1つ目は  THE 王道！「ホテルグランヴィア京都」
                            えびちゃんこと、海老原先生の御来団時のご所望宿泊先ですね。

                            今回はなんとスイートルーム。
                            コロナ禍により海外からの観光客が減った京都では、どこの宿も異常な程、宿泊代が安い…！
                            訪問時はgo to travelもあり、スイートルームとは思えないどころかビジネス並みのお値段で宿泊。
                        """)
                    elif n == 3:
                        st.markdown("""
                            ゆったりとしたソファが並べられ、その横にはテレビと冷蔵庫。そしてベッドの前にもテレビ。
                            こんな部屋に2台もテレビがあっても、むしろテレビ見るなんて勿体ない。と思える。
                        """)
                    elif n == 4:
                        st.markdown("""
                            ちょうど同響の定演のライブ配信日だったため、この優雅な部屋で山下先生指揮の優雅な音楽を楽しめた。(これはスマホで見るという…)

                        """)
                    elif n == 5:
                        st.markdown("""
                            スイートルームはグランヴィアフロアにあるため、専用の「フロアラウンジ」を利用出来る。
                            お菓子やおつまみ、お茶やお酒まで自由に楽しめ、専用コンシェルジュがいるため混雑を避けてゆっくりとチェックアウトが出来る。
                        """)
                    elif n == 7:
                        st.markdown("""
                            部屋から変化していく空色と京都タワーを永遠に眺められる。いつも見る光景がちょっと特別に感じられた。

                        """)
                    elif n == 8:
                        st.markdown("""
                            朝食もまた京都を眺めながら。鶏肉かオムレツの2択で選べる朝から豪華なモーニング。

                            王道のグランヴィアこそ、案外お手軽価格で泊まれるため新幹線移動になる人にはとてもオススメ。
                        """)
                    elif n == 9:
                        st.markdown("""
                            2つ目は二条城の目の前に位置する「CANATA  KYOTO」

                            実はANAクラウンプラザホテルの真横にあり、髙橋夫妻 (りょーいちさん、ごっちん先輩) の結婚パーティーの時にアクセスが良すぎて最高だった場所。改めておめでとうございます！
                        """)
                    elif n == 10:
                        st.markdown("""
                            まずこの鍵。この鍵だけでテンションが上がる。
                            「マットな質感」が個人的に好きでそれを凝縮しているようなこの鍵から全てが始まる素敵なお部屋。
                        """)
                    elif n == 11:
                        st.markdown("""
                            グレーの統一感と、お洒落なインテリアに囲まれて落ち着いた時間を過ごすことが出来る。
                            今回は一休のクーポンを利用して宿泊。お高い方のお部屋であれば、二条城を望むテラスがどーんとあり、夜の一杯、朝のヨガなどしたらまさに絵に描いたようなホテルステイ。
                        """)
                    elif n == 12:
                        st.markdown("""
                            3つ目は祇園に位置する「ザ セレスティン京都祇園」

                            こちらは法人の社割を利用して宿泊。
                            これも個人的にどタイプ。八坂にも花見小路にも近く、入口から観光地感漂う。落ち着いたラウンジに、大浴場もあり、部屋から浴衣で移動出来る。
                            部屋には老舗日本茶専門店・一保堂のお茶、西川貞三郎商店プロデュースの清水焼の茶器が用意されており、タオルは今治タオル。上質の極み…。
                        """)
                    elif n == 14:
                        st.markdown("""
                            扉を開けると和を感じる設。

                            三井不動産の宿で、二条城前にあった国際ホテルが建て直され新しく出来たHotel The Mitsui  Kyotoも系列でかーーなり気になっているものの高すぎてハードルが高い…まずはレストラン利用から攻めようと検討中。
                        """)
                    elif n == 15:
                        st.markdown("""
                            4つ目はアートが融合されたホテル「node hotel」

                            部屋ごとに飾られているアートが異なり、アーティストの紹介もされている。グレーを基調とした無機質さがよりスタイリッシュさを際立たせる。
                            この宿も個人的に超タイプ。ソファにライトにインテリア全て欲しくなる。
                        """)
                    elif n == 17:
                        st.markdown("""
                            朝からおしゃれ家電の代名詞バルミューダのポットで珈琲を。
                        """)
                    elif n == 18:
                        st.markdown("""
                            一階のレストランは宿泊者以外も利用出来る。
                            宿に戻ってきて一杯だけ飲んで部屋に帰るというのも最近の個人的な楽しみ方。
                        """)
                    elif n == 19:
                        st.markdown("""
                            5つ目は「ザ ジェネラル 京都」
                            実は結婚式会場であるフォーチュンガーデン京都から紹介してもらえる宿の1つ。
                            今回は式場成約特典として無料宿泊券をゲット。
                        """)
                    elif n == 20:
                        st.markdown("""
                            ウェルカムフードに箱入りお団子をいただき、お部屋でゆっくり食せる。
                            部屋に空きがあったため、たった1000円でワンランク部屋タイプをアップしてもらえた。
                        """)
                    elif n == 21:
                        st.markdown("""
                            今回は「高辻富小路」の宿で、中庭にはシンボリックなケラマツツジが植えられている。
                        """)
                    elif n == 22:
                        st.markdown("""
                            朝食はレストランにて「tgkのtkg」(「ザ ジェネラル京都の卵かけご飯」)と題された、卵かけご飯を食した。ラウンジでも朝食にフリーでパンをいただくこともできる。
                        """)
                        st.markdown("""
                            今回は5つホテルを紹介。
                            長くなってしまうので今回はここまで。

                            泊まってみたい宿はありましたか？

                            次回は今っぽい宿と、京町家を生かした京都らしい宿をご紹介。

                            次回コラムもお楽しみに！
                        """)
                        write_text("理香子", align="right")


if __name__ == "__main__":
    main(debug)
