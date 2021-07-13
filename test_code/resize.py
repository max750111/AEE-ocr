import cv2

src = cv2.imread('test.jpg')
print(type(src))

# percent by which the image is resized
scale_percent = 10

# calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite('resize.jpg', output)