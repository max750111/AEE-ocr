import cv2


# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型

def save_image(image, num):
    address = './output/' + 'image' + str(num) + '.jpg'
    cv2.imwrite(address, image)


# 讀取影片檔
videoCapture = cv2.VideoCapture("1.mp4")
# print(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# videoCapture.get(cv2.CAP_PROP_FPS)
# videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
# videoCapture.get(cv2.CAP_PROP_POS_FRAMES)
# CAP_PROP_FRAME_WIDTH
# CAP_PROP_FRAME_HEIGHT

timeF = 7  # 設定多少幀截圖
i = 0
j = 0
while True:
    success, frame = videoCapture.read()
    if success:
        i = i + 1
        if i % timeF == 0:
            j = j + 1
            save_image(frame, j)
            print('save image:', j)
    elif success == 0:
        break

videoCapture.release()
