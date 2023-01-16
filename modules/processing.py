import time
import cv2
import numpy as np
import os

#ファイル内でのディレクトリ構造の統一のためにカレントディレクトリと親ディレクトリの位置を取得する関数を導入
def show_cur_pare_path():
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, '..'))
    print(base)
    print(name)
#カレントディレクトリの絶対パスを取得
def get_current_path():
    base = os.path.dirname(os.path.abspath(__file__))
    return base
#親ディレクトリ(一つ上のディレクトリ)の絶対パスを取得(module内の関数ならFreeSubjectまでのパスを取得)
def get_parent_path():
    base = get_current_path()
    name = os.path.normpath(os.path.join(base, '..'))
    return name

#images のパスを取得
def get_images_path():
    name = get_parent_path()+'/static/images/'
    return name

#images内 のパスを取得
def get_img_select_path(imgtype):
    name = get_images_path()+imgtype+'/'
    return name

####


#分割処理
def split_img(input,rows,cols):
    root,ext = os.path.splitext(input)
    input_img = get_img_select_path('process')+input
    #print(input_img)
    img=cv2.imread(input_img)
    chunks = []
    for row_img in np.array_split(img, rows, axis=0):
        for chunk in np.array_split(row_img, cols, axis=1):
            chunks.append(chunk)
    #print(len(chunks))
    output_img = get_img_select_path('split')
    for i, chunk in enumerate(chunks):
        cv2.imwrite(output_img+f"chunk_{i}"+ext,chunk)

#split内の分割画像を削除
def del_split():
    dir = get_img_select_path('split')
    for f in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,f)):
            os.remove(os.path.join(dir,f))



    


#debug用コード
if __name__ == "__main__":
    
    image1 = 'sample.png'
    image2 = 'input1.jpg'
    #print(get_current_path())
    #print(get_parent_path())

    rows=3
    cols=3
    split_img(image1,rows,cols)
    #5秒後にディレクトリ内の分割画像を削除する
    time.sleep(15)
    del_split()