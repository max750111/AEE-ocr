import pytesseract
import cv2
import re
from os import listdir

def queue_img(path):
    files = listdir(path)
    return files  # list

episode = dict()
episode_num = re.compile(r'AEE (\d*)')

for i in queue_img("../output"):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img_for_ocr = cv2.imread("../output/" + i, cv2.IMREAD_GRAYSCALE)
    img_gray = 255 - img_for_ocr
    a = pytesseract.image_to_string(img_gray[1200:1650, 80:980], lang="eng",
                                config="--oem 1 --psm 6")
    m = episode_num.search(a)
    if m.group(1) not in episode:
        episode[m.group(1)] = []
        episode[m.group(1)].append(i)
        print(episode)
    else:
        episode[m.group(1)].append(i)
        print(episode)
print(episode)