from flask import Flask, request, render_template
import glob  # ファイルの一覧を取得用に使用
import os  # パス操作用に使用

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'images/normal')

@app.route('/')
def index():
    # テスト用トップページを表示させる
    return render_template("testTopPage.html")

@app.route('/selected_Img')
def showSelectedImg():
    # アップロードされた画像を表示させる
    app.config['UPLOAD_FOLDER'] = IMG_FOLDER
    IMG_LIST = os.listdir('static/images/normal')
    imagePaths = []
    for file in IMG_LIST:
        imagePaths.append({
            "filename": file,
            "url": 'images/normal/' + file
        })
    return render_template("selected_Img.html", image_List=imagePaths)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(port=5002,debug=True)