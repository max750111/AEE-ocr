from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
import math
import pytesseract
import cv2
import re
from os import listdir
import time
from os import listdir, mkdir
import shutil
from docx import Document
import difflib
from multiprocessing import Pool
import pandas as pd




def load_video_and_cut(split=4):
    clip = VideoFileClip("all.mp4")
    print(clip.duration)

    t1, t2 = 0, clip.duration/split
    for i in range(0, split):
        t1, t2 = math.floor(0+clip.duration/4*i), math.floor(clip.duration / split +clip.duration/split*i)-1
        ffmpeg_extract_subclip('all.mp4', t1, t2, targetname='./split_video/'+'part'+str(i+1)+'.mp4')
        #print(t1, t2)


def queue_img(path):
    files = listdir(path)
    return [x for x in files if x[-3:] == 'mp4']  # list

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
                #print(j)
                main(frame)
        elif success == 0:
            break
    video_capture.release()

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


episode_num = re.compile(r'AEE (\d+)')

transcript = dict()


def main(frame):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img_for_ocr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # SHOW一下圖
    img_gray = 255 - img_for_ocr
    # SHOW一下圖
    a = pytesseract.image_to_string(img_gray[1200:1650, 80:980], lang="eng", config="--oem 1 --psm 6")
    m = episode_num.search(a)
    if m: # 如果AEE後面有數字（不是AEE BONUS），就辨識口語稿區
        #print(m.group(1))
        b = pytesseract.image_to_string(img_gray[225:1100, 80:980], lang="eng", config="--oem 1 --psm 6")
        b = b.strip()  # 去除最後的空白字元
        b = b.replace("|", "I")  # 修正辨識內容
        ocr_result = b.split("\n")  # 用\n分割每行，存成列表
        ocr_result = [x for x in ocr_result if x != (' ' and '')]
        #print(ocr_result)

# all_name(transcript)  # 將名字縮寫還原

load_film('all.mp4')
for i in transcript:
    all_name(transcript[i])
    transcript_final = " ".join(transcript[i])
    doc = Document()
    doc.add_paragraph(transcript_final)
    doc.save(i + '.docx')




#load_video_and_cut()
print(queue_img('./split_video'))