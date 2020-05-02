import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('coin.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', gray)
cv.waitKey(0)


ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
cv.imshow('image', opening)
cv.waitKey(0) 
# sure background area
sure_bg = cv.dilate(opening,kernel,iterations=3)
cv.imshow('image', sure_bg)
cv.waitKey(0) 
# Finding sure foreground area
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
cv.imshow('image', sure_fg)
cv.waitKey(0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)
cv.imshow('image', unknown)
cv.waitKey(0) 

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)
# cv.imshow('image', markers)
# cv.waitKey(0)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0
markers = cv.watershed(img,markers)
img[markers == -1] = [255,0,0]
cv.imshow('image', img)
cv.waitKey(0) 
        