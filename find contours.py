
import numpy as np
import cv2
im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
cnt = contours[4]	# IndexError: list index out of range
# cv2.drawContours(im, [cnt], 0, (0,255,0), 3)  # this fucntion is for OpemCV3
img = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)

for i in range(img.shape[0]):
    s,e,f,d = img[i,0]	# IndexError: list index out of range
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)

cv2.imshow('img',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

import numpy as np
import cv2

im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cnt = contours[4]
#img = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
"""
if len(contours)>0 :
   cnt=contours[len(contours)-1]
   cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
"""


cv2.imshow('test.jpg',im, (100, 100)
cv2.waitKey(0)
cv2.destroyAllWindows()

Mohit99040"""