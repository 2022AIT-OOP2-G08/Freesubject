import time
import cv2
import numpy as np
import os

#パス取得関数
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

#画像処理関数
def gray_scale(input): #グレースケール化
    img = get_img_select_path('normal')+input
    img_bgr = cv2.imread(img)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray_img',img_gray)
    cv2.imwrite(get_img_select_path('process') + '/gray_' + input,img_gray)
    # cv2.waitKey(0)


def mosaic(input, ratio=0.005): #モザイク化
    img = get_img_select_path('normal')+input
    img_bgr = cv2.imread(img) 
    small = cv2.resize(img_bgr, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    img_mosaic =  cv2.resize(small, img_bgr.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    #cv2.imshow('mosaic_img',img_mosaic)
    cv2.imwrite(get_img_select_path('process') + '/mosaic_' + input,img_mosaic)
    #cv2.waitKey(0)

def line(input): #線画化
    img = get_img_select_path('normal')+input
    gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    neiborhood24 = np.array([[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]],
    np.uint8
    )
    dilated = cv2.dilate(gray, neiborhood24, iterations=1)
    diff = cv2.absdiff(dilated, gray)
    img_line = 255 - diff
    #cv2.imshow('line_img',img_line)
    cv2.imwrite(get_img_select_path('process') + '/line_' + input,img_line)
    #cv2.waitKey(0)

def changecolor(input): #色変化
    img = get_img_select_path('normal')+input
    img_bgr = cv2.imread(img)
    img_hsv = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV) # 色空間をBGRからHSVに変換
    h_deg = 50 #色相(Hue)の回転度数
    s_mag = 2.0 # 彩度(Saturation)の倍率
    v_mag = 1 # 明度(Value)の倍率
 
    img_hsv[:,:,(0)] = img_hsv[:,:,(0)]+h_deg # 色相の計算
    img_hsv[:,:,(1)] = img_hsv[:,:,(1)]*s_mag # 彩度の計算
    img_hsv[:,:,(2)] = img_hsv[:,:,(2)]*v_mag # 明度の計算
    img_change = cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR) # 色空間をHSVからBGRに変換
    #cv2.imshow('line_img',img_change)
    cv2.imwrite(get_img_select_path('process') + '/change_' + input,img_change)
    #cv2.waitKey(0)

def inversion(input): #色反転
    img = get_img_select_path('normal')+input
    img_bgr = cv2.imread(img)
    img_inv = cv2.bitwise_not(img_bgr)
    #cv2.imshow('inversion_ing',img_inv)
    cv2.imwrite(get_img_select_path('process') + '/inversion_' + input,img_inv)
    #cv2.waitKey(0)

#分割処理
def split_img(input,rows,cols):
    root,ext = os.path.splitext(input)
    input_img = get_img_select_path('process')+input
    # print(input_img)
    img=cv2.imread(input_img)
    chunks = []
    for row_img in np.array_split(img, rows, axis=0):
        for chunk in np.array_split(row_img, cols, axis=1):
            chunks.append(chunk)
    #print(len(chunks))
    output_img = get_img_select_path('split')
    for i, chunk in enumerate(chunks):
        cv2.imwrite(output_img+f"chunk_{i:02d}"+ext,chunk)

#split内の分割画像を削除
def del_split():
    dir = get_img_select_path('split')
    for f in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,f)):
            os.remove(os.path.join(dir,f))


#debug用コード
if __name__ == "__main__":
    input = 'sample.png'
    gray_scale(input)
    mosaic(input)
    line(input)
    changecolor(input)
    inversion(input)

    # rows=3
    # cols=4
    # split_img(input,rows,cols)
    # #5秒後にディレクトリ内の分割画像を削除する
    # time.sleep(15)
    del_split()
