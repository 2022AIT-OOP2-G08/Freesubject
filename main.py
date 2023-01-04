from flask import Flask, render_template, request, url_for, redirect
import os

from modules import score

app = Flask(__name__)


#ファイルダイアログの表示と画像のアップロード
@app.route('/upload', methods=['GET', 'POST'])#画面3
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

@app.route('/game')#画面4
def game():
    return render_template('game.html')

@app.route('/show')#画面7
def show():
    score_h = score.read_csv()
    return render_template('show.html', arr=score_h)

if __name__ == '__main__':
    app.run(debug=True)