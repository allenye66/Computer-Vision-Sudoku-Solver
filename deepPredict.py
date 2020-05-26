from keras.models import load_model
from keras.datasets import mnist
import matplotlib.pyplot as plt
from splice import splice_image

import numpy



model = load_model('digits.h5')
import cv2
#model.summary()


def prepare(img):
	img_size = 28
	#img_arr = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	new_arr = cv2.resize(img, (img_size, img_size)) #resize for CNN
	new_arr = numpy.invert(new_arr) #mnist dataset has data that is inverted so we must invert our input
	#plt.imshow(new_arr)
	#plt.show()
	return new_arr.reshape(-1, img_size, img_size, 1)


'''
(X_train, y_train), (X_test, y_test) = mnist.load_data()
#plt.imshow(X_train[1], cmap="gray")
#plt.show()
img = X_train[1]
img = img.reshape(-1, 28, 28, 1)
'''
#prediction = model.predict_classes([prepare("/Users/allen/Desktop/blank.png")])
#prediction = model.predict_classes(img)

def blankSpot(image):
	
def CNN_predict_single(image):
	if blankSpot(image):
		return 0
	else:
		prediction = model.predict_classes(prepare(image))
		return(prediction[0])

def CNN_predict_grid(image_grid):
	imgArr = splice_image(image_grid)
	grid = []
	for i in range(81):
		grid.append(CNN_predict_single(imgArr[i]))
	#print(len(grid))
	#print(grid)
	return grid
if __name__ == '__main__':
	#img = cv2.imread('/Users/allen/Desktop/download.png')
	img = cv2.imread('/Users/allen/Desktop/download.png',cv2.IMREAD_GRAYSCALE)
	print(CNN_predict_grid(img))
	#img = cv2.imread('/Users/allen/Desktop/five.png',cv2.IMREAD_GRAYSCALE)
	#print(CNN_predict_single(img))

