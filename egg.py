from SimpleCV import *
#import Image, Color, time

disp = Display()

img = Image("images/egg.jpg")
#img2 = img.colorDistance((71,57,45))
img5 = img.toGray()
img2 = img5.binarize()
img3 = img2.findBlobs()
#img4 = img3.resize(500,500)
#img4 = img3.scale(500,500)
print("Image in binary: ", img2)
print("Area: ", img3.area())
print("Angle: ", img3.angle())
print("Coordinate: ", img3.coordinates())
for x in img3:
    print("Saving ", x)
    x.save("picture",x,".jpg")
    #x.show()
    #time.sleep(1)
#img3.show(width=1)
#img3.save(disp)
#time.sleep(10)
#img = img.drawText("Hello World!")
#while True:
#img2 = img.toGray()
#img3 = img2.binarize()
#img4 = img2.edges()
#img5 = img.findBlobs()
#for blob in blobs:
#    blob.draw()
#    if img.mouseLeft:
#        break

#img = img.resize(500,500)
#img.show()
#img.save(disp)
#time.sleep(5)


#cam = camera(0, { "width": 640, "height": 480 })
#img2 = cam.getImage()
#img2.save(disp)
#img2 = img2.resize(500,500)
#img2.show()
#time.sleep(5)
#img5.show()
#img5.save(disp)
