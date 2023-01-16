from flask import Flask, redirect, request, render_template, url_for
import glob  # ファイルの一覧を取得用に使用
import os  # パス操作用に使用
import time

from modules import score, timer, c_json

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'images/normal')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route('/')
def index():
    # テスト用トップページを表示させる
    return render_template("testTopPage.html")

# @app.route('/upload', methods=['GET', 'POST'])#画面2
# def upload():
#     # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
#     if request.method == 'GET':
#         return render_template('upload.html')

# @app.route('/selected_Img')
# def showSelectedImg():
#     # アップロードされた画像を表示させる
#     IMG_LIST = os.listdir('static/images/normal')
#     imagePaths = []
#     for file in IMG_LIST:
#         imagePaths.append({
#             "filename": file,
#             "url": 'images/normal/' + file
#         })
#     return render_template("selected_Img.html", image_List=imagePaths)

# 画面2(画像選択、画像追加)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
    if request.method == 'GET':
        # アップロードされた画像を表示させる
        IMG_LIST = os.listdir('static/images/normal')
        imagePaths = []
        for file in IMG_LIST:
            imagePaths.append({
                "filename": file,
                "url": 'images/normal/' + file
            })
        return render_template("image-select.html", image_List=imagePaths)
    # formでsubmitボタンが押されるとPOSTリクエストとなるのでこっち
    elif request.method == 'POST':
        file = request.files['image_file']
        filename = file.filename
        file.save(os.path.join('static/images/normal', filename))
        return redirect(url_for('upload'))  # /uploadを再ロード


@app.route('/game')  # 画面5
def game():
    timer.start = time.time()  # スタート時間
    return render_template('game.html')


@app.route('/fin')  # 画面6
def fin():
    # 経過時間計算
    timer.end = time.time()
    sec = int(timer.end - timer.start)  # ゲームにかかった秒数
    dict = {'time': sec}
    c_json.update_json(dict)  # jsonファイルに秒数を保存
    return render_template('game.html')  # ここのreturnは適当


@app.route('/show')  # 画面7
def show():
    score_h = score.read_csv()
    return render_template('show.html', arr=score_h)


@app.route('/page4', methods=["GET"])
def page4():
    img_Name = ""

    if request.args.get('img_Name') is not None:
        img_Name = request.args.get('img_Name')
    else:
        img_Name = "パラメーターがないよ"
    return render_template("testPage4.html", img_Name=img_Name)


@app.route('/gameEnd', methods=["GET"])
def gameEnd():
    score_array = [7000, 100, 50]
    return render_template("game-end.html", score_array=score_array)


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(port=5000, debug=True)
