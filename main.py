from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)


#ファイルダイアログの表示と画像のアップロード
@app.route('/upload', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)