import cv2
import numpy as np

img1 = cv2.imread("v.jpg", cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dim = (640,1000)
        resized1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)    
        resized2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
        orb = cv2.ORB_create(nfeatures = 1000)
        keypoints1, descriptors1 = orb.detectAndCompute(resized1, None)
        keypoints2, descriptors2 = orb.detectAndCompute(resized2, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(descriptors1,descriptors2)
        matches = sorted(matches, key = lambda x:x.distance)
        matching_result = cv2.drawMatches(resized1, keypoints1 , resized2, keypoints2 , matches[:20] , None)
        print(len(matches))
        cv2.imshow("Matching Result", matching_result)
        frame = cv2.flip(frame,0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

resized = cv2.drawKeypoints(resized, keypoints, None)

cv2.imshow("Image1", resized1)
cv2.imshow("Image2", resized2)
