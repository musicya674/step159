from flask import Flask, request
from datetime import datetime
import pytz, random

# Flaskのインスタンスをappという名前で作成
app = Flask(__name__)

# localhost:5000にアクセスした時の処理
@app.route('/', methods=['GET'])
def raretech_message():
    return '夢は、目標に向かって毎日歩みを進めた者だけが叶えられる。\
            今日の二時間は、その一歩だ'


# /timeへgetでアクセスしたら現在時刻を知らせる
@app.route('/time', methods=['GET'])
def current_time():
    # 現在の日時
    now = datetime.now(pytz.timezone('Asia/Tokyo'))
    formatted_date_time = now.strftime("%Y年%m月%d日　%H時%M分%S秒")
    return f"現在時刻は{formatted_date_time}です"


# 入力した日付から曜日を算出
@app.route('/date', methods=['POST'])
def week_day():
    """
    コマンド例: curl -X POST -d 'days=2022-10-03' http://localhost:5000/date
    """

    w_list = ['月曜日', '火曜日', '水曜日' , '木曜日', '金曜日', '土曜日', '日曜日']
    input_date = request.form.get('days')

    # 受け取った文字を日付に変換する
    date = datetime.strptime(input_date, '%Y-%m-%d')

    # 日付を曜日に変換する
    week = date.weekday()

    return f'{date.strftime("%Y年%m月%d日")}は{w_list[week]}'


# /aphorismへアクセスすると、名言をランダムに返す
@app.route('/aphorism', methods=['GET'])
def aphorism():
    aphorism_words = ['Done is better than perfect.',
                      'Stay hungry, stay foolish',
                      'We are What We Choose',
                      'Our greatest weakness lies in giving up.\
The most certain way to succeed is always \
to try just one more time.']
    
    selected_word = random.choice(aphorism_words)

    return selected_word


# ポジティブおみくじ
@app.route('/fortune', methods=['GET'])
def fortune():
    options =  [
        '大吉',
        '吉',
        '中吉',
        '小吉',
        '末吉',
        # '凶',
        # '大凶',
    ]

    selected = random.choice(options)

    if selected == '大吉':
        return f'おめでとう!!!{selected}です!!今日は最高な1日になりますよ!'
    else:
        return f'今日の運勢は{selected}です!頑張りましょう!'



if __name__ == "__main__":
    app.run()