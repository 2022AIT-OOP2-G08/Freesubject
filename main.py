from flask import Flask, request, render_template, jsonify, send_from_directory
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する
import glob  # ファイルの一覧を取得用に使用
import os  # パス操作用に使用
import random

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return gameplay()

# http://127.0.0.1:5000/
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
    files = glob.glob(app.config['SPLIT'] + "sample2/*")
    print(files.sort())
    random.shuffle(files)
    split_path = []
    file_count = []
    count = 1
    for file in files:
        split_path.append({
            "id": str(count),
            "filename": os.path.basename(file),
            "url": "/images/split/"+ "sample2/" + os.path.basename(file)
        })
        file_count.append(count)
        count += 1
    
    print(file_count)
    split_file_count = [file_count[idx:idx + 3] for idx in range(0,len(file_count), 3)]
    print(split_file_count)
    
    return render_template("game-play.html", file=paths, split_file_count=split_file_count, target_files=split_path)

@app.route('/game-clear')
def gameclear():
    path = "static/images/normal/sample.png"
    return render_template("game-clear.html", path=path)

@app.route('/images/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['FOLDER'], filename)

@app.route('/images/split/<path:filename>')
def split_file(filename):
    return send_from_directory(app.config['SPLIT'], filename)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)