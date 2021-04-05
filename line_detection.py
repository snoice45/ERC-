import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image=cv.imread('img.jpg')
cv.imshow('IMAGE',image)
img_rgb=cv.cvtColor(image,cv.COLOR_BGR2RGB)
cv.imshow('IMAGE',img_rgb)
img_hsv=cv.cvtColor(img_rgb,cv.COLOR_RGB2HSV)
cv.imshow('IMAGE',img_hsv)

lower=np.array([10,60,180])
upper=np.array([30,255,255])
mask=cv.inRange(img_hsv,lower,upper)

lower2=np.array([0,0,87])
upper2=np.array([86,32,225])
mask2=cv.inRange(img_hsv,lower2,upper2)
# cv.imshow('IMAGE',mask2)
bitwise_and=cv.bitwise_or(mask,mask2)
cv.imshow('IMAGE',bitwise_and)
cv.waitKey(0)