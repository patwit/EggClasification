__author__ = 'polpinit'

BETWEEN_EGG = 590  # distance between the center of each egg
SQUARE_SIZE = 250  # size of the square to be drawn over egg
SQUARE_THICK = 10  # thickness of the line of square
EGG_PER_ROW = 6  # number of eggs per row in the picture
NUM_RANDOM_POINT = 10  # number of random point to be RGB sample


import numpy as np
import cv2
import random
import argparse
from matplotlib import pyplot as plt

# read in image
image = cv2.imread('images/egg3.JPG')

# get size of the image
height, width, channels = image.shape

x = int(BETWEEN_EGG / 2.0)  # initial the center of the first egg
y = int(BETWEEN_EGG / 2.0)  #


#cv2.circle(image, (x, y), SQUARE_SIZE, SQUARE_THICK)
cv2.circle(image, (x, y), SQUARE_SIZE, (0,0,255), SQUARE_THICK)
for num in range(1, 31):
    x1 = int(x - SQUARE_SIZE / 2.0)
    y1 = int(y - SQUARE_SIZE / 2.0)
    x2 = int(x + SQUARE_SIZE / 2.0)
    y2 = int(y + SQUARE_SIZE / 2.0)
    #cv2.rectangle(image, (x1, y1), (x2, y2), SQUARE_SIZE, SQUARE_THICK)
    #cv2.circle(image, (x, y), SQUARE_SIZE, SQUARE_THICK)
    for r in range(1, 11):
        x_rand = random.randint(x1, x2)
        y_rand = random.randint(y1, y2)
        print ("(", x_rand, ",", y_rand, ")")
    if num % EGG_PER_ROW != 0:
        x = x + BETWEEN_EGG
    else:
        x = BETWEEN_EGG / 2.0
        y = y + BETWEEN_EGG

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256]); plt.show()
color = ('b','g','r')
for i,col in enumerate(color):
   histr = cv2.calcHist([image],[i],None,[256],[0,256])
   plt.plot(histr,color = col)
   plt.xlim([0,256])
plt.show()

print " B G R : " im

key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):  # if press 's' save the picture
    cv2.imwrite('images/egg_result.jpg', img)
    cv2.destroyAllWindows()
