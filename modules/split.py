import cv2
import numpy as np


#画像の読み込み
#photo=cv2.imread('sample.jpg',cv2.IMREAD_COLOR)

def split_img(input_img, output_img,rows,cols):
    img=cv2.imread(input_img)
    chunks = []
    for row_img in np.array_split(img, rows, axis=0):
        for chunk in np.array_split(row_img, cols, axis=1):
            chunks.append(chunk)
    print(len(chunks))
    for i, chunk in enumerate(chunks):
        cv2.imwrite(output_img+f"chunk_{i:02d}.png",chunk)
    


#debug用コード
if __name__ == "__main__":
    input = '/Users/k21013/Oop/Oop2/final/Freesubject/static/images/process/sample.png'
    output = '/Users/k21013/Oop/Oop2/final/Freesubject/static/images/split/'
    rows=6
    cols=6
    split_img(input,output,6,6)
    