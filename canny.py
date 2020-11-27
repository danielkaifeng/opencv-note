import numpy as np
import cv2
from sys import argv

cv2.namedWindow("images")
def nothing(_):
    print(_)

cv2.createTrackbar("s1","images",0,255,nothing)
cv2.createTrackbar("s2","images",0,255,nothing)

img_path = argv[1]
img = cv2.imread(img_path,0)
img = cv2.resize(img, (img.shape[1]*4, img.shape[0]*4))

while(1):
    s1 = cv2.getTrackbarPos("s1","images")
    s2 = cv2.getTrackbarPos("s2","images")
    out_img = cv2.Canny(img,s1,s2)
    cv2.imshow("img",out_img)
    k = cv2.waitKey(1)
    if k==ord("q"):
        break
cv2.destroyAllWindows()
