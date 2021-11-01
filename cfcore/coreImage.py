# 画像処理モジュール
# cfcore/coreImage.py

import cv2
import numpy as np

# param
size = (480, 384)
maskBright = 3


def imread(filename):
    return cv2.imread(filename)


def imwrite(filename, img):
    cv2.imwrite(filename, img)


def imcrop(img, x, y, w, h):
    imgCrop = img[x:x+w, y:y+h]
    imgResize = cv2.resize(imgCrop, dsize=size, interpolation=cv2.INTER_LANCZOS4)
    return imgResize


def immask(img, mode='top', maskH = 270):
    if mode == 'bottom':
        maskY = 0
    else:
        maskY = size[0] - maskH
    img[maskY:maskY+maskH, 0:size[0]] //= maskBright
    return img


# module test
if __name__ == '__main__':
    img = imread('test.png')
    im2 = immask(img)
    imwrite("out.png", im2)
