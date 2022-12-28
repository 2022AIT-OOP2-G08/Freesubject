from xml.etree.ElementPath import get_parent_map
import cv2
import numpy as np
from opedir import get_current_path , get_parent_path






#画像の読み込み
#photo=cv2.imread('sample.jpg',cv2.IMREAD_COLOR)

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
    