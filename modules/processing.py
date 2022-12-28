from xml.etree.ElementPath import get_parent_map
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




#分割処理
def split_img(input,rows,cols):
    input_img = get_parent_path()+'/static/images/process/'+input
    #print(input_img)
    img=cv2.imread(input_img)
    chunks = []
    for row_img in np.array_split(img, rows, axis=0):
        for chunk in np.array_split(row_img, cols, axis=1):
            chunks.append(chunk)
    #print(len(chunks))
    output_img = get_parent_path() + '/static/images/split/'
    for i, chunk in enumerate(chunks):
        cv2.imwrite(output_img+f"chunk_{i:02d}.png",chunk)
    


#debug用コード
if __name__ == "__main__":
    
    images = 'sample.png'
    #print(get_current_path())
    #print(get_parent_path())

    rows=3
    cols=4
    split_img(images,rows,cols)
    