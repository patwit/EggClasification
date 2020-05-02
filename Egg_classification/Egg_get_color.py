__author__ = 'polpinit'

import cv2
import cv2.cv as cv

image = cv2.imread('images/2-result_single1.jpg')

height, width, channels = image.shape

cv2.rectangle(image, (height/2 - 5, width/2 - 5), (height/2 + 5, width/2 + 5), (0, 128, 255), -1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', image)
cv2.waitKey(0)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#s=cv.Get2D(hsv, height/2, width/2)

#print "H:",s[0],"      S:",s[1],"       V:",s[2]

# H=hsv.val[0];
# S=hsv.val[1];
# V=hsv.val[2];

print image[height/2, width/2]
print hsv[height/2, width/2]
 # Vec3b color = image.at<Vec3b>(Point(x,y));

#         bgrPixel.val[0] = rowPtr[j*cn + 0]; // B
#         bgrPixel.val[1] = rowPtr[j*cn + 1]; // G
#         bgrPixel.val[2] = rowPtr[j*cn + 2]; // R
