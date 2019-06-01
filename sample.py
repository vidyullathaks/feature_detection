#! /usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
img = cv2.imread("v.jpg",0)
img1 = imutils.resize(img)
img2 = img1[197:373,181:300]  #roi of the image
ans = []
for y in range(0, img2.shape[0]):  #looping through each rows
     for x in range(0, img2.shape[1]): #looping through each column
            if img2[y, x] != 0:
                  ans = ans + [[x, y]]
ans = np.array(ans)
print ("the roi of the image is located at :", ans)
#print (ans)
