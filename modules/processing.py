import cv2
import numpy as np

def gray_scale(input): #グレースケール化
    img_bgr = cv2.imread(input)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray_img',img_gray)
    cv2.waitKey(0)


def mosaic(input, ratio=0.005): #モザイク化
    img_bgr = cv2.imread(input) 
    small = cv2.resize(img_bgr, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    img_mosaic =  cv2.resize(small, img_bgr.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    cv2.imshow('mosaic_img',img_mosaic)
    cv2.waitKey(0)

def line(input):
    gray = cv2.imread(input, cv2.IMREAD_GRAYSCALE)
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
    cv2.imshow('line_img',img_line)
    cv2.waitKey(0)
    
    




#debug用コード
if __name__ == "__main__":
    input = 'static/images/normal/kinopio.jpeg'
    gray_scale(input)
    mosaic(input)
    line(input)
    

