from flask import Flask, render_template, request, url_for, redirect
import os, time

from modules import score, timer, c_json

app = Flask(__name__)


#ファイルダイアログの表示と画像のアップロード
@app.route('/upload', methods=['GET', 'POST'])#画面2
def upload():
    # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
    if request.method == 'GET':
        return render_template('upload.html')
    # formでsubmitボタンが押されるとPOSTリクエストとなるのでこっち
    elif request.method == 'POST':
        file = request.files['image_file']
        filename = file.filename
        file.save(os.path.join('static/images/normal', filename))
        return redirect(url_for('upload'))#/uploadを再ロード

@app.route('/game')#画面5
def game():
    timer.start = time.time()#スタート時間
    return render_template('game.html')

@app.route('/fin')#画面6
def fin():
    #経過時間計算
    timer.end = time.time()
    sec = int(timer.end - timer.start)#ゲームにかかった秒数
    dict = {'time': sec}
    c_json.update_json(dict)#jsonファイルに秒数を保存
    return render_template('game.html')#ここのreturnは適当

@app.route('/show')#画面7
def show():
    score_h = score.read_csv()
    return render_template('show.html', arr=score_h)

if __name__ == '__main__':
    app.run(debug=True)