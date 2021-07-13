import cv2
import numpy as np

img = cv2.imread("image/1.jpg", 0)  #讀取一張圖片，灰度
height, width= img.shape
dst = np.zeros((height, width, 1), np.uint8)
for i in range(height):
    for j in range(width):
        dst[i, j] = 255-img[i, j]

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.imwrite('2.jpg', dst)
cv2.waitKey()  #窗口等待任意鍵盤按鍵輸入,0為一直等待,其他數字為毫秒數