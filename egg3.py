from SimpleCV import *
#import Image, Color, time

disp = Display()

filename = "egg2"
file_to_load = "images/" + filename + ".jpg"
img = Image(file_to_load)
img_gray_scale = img.toGray()
img_filter = img_gray_scale.medianFilter(window='2')
#final = img.sideBySide(img_gray_scale.sideBySide(img_filter)).scale(0.2)
#final = img.sideBySide(img_gray_scale.sideBySide(img_filter)).scale(0.2)
#final.show()
#raw_input("Press Enter to continue...")
#circles = img.findCircle(canny=100, thresh=200, distance= 280)
circles = img.findCircle(canny=100, thresh=250, distance=320)
circles = circles.sortArea()
print "Circles: "
i = 1;
for c in circles:
     print "Circle " + str(i) + " : " + str(c)
     i = i+1
circles.draw(width=8)
circles[0].draw(color=Color.RED, width=4)
img_with_circles = img.applyLayers()
edges_in_image = img.edges(t2=100)
final = img.sideBySide(edges_in_image.sideBySide(img_with_circles)).scale(0.2)
final.show()
file_to_save = "images/" + filename +"_save.jpg"
final.save(file_to_save)
raw_input("Press Enter to continue...")
#time.sleep(10)


#img2 = img.colorDistance((71,57,45))
#img5 = img.toGray()
#img2 = img5.binarize()
#img3 = img2.findBlobs()
#img4 = img3.resize(500,500)
#img4 = img3.scale(500,500)
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
