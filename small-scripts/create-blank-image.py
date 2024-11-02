'''This will create an image with a black background, technically blank 
background, since at any position the black pixel is represented by the
value,(0,0,0). Upon adding any pixel value (R,G,B) to this position (s),
the results is the added pixel itself.'''
import numpy as np
import cv2
height = 3507
width = 2480
channels = 3
img = np.full((height,width,channels), 255, dtype=np.uint8)
# cv2.imshow("blank_image", img)
cv2.imwrite("blank_image.png", img)