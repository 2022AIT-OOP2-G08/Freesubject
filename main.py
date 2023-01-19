from flask import Flask, redirect, request, render_template, url_for
import glob  # ファイルの一覧を取得用に使用
import os  # パス操作用に使用
import time
import random

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

@app.route('/game-play')
def gameplay():
    # アップロードされた画像を表示させる
    app.config['FOLDER'] = 'static/images/normal/'
    # file = glob.glob("static/images/normal/*.png")
    path = app.config['FOLDER'] + "sample2.jpeg"
    # print(file)
    paths = {"filename": os.path.basename(path), "url": "/images/uploaded/" + os.path.basename(path)}
    print(paths["filename"],paths['url'])
    
    # 分割した画像を取得する
    app.config['SPLIT'] = 'static/images/split/'
    files = glob.glob(app.config['SPLIT']+ '*')
    print(files.sort())
    random.shuffle(files)
    split_path = []
    file_count = []
    count = 1
    for file in files:
        fname = os.path.basename(file)
        fid = fname.split('.')
        split_path.append({
            "id": fid[0],
            "filename": os.path.basename(file),
            "url": "/images/split/" + os.path.basename(file)
        })
        file_count.append(count)
        count += 1
    
    print(file_count)
    split_file_count = [file_count[idx:idx + 3] for idx in range(0,len(file_count), 3)]
    print(split_file_count)
    
    return render_template("game-play.html", file=paths, split_file_count=split_file_count, target_files=split_path)

@app.route('/game-clear')
def gameclear():
    path = "static/images/normal/sample2.jpeg"
    return render_template("game-clear.html", path=path)

@app.route('/images/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['FOLDER'], filename)

@app.route('/images/split/<path:filename>')
def split_file(filename):
    return send_from_directory(app.config['SPLIT'], filename)


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
