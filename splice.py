import numpy as np
import cv2
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
from PIL import Image
# import image_slicer

def splice_image(img):
	# img = cv2.imread(img) # comment this out
	img = cv2.resize(img, dsize=(720, 720), interpolation=cv2.INTER_CUBIC)
	print(img.shape)

	imageArr = []
	for i in range(9):
		leftSide = i* 80
		rightSide = i*80 + 80
		for j in range(9):
			topSide = j*80
			bottomSide = j*80 + 80
			#a = [leftSide,rightSide,topSide, bottomSide]
			#print(a)\
			imageArr.append(img[leftSide+2:rightSide-2,topSide+2:bottomSide-2])

			#imageArr.append(img[topSide:bottomSide, leftSide:rightSide])


	f, axarr = plt.subplots(9,9)

	c = 0
	for i in range(9):
		for j in range(9):
			index = i, j
			axarr[i][j].imshow(imageArr[c])
			c = c + 1

	plt.savefig('output.png')
	
	return imageArr

if __name__ == '__main__':
	img = cv2.imread('images/download.png')
	splice_image(img)


