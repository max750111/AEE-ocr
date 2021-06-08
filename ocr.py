import pytesseract
import cv2
import numpy as np


# 截取圖片存在output資料夾
def save_image(image, num):
    """

    :param image: 要儲存的圖片
    :param num: 圖片編號
    :return: none
    """
    address = './output/' + 'image' + str(num) + '.jpg'  # 完整儲存位置(含路徑、檔名及副檔名);儲存路徑預設為output
    cv2.imwrite(address, image)


# 讀取影片檔並截圖
def load_film(film_filename):
    video_capture = cv2.VideoCapture(film_filename)
    # video_capture.get(cv2.CAP_PROP_FPS)
    # video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    # video_capture.get(cv2.CAP_PROP_POS_FRAMES)
    success, frame = video_capture.read()  # 讀幀

    per_frame = 7  # 設定多少幀截圖
    i = 0
    j = 0
    while success:
        i = i + 1
        if i % per_frame == 0:
            j = j + 1
            save_image(frame, j)
            #print('save image:', i)
        success, frame = video_capture.read()
    video_capture.release()


# 讀取所有放在image資料夾待辨識圖片檔檔名，存在queue_job列表
def queue_img():
    queue_job = []
    return queue_job


# 黑白反轉，增加辨識準確率，轉換結果放到result資料夾
def change_color_resize(queue_job):
    for img in queue_job:
        img_origin = cv2.imread(img, 0)
        height, width = img_origin.shape
        img_result = np.zeros((height, width, 1), np.uint8)
        for i in range(height):
            for j in range(width):
                img_result[i, j] = 255 - img[i, j]  # img_result為轉換後的圖片
        crop_img = img_result[y:y + h, x:x + w]
        cv2.imwrite('./result/' + img, crop_img)


# 文字辨識(未完成)
def ocr():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(r"image\2.JPG")
    a = pytesseract.image_to_string(img, lang="eng")
    a = a.strip()  # 去除最後的空白字元

    print(a)


def main():
    pass
    #load_film('1.mp4')


if __name__ == "__main__":
    main()
