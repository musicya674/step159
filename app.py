from flask import Flask
from datetime import datetime
import pytz

# Flaskのインスタンスをappという名前で作成
app = Flask(__name__)

# localhost:5000にアクセスした時の処理
@app.route('/', methods=['GET'])
def hello():
    return 'コメント変更'

# /timeへgetでアクセスしたら現在時刻を知らせる
@app.route('/time', methods=['GET'])
def current_time():
    # 現在の日時
    now = datetime.now(pytz.timezone('Asia/Tokyo'))
    formatted_date_time = now.strftime("%Y年%m月%d日　%H時%M分%S秒")
    return f"現在時刻は{formatted_date_time}です"

if __name__ == "__main__":
    app.run()