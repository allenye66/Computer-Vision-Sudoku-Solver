import numpy as np
import cv2
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
# import image_slicer

def splice_image(img):
	# img = cv2.imread(img) # comment this out
	img = cv2.resize(img, dsize=(252, 252), interpolation=cv2.INTER_CUBIC)
	print(img.shape)

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
			index = i, j
			axarr[i][j].imshow(imageArr[c])
			c = c + 1

	# plt.show()
	return imageArr

#if __name__ == '__main__':
#	img = cv2.imread('/Users/allen/Desktop/download.png')
#	splice_image(img)


