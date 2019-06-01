import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import cos, sin

img_filt = cv2.medianBlur(cv2.imread('v.jpg',0), 5)
img_th = cv2.adaptiveThreshold(img_filt,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
contours, hierarchy = cv2.findContours(img_th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    
