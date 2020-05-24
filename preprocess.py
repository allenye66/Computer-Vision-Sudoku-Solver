import numpy as np
import cv2
from matplotlib import pyplot as plt
   
img = cv2.imread('/Users/allen/Desktop/image2.png')

'''
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5) 
plt.imshow(thresh1)
plt.show()
'''

'''
img = cv2.medianBlur(img,5)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)



plt.imshow(th2)
plt.show()
'''

'''

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 20, apertureSize = 3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 250)
for line in lines:
	rho, theta = line[0]
	a = np.cos(theta)
	b  = np.sin(theta)
	x0 = a * rho
	y0 = b * rho
	x1 = int(x0+ 1000*(-b))
	y1 = int(y0+ 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0- 1000*(a))
	cv2.line(img, (x1, y1), (x2,y2), (0, 0, 255), 2)

'''

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=50,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

arr = [img, gray, edges]
for i in arr:
	plt.figure()
	plt.imshow(i)
	plt.show()

#plt.imshow(img)


#plt.show()