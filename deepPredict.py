from keras.models import load_model
from keras.datasets import mnist
import matplotlib.pyplot as plt
    
import numpy



model = load_model('digits.h5')
import cv2
#model.summary()


def prepare(filepath):
	img_size = 28
	img_arr = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	new_arr = cv2.resize(img_arr, (img_size, img_size))
	new_arr = numpy.invert(new_arr)
	#plt.imshow(new_arr)
	#plt.show()
	return new_arr.reshape(-1, img_size, img_size, 1)



(X_train, y_train), (X_test, y_test) = mnist.load_data()
#plt.imshow(X_train[1], cmap="gray")
#plt.show()
img = X_train[1]
img = img.reshape(-1, 28, 28, 1)



prediction = model.predict_classes([prepare("/Users/allen/Desktop/one.png")])
#prediction = model.predict_classes(img)
#print(prediction.shape)
print(prediction)
