import numpy as np
import cv2

img1 = cv2.imread('demo1.png')
img2 = cv2.imread('test.png')

width, height = img2.shape[:2]

# print(height, width)

img1 = cv2.resize(img1, (height, width), interpolation = cv2.INTER_CUBIC)

# cv2.imshow("resized image", img1)
# key = cv2.waitKey()

newImg = cv2.addWeighted(img1, 1, img2, 0.1, 0)

cv2.imshow("newImg", newImg)
key = cv2.waitKey()
cv2.imwrite("newImg.png", newImg)