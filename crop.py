import cv2

img = cv2.imread("test.jpg")

# 裁切區域的 x 與 y 座標（左上角）
x = 100
y = 100

# 裁切區域的長度與寬度
w = 250
h = 150

# 裁切圖片
crop_img = img[y:y+h, x:x+w]

cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
