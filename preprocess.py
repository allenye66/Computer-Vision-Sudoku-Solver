import cv2  
import numpy as np  
from matplotlib import pyplot as plt

   

image1 = cv2.imread('/kaggle/input/sudoku-original.jpg')  
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 

thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                          cv2.THRESH_BINARY, 199, 5) 
  
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 199, 5)  
plt.imshow(thresh1) 
plt.imshow(thresh2) 

