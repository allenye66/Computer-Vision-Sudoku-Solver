from keras.models import load_model
from keras.datasets import mnist
import matplotlib

import matplotlib.pyplot as plt
from splice import splice_image
import numpy
tf.logging.set_verbosity(tf.logging.ERROR)

model = load_model('digits.h5')
import cv2
#odel.summary()


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

def blankSpot(blank):
	#print(blank)
	#plt.imshow(blank)
	#plt.show()
	#x = numpy.array([0,1,2,3,4,5,6,7,8,9,10])
	#print(x)
	#indices = list(range(1,3))
	#y = x[indices]
	#print(y)
	#a = numpy.array([[0, 1], [2, 3], [ 4, 5],[6, 7]])
	#print(a)
	#indices = list(range(1, 2) )
	#b = a[indices]
	#print(b)


	#cv2.line(blank ,(5,5),(20,5),(0,0,0),1)
	#cv2.line(blank ,(20,5),(20,20),(0,0,0),1)
	#cv2.line(blank ,(20,20),(5,20),(0,0,0),1)
	#cv2.line(blank ,(5,20),(5,5),(0,0,0),1)

	s = set()
	for i in range(10):
		for j in range(10):
			#for k in range(2):
			s.add(blank[i + 10][j + 10])
			#print((i + 10), ",", (j+10), ": ", blank[i + 10][j+10])
	#print(s)
	if len(s) == 1:
		return True
	else: 
		return False

def CNN_predict_single(image):
	if blankSpot(image) == True:
		return int(0)
	else:
		prediction = model.predict_classes(prepare(image))
		return(prediction[0])
'''
def CNN_predict_single(image):
	print(blankSpot(image))
	prediction = model.predict_classes(prepare(image))
	return(prediction[0])
'''
def CNN_predict_grid(filepath):
	#image_grid = cv2.imread('/Users/allen/Desktop/download.png',cv2.IMREAD_GRAYSCALE)
	image_grid = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
	imgArr = splice_image(image_grid)
	grid = []
	for i in range(81):
		grid.append(CNN_predict_single(imgArr[i]))
	#print(len(grid))
	#print(grid)
	return grid
def hello():
    return 'Hi'

#if __name__ == '__main__':
	#img = cv2.imread('/Users/allen/Desktop/download.png')
	#img = cv2.imread('/Users/allen/Desktop/download.png',cv2.IMREAD_GRAYSCALE)
#	print(CNN_predict_grid('/Users/allen/Desktop/download.png'))
	#img = cv2.imread('/Users/allen/Desktop/five.png',cv2.IMREAD_GRAYSCALE)
	#print(CNN_predict_single(img))
	#img = cv2.imread("/Users/allen/Desktop/three.png")
	#img = cv2.resize(img, (28, 28))
	#print(blankSpot(img))

