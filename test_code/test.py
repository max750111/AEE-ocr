import pytesseract
import cv2
import re
from os import listdir
import csv
import time

def queue_img(path):
    files = listdir(path)
    return files  # list



episode = list()
delete_file = set()
episode_num = re.compile(r'AEE (\d*)')

for i in queue_img("../output"):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img_for_ocr = cv2.imread("../output/" + i, cv2.IMREAD_GRAYSCALE)
    img_gray = 255 - img_for_ocr
    a = pytesseract.image_to_string(img_gray[1200:1650, 80:980], lang="eng",
                                config="--oem 1 --psm 6")
    m = episode_num.search(a)
    if m:
        b = pytesseract.image_to_string(img_gray[225:1100, 80:980], lang="eng",
                                config="--oem 1 --psm 6")
        b = b.strip()  # 去除最後的空白字元
        b = b.replace("|", "I")  # 修正辨識內容
        b = b.replace("\n", "\\n")
        # ocr_result = b.split("\n")  # 用\n分割每行，存成列表
        # ocr_result = [x for x in ocr_result if x != (' ' and '')]
        episode.append([m.group(1), i, b])
        print(type(b))
        print(episode)

    else:
        delete_file.add(i)
        print(delete_file)


with open(str(int(time.time())) + '.csv', 'w', encoding='utf-8') as csvfile:
  writer = csv.writer(csvfile)

  # 寫入二維表格
  writer.writerow(['episode', 'filename', 'string'])
  writer.writerows(episode)
