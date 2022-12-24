from flask import Flask, request, render_template, jsonify, send_from_directory
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する
import glob  # ファイルの一覧を取得用に使用
import os  # パス操作用に使用

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return gameplay()

# http://127.0.0.1:5000/
@app.route('/gameplay')
def gameplay():
    # アップロードされた画像を表示させる
    app.config['FOLDER'] = 'static/images/normal'
    # file = glob.glob("static/images/normal/*.png")
    path = "static/images/normal/sample.png"
    # print(file)
    paths = {"filename": os.path.basename(path), "url": "/images/uploaded/" + os.path.basename(path)}
    print(paths["filename"],paths['url'])
    # トップページを表示させる
    # return render_template("page5.html")
    return render_template("gameplay.html", file=paths)

@app.route('/gamecomp')
def gamecomp():
    return render_template("gamecomp.html")

@app.route('/images/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['FOLDER'], filename)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)