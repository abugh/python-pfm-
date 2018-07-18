import numpy as np
import cv2 as cv
def readPfm(fn):
    with open(fn, 'rb') as f:
        channel = np.fromfile(f, np.uint8, count=3)# PF
        Enter = np.fromfile(f, np.uint8, count=1)# 换行
        w ,h = 0,0
        # 读w
        c = np.fromfile(f, np.uint8, count=1)
        while c != 32 :# 空格的可现实ascii码
            w = w * 10 + (int(c) - 48)
            c = np.fromfile(f, np.uint8, count=1)
        # 读h
        c = np.fromfile(f, np.uint8, count=1)
        while c != 32 :# 空格的可现实ascii码
            h = h * 10 + (int(c) - 48)
            c = np.fromfile(f, np.uint8, count=1)

        Enter = np.fromfile(f, np.uint8, count=1)  # 换行

        # todo:读scale鲁棒处理(现在是按照'-', '1', '.', '0'4个字符在处理)
        scale = np.fromfile(f, np.uint8, count=4)

        Enter = np.fromfile(f, np.uint8, count=1)  # 换行
        print ('---------------------------')
        print (w,h,scale)
        data = np.fromfile(f, np.float32, count=3 * w * h)
        return np.resize(data, (h, w, 3))

cv.imshow("1",readPfm("tmp.pfm"))
cv.waitKey(0)