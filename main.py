#from crypt import methods
from cv2 import split
from flask import Flask, redirect, request, render_template, url_for, send_from_directory
import glob  # ファイルの一覧を取得用に使用
import os  # パス操作用に使用
import time
import cv2
import random
import modules.processing as processing
import ast

from modules import score, timer, c_json

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'images/normal')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


@app.route('/')
def index():
    # テスト用トップページを表示させる
    return render_template("top.html")

# 画面2(画像選択、画像追加)
@app.route('/select', methods=['GET', 'POST'])
def select():
    # URLでhttp://127.0.0.1:5000/selectを指定したときはGETリクエストとなるのでこっち
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
        return redirect(url_for('select'))  # /selectを再ロード

#画面4(画像加工)
@app.route('/preview', methods=["POST"])
def preview():
    processing.del_process()
    processing.del_split()
    img_Name = ""

    if request.form.get('img_Name') is not None:
        img_Name = request.form.get('img_Name')
        processing.normal(img_Name)
        processing.gray_scale(img_Name)
        processing.mosaic(img_Name)
        processing.inversion(img_Name)
        img_Path = "images/normal/" + img_Name
    else:
        img_Name = "パラメーターがないよ"
    return render_template("image-preview.html", img_Name=img_Name, img_Path=img_Path)


#画面5(パズルゲーム画面)
@app.route('/game-play', methods=['POST'])
def gameplay():
    # アップロードされた画像を表示させる
    app.config['FOLDER'] = 'static/images/process/'
    img_Name = ""
    rowcol=0
    if request.form.get('img_Name') is not None:
        img_Name = request.form.get('img_Name')
    else:
        img_Name = "パラメーターがないよ"

    if request.form.get('rowcol', type=int) is not None:
        rowcol= request.form.get('rowcol', type=int)
    else:
        rowcol = "パラメーターがないよ"
    
    timer.start = time.time()  # スタート時間
    # 画像の分割処理
    processing.split_img(img_Name,rowcol,rowcol)
    
    # パズルピースや完成図の大きさの設定
    img_size=[{'width': "400",'height': "300"},{'width': "350",'height': "350"},{'width': "300",'height': "400"}]
    peace_size=[]
    for size in img_size:
        width = int(size['width']) / rowcol
        height = width * (int(size['height'])/int(size['width']))
        peace_size.append(
            {
                'width': str(width),
                'height': str(height)
            }
        )
    img_type = None
    img = cv2.imread(app.config['FOLDER'] + img_Name)
    h, w, c = img.shape
    
    if(w > h+100):
        img_type = 0
    elif(h > w+100):
        img_type = 2
    else:
        img_type = 1
    
    print("width:" + str(w)+" height:" + str(h) + " img_type:" + str(img_type))
    print(img_size[img_type])
    print(peace_size[img_type])
    
    # file = glob.glob("static/images/normal/*.png")
    path = app.config['FOLDER'] + img_Name
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
    split_file_count = [file_count[idx:idx + rowcol] for idx in range(0,len(files), rowcol)]
    print(split_file_count)
    print("game-play:" + str(img_size[img_type]))
    return render_template("game-play.html", file=paths, split_file_count=split_file_count, target_files=split_path, 
                            rowcol=rowcol, img_Name=img_Name, img_size=img_size[img_type], peace_size=peace_size[img_type])

#画面6(ゲームクリア画面)
@app.route('/game-clear', methods=['POST'])
def gameclear():
    # 経過時間計算
    timer.end = time.time()
    sec = int(timer.end - timer.start -3)  # ゲームにかかった秒数
    img_Name=""
    rowcol=0
    if request.form.get('img_Name') is not None:
        img_Name = request.form.get('img_Name')
    else:
        img_Name = "パラメーターがないよ"
    
    if request.form.get('rowcol', type=int) is not None:
        rowcol= request.form.get('rowcol', type=int)
    else:
        rowcol = "パラメーターがないよ"
    if request.form.get('img_size') is not None:
        img_size = request.form.get('img_size')
    else:
        img_size = "パラメータがないよ"
    # imgmode,nomal = img_Name.split("_")
    imgmode = img_Name.split("_")
    print(imgmode)
    mode_amp = score.mode_score(imgmode[0])
    
    ##スコア計算・csvに上書き
    dict = {'size_amp': rowcol,"mode_amp": mode_amp,'time': sec}
    c_json.update_json(dict)  # jsonファイルに秒数を保存
    score_total = score.calc_score(dict['size_amp'],dict['mode_amp'],dict['time'],score.read_csv())
    #path = processing.get_img_select_path('process')+img_Name
    # print(type(img_size))
    # print("game-clear:" + img_size)
    # print(type(ast.literal_eval(img_size)))
    img_size = ast.literal_eval(img_size)
    
    return render_template("game-clear.html", img_Name=img_Name, score=score_total, img_size=img_size)

@app.route('/images/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['FOLDER'], filename)

@app.route('/images/split/<path:filename>')
def split_file(filename):
    return send_from_directory(app.config['SPLIT'], filename)


# 画面7(スコア表示　タイトルに戻る　同じ難易度で遊ぶ)
@app.route('/game-end', methods=["POST"])
def gameEnd():
    img_Name=""
    if request.form.get('img_Name') is not None:
        img_Name = request.form.get('img_Name')
    else:
        img_Name = "パラメーターがないよ"

    img_split = img_Name.split('_')
    img_normal = ""
    for n in range(len(img_split)):
        if(n > 0):
            img_normal += img_split[n]
            if(n < int(len(img_split))-1):
                img_normal += "_"

    score_array = score.read_csv()
    return render_template("game-end.html", score_array=score_array, img_Name=img_normal)


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(port=5000, debug=True)
