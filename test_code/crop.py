import cv2

img = cv2.imread("..\image00001.jpg")

# 裁切區域的 x 與 y 座標（左上角）
# x = 80
# y = 230
x = 70
y = 170

# 裁切區域的長度與寬度
# w = 900
# h = 870
w = 700
h = 720

# 裁切圖片
# 225:1100, 80:980
crop_img = img[1200:1650, 80:980]

cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.imwrite('img.jpg', crop_img)
