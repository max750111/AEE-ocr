# 產出word檔

import pytesseract
import cv2
from os import listdir, mkdir
import pyperclip
import difflib
from multiprocessing import Pool
import time
import shutil
import tqdm
from docx import Document
import re


# 截取圖片存在output資料夾
def save_image(image, num):
    """

    :param image: 要儲存的圖片
    :param num: 圖片編號
    :return: none
    """
    address = './output/' + 'image' + num + '.jpg'  # 完整儲存位置(含路徑、檔名及副檔名);儲存路徑預設為output
    cv2.imwrite(address, image)


# 讀取影片檔並截圖
# 要設定多少幀截一張圖
def load_film(film_filename):
    shutil.rmtree('./output')
    mkdir('./output')
    video_capture = cv2.VideoCapture(film_filename)

    per_frame = 7  # 設定多少幀截圖
    i = 0
    j = 0
    while True:
        success, frame = video_capture.read()
        if success:
            i = i + 1
            if i % per_frame == 0:
                j = j + 1
                save_image(frame, '{0:05d}'.format(j))
                print('save image:', j)
        elif success == 0:
            break
    video_capture.release()


# 讀取所有放在image資料夾待辨識圖片檔檔名並回傳成list
def queue_img(path):
    files = listdir(path)
    return files  # list


# 黑白反轉，增加辨識準確率，轉換結果放到result資料夾
def change_color_crop(image_filename):
    shutil.rmtree('./result')
    mkdir('./result')
    for img in image_filename:
        img_origin = cv2.imread("./output/" + img, cv2.IMREAD_GRAYSCALE)
        img_result = 255 - img_origin
        crop_img = img_result[225:1100, 80:980]
        cv2.imwrite("./result/" + img, crop_img)


# 檢查辨識過後的字串若己經存在結果列表中（相似度超過80%），則返回False
# 要設定相似度
def delete_repeat(str, list):
    result = 1
    if list:
        for i in list[-15:]:
            # print(i)
            if difflib.SequenceMatcher(None, str, i).quick_ratio() > 0.9:
                result = 0
                break
    return result


def all_name(transcript_list):
    for index, str in enumerate(transcript_list):
        if str.startswith("M:"):
            transcript_list[index] = transcript_list[index].replace("M:", "\n\nMichelle:")
        elif str.startswith("L:"):
            transcript_list[index] = transcript_list[index].replace("L:", "\n\nLindsay:")


transcript = []


# 文字辨識(未完成)
def main_map(l):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # print(l)
    img_for_ocr = cv2.imread("./output/" + l, cv2.IMREAD_GRAYSCALE)
    img_gray = 255 - img_for_ocr

    # 逐字稿區
    # img_gray[225:1100, 80:980]
    # episode區
    # img_gray[1200:1650, 80:980]

    # 以下要改
    a = pytesseract.image_to_string(img_for_ocr, lang="eng", config="--oem 1 --psm 6")
    a = a.strip()  # 去除最後的空白字元
    a = a.replace("|", "I")  # 修正辨識內容
    ocr_result = a.split("\n")  # 用\n分割每行，存成列表
    ocr_result = [x for x in ocr_result if x != (' ' and '')]  # 過濾掉空白字元
    return ocr_result


def delete_useless_img():
    episode = dict()
    for i in queue_img("./output"):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        # print(l)
        img_for_ocr = cv2.imread("./output/" + i, cv2.IMREAD_GRAYSCALE)
        img_gray = 255 - img_for_ocr
        if pytesseract.image_to_string(img_gray[1200:1650, 80:980], lang="eng",
                                       config="--oem 1 --psm 6") not in episode:
            episode[pytesseract.image_to_string(img_gray[1200:1650, 80:980], lang="eng",
                                       config="--oem 1 --psm 6")].append(i)

# 程式進入點
def main():
    t1 = time.time()

    for v in queue_img('./video'):
        load_film('./video/' + v)

        # change_color_crop(queue_img("./output"))

        with Pool(8) as p:
            r = list(tqdm.tqdm(p.imap(main_map, sorted(queue_img("./output"), key=lambda x: int(x[-9:-4]))),
                               total=len(queue_img("./result"))))
            outputs = list(r)

        # pool = Pool(8)

        # 運行多處理程序
        # outputs = pool.map(main_map, sorted(queue_img("./result"), key=lambda x: int(x[-9:-4])))
        # print(outputs)
        for i in outputs:
            for str in i[2:-3]:  # 去除圖片頭尾可能的亂碼
                # 若辨識字串不在結果列表中或與結果列表中字串相似度不超過80%
                # 將字串加入結果列表
                if (str not in transcript[-15:]) and delete_repeat(str, transcript[-15:]):
                    # print(str)
                    transcript.append(str)
                    # print(transcript)
        all_name(transcript)  # 將名字縮寫還原
        transcript_final = " ".join(transcript)  # 將字串列表還原成字串
        # print(transcript_final)
        pyperclip.copy(transcript_final)

        doc = Document()

        doc.add_paragraph(pyperclip.paste())
        doc.save('./ocr_final/' + v[:-5] + '.docx')

    t2 = time.time()

    tf = t2 - t1
    print(tf)


if __name__ == "__main__":
    main()
