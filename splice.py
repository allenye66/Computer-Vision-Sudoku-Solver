import numpy as np
import cv2
from matplotlib import pyplot as plt
import image_slicer
   
img = cv2.imread('/Users/allen/Desktop/download.png')
img = cv2.resize(img, dsize=(252, 252), interpolation=cv2.INTER_CUBIC)

print(img.shape)


height, width = img.shape[:2]
print(height)
print(width)
'''
cropped = img[0:int(255/9)-2, 0:int(255/9)-2]
cropped1 = img[0:int(255/9)-2, int(255/9)-4 :2*(int(255/9))-2]
cropped1 = img[0:int(255/9)-2, int(255/9)-4 :2*(int(255/9))-2]
cropped2 = img[0:int(255/9)-2, 2*(int(255/9))-2:3*(int(255/9))-2]
'''

'''
cropped = img[0:28, 0:28]
cropped1 = img[0:28, 28:56]
cropped2 = img[0:28, 56:84]
cropped3 = img[0:28, 84:112]
cropped4 = img[0:28, 112:140]



arr = [img, cropped, cropped1, cropped2, cropped3, cropped4]

f, axarr = plt.subplots(3,3)
axarr[0,0].imshow(arr[0])
axarr[0,1].imshow(arr[1])
axarr[1, 0].imshow(arr[2])
axarr[1, 1].imshow(arr[3])
axarr[2, 0].imshow(arr[4])
axarr[2, 1].imshow(arr[5])
'''
imageArr = []
for i in range(9):
	leftSide = i* 28
	rightSide = i*28 + 28
	for j in range(9):
		topSide = j*28
		bottomSide = j*28 + 28
		#a = [leftSide,rightSide,topSide, bottomSide]
		#print(a)
		imageArr.append(img[leftSide:rightSide,topSide:bottomSide])

		#imageArr.append(img[topSide:bottomSide, leftSide:rightSide])


f, axarr = plt.subplots(9,9)

c = 0
for i in range(9):
	for j in range(9):
		axarr[i][j].imshow(imageArr[c])
		c = c + 1

plt.show()
'''
arr = [img, cropped]
for i in arr:
	plt.figure()
	plt.imshow(i)
	plt.show()
'''

