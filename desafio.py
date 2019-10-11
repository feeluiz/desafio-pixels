import numpy as np
import cv2 as cv

image = cv.imread("cs.png")

imageHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)

red_lower = np.array([194, 194, 244])
red_upper = np.array([0, 0, 255])

mascara = cv.inRange(imageHSV,  red_lower, red_upper)

res = cv.bitwise_and(image,image, mask=mascara)


cv.imshow('mascara',mascara)
cv.imshow('res',res)
cv.imshow('image',imageHSV)

cv.waitKey(0)
cv.destroyAllWindows()