import pytesseract
import cv2
import re

episode_num = re.compile(r'AEE (\d*)')
episode_bonus = re.compile(r'aee bonus')

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img_for_ocr = cv2.imread("image00001.jpg")
a = pytesseract.image_to_string(img_for_ocr[1200:1650, 80:980], lang="eng", config="--oem 1 --psm 6")
print(a.lower())

m = episode_num.search(a)
print(m.group(1))

cv2.imshow('test', img_for_ocr[1200:1650, 80:980])
cv2.waitKey(0)