import pytesseract
import cv2
import numpy as np
from os import listdir


def resize_image(frame):
    """

    """
    scale_percent = 80

    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)

    dsize = (width, height)

    output = cv2.resize(frame, dsize)

    return output


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
def load_film(film_filename):
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
                save_image(resize_image(frame), '{0:05d}'.format(j))
                print('save image:', j)
        elif success == 0:
            break
    video_capture.release()


# 讀取所有放在image資料夾待辨識圖片檔檔名，存在queue_job列表
def queue_img(path):
    files = listdir(path)
    return sorted(files, key = lambda x : int(x[-9:-4]))  # list


# 黑白反轉，增加辨識準確率，轉換結果放到result資料夾
def change_color_crop(image):
    for img in image:
        img_origin = cv2.imread("./output/" + img, 1)
        gray = cv2.cvtColor(img_origin, cv2.COLOR_BGR2GRAY)
        img_result = 255 - gray
        crop_img = img_result[170:890, 70:770]
        cv2.imwrite("./result/" + img, crop_img)


def all_name(transcript_list):
    for index, str in enumerate(transcript_list):
        if str.startswith("M:"):
            transcript_list[index] = transcript_list[index].replace("M:", "FuckM")
        elif str.startswith("L:"):
            transcript_list[index] = transcript_list[index].replace("L:", "FuckL")


# 文字辨識(未完成)
def ocr():
    transcript = []
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    for img_file in queue_img("./result"):
        print(img_file)
        img_for_ocr = cv2.imread("./result/" + img_file)
        a = pytesseract.image_to_string(img_for_ocr, lang="eng")
        a = a.strip()  # 去除最後的空白字元
        ocr_result = a.split("\n")  # 用\n分割每行，存成列表
        print(ocr_result)
        for str in ocr_result[1:-2]:
            if str not in transcript[-11:0]:
                transcript.append(str)
    print(transcript)
    #all_name(transcript)
    #transcript_final = " ".join(transcript)

    #print(transcript_final)


def main():
    #pass
    load_film('1.mp4')
    change_color_crop(queue_img("./output"))
    #ocr()


if __name__ == "__main__":
    main()
