import os
import time
from SimpleCV import *
from SimpleCV.Shell import plot

img = Image("tray1.jpg")

egg = img
img2 = img
histogram = img.hueHistogram()


peaks = img.huePeaks()
print peaks
peak_one = peaks[2][0]
print peak_one
hue = img.hueDistance(165)
hue.save("hue.jpg")
imgCut = img - hue
segmented = imgCut.stretch(26,255)
eggcut = img2 - segmented.invert()
eggcut.save("eggcut2.jpg")
#segmented.show()
#time.sleep(3)
Circle = segmented.findCircle(canny=73,thresh=320,distance=300)
Circle = Circle.sortArea()
Circle[30].draw(color=Color.GREEN, width=15)
cir1 = img2.applyLayers()
cir1.save("z.jpg")
time.sleep(3)
Circle.draw(width=6)
Circle[30].draw(color=Color.RED, width=15)
img_with_circles = img2.applyLayers()
img_with_circles.show()
time.sleep(2)
img_with_circles.save("eggCir2.jpg")
imgCut.save("IMGcutHue1.jpg")
segmented.save("segmentegg.jpg")

"""
egg = egg.colorDistance((170,150,130)).dilate(1)
egg.show()
time.sleep(3)
segmented = egg.stretch(110,242)

segmented.show()
time.sleep(3)
Circle = segmented.findCircle(canny=100,thresh=200,distance=280)
Circle = Circle.sortArea()
Circle.draw(width=4)
Circle[0].draw(color=Color.RED, width=4)
img_with_circles = img.applyLayers()
img_with_circles.show()
time.sleep(3)
blobs = segmented.findBlobs()
if blobs:
	circles = blobs.filter([b.isCircle(0.000001) for b in blobs])

	if circles:
		img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),Color.RED,3)

segmented.show()
#hue.show()
#hue.save("hueTray1_4.jpg")
#imgCut.save("IMGcutHue1.jpg")
segmented.save("segmentegg.jpg")
#plot(histogram)
"""

#########################################################
'''
stretch(thresh_low=0, thresh_high=255)

    The stretch filter works on a greyscale image, if the image is color, it returns a greyscale image. The filter works by taking in a lower and upper threshold. Anything below the lower threshold is pushed to black (0) and anything above the upper threshold is pushed to white (255)

    Returns: IMAGE
'''
'''
def isCircle(self, tolerance = 0.05):
        """
        **SUMMARY**
        Test circle distance against a tolerance to see if the blob is circlular.
        **PARAMETERS**
        * *tolerance* - the percentage difference between our blob and an ideal circle.
        **RETURNS**
        True if the feature is within tolerance for being a circle, false otherwise.
        """
'''

'''
 def findCircle(self,canny=100,thresh=350,distance=-1):
        """
        **SUMMARY**
        Perform the Hough Circle transform to extract _perfect_ circles from the image
        canny - the upper bound on a canny edge detector used to find circle edges.
        **PARAMETERS**
        * *thresh* - the threshold at which to count a circle. Small parts of a circle get
          added to the accumulator array used internally to the array. This value is the
          minimum threshold. Lower thresholds give more circles, higher thresholds give fewer circles.
        .. ::Warning:
          If this threshold is too high, and no circles are found the underlying OpenCV
          routine fails and causes a segfault.
        * *distance* - the minimum distance between each successive circle in pixels. 10 is a good
          starting value.
        **RETURNS**
        A feature set of Circle objects.
        **EXAMPLE**
        >>> img = Image("lenna")
        >>> circs = img.findCircles()
        >>> for c in circs:
        >>>    print c
        """
        storage = cv.CreateMat(self.width, 1, cv.CV_32FC3)
        #a distnace metric for how apart our circles should be - this is sa good bench mark
        if(distance < 0 ):
            distance = 1 + max(self.width,self.height)/50
        cv.HoughCircles(self._getGrayscaleBitmap(),storage, cv.CV_HOUGH_GRADIENT, 2, distance,canny,thresh)
        if storage.rows == 0:
            return None
        circs = np.asarray(storage)
        sz = circs.shape
        circleFS = FeatureSet()
        for i in range(sz[0]):
            circleFS.append(Circle(self,int(circs[i][0][0]),int(circs[i][0][1]),int(circs[i][0][2])))
        return circleFS
'''

