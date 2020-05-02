import os
import time
from SimpleCV import *


img = Image("IMGcutHue1.jpg")
#img = img.colorDistance((217,150,130))
#img = img.binarize(30)
circles = img.findCircle(canny=100,thresh=200,distance=280)
circles = circles.sortArea()
circles.draw(width=4)
circles[0].draw(color=Color.RED, width=4)
img_with_circles = img.applyLayers()
#img_with_circles.save("1.jpg")


img.show()
img.save("IMGcutHueCir1.jpg")
time.sleep(5)
