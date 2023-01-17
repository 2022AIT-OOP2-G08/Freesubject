from crypt import methods
from flask import Flask, redirect, request, render_template, url_for, jsonify,send_from_directory
import glob  # ファイルの一覧を取得用に使用
import os  # パス操作用に使用
import modules.processing as proapp
import json

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'images/normal')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def index():
    # テスト用トップページを表示させる
    return render_template("testTopPage.html")

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

@app.route('/upload', methods=['GET', 'POST'])#画面2
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
        return redirect(url_for('upload'))#/uploadを再ロード

@app.route('/page4', methods=["GET", "POST"])
def page4():
    proapp.del_split()
    if request.method =="GET":
        return render_template("testPage4.html")
    else:
        img_Name = ""
        if request.form.get('img_Name') is not None:
            img_Name = request.form.get('img_Name')
        else:
            img_Name = "パラメーターがないよ"
        return render_template("testPage4.html", img_Name=img_Name)


@app.route('/page5', methods=["GET", "POST"])
def page5():
    if request.method =="GET":
        return render_template("testPage5.html")
    elif request.method =="POST":
        img_Name = ""
        rows=0
        cols=0
        if request.form.get('img_Name') is not None:
            img_Name = request.form.get('img_Name')
        else:
            img_Name = "パラメーターがないよ"

        if request.form.get('cols', type=int) is not None:
            cols= request.form.get('cols', type=int)
        else:
            cols = "パラメーターがないよ"
        
        if request.form.get('rows', type=int) is not None:
            rows= request.form.get('rows', type=int)
        else:
            rows = "パラメーターがないよ"
        
        
        # アップロードされた画像を表示させる
        app.config['FOLDER'] = 'static/images/process'
        # file = glob.glob("static/images/normal/*.png")
        path = "static/images/process/"+img_Name
        # print(file)
        paths = {"filename": os.path.basename(path), "url": "static/images/process/" + os.path.basename(path)}
        print(paths["filename"],paths['url'])

        proapp.split_img(paths['filename'],rows,cols)
        
        app.config['SPLIT'] = 'sample'
        files = glob.glob("static/images/split/*")
        split_path = []
        i=0
        for file in files:
            name=os.path.basename(file)
            idname=name.split('.')
            split_path.append({
                "filename": name,
                "id": idname[0],
                "url": "static/images/split/" + os.path.basename(file)
            })
            i+=1

        item = [{
            "cols": cols,
            "rows": rows,
        }]
    
        try:
            # 保存処理
            with open('rowcol.json', 'w') as f:
                # インデントや整形の設定を付加して吐き出し
                json.dump(item, f, 
                        ensure_ascii = False,
                        indent = 4,
                        sort_keys = True,
                        separators = (',', ': '))
        except IOError as e:
            # Tracebackの表示
            import traceback
            traceback.print_exc()
        
        return render_template("testPage5.html", file=paths, target_files=split_path)
       


@app.route('/page6')
def correct():
    return render_template("testPage6.html")


@app.route('/gameEnd', methods=["GET"])
def gameEnd():
    score_array = [7000,100,50]
    return render_template("game-end.html", score_array=score_array)



if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(port=5000,debug=True)