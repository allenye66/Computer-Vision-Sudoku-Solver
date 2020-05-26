from keras.models import load_model
from keras.datasets import mnist

import matplotlib.pyplot as plt

model = load_model('digits.h5')
import cv2
arr = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
#model.summary()
'''
def prepare(filepath):
	img_size = 28
	img_arr = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	new_arr = cv2.resize(img_arr, (img_size, img_size))
	return new_arr.reshape(-1, img_size, img_size, 1)
'''


(X_train, y_train), (X_test, y_test) = mnist.load_data()

#plt.imshow(X_train[0], cmap="gray")
#plt.show()
img = X_train[0]
img = img.reshape(-1, 28, 28, 1)
#print(type(img))
#prediction = model.predict([prepare("/Users/allen/Desktop/three.png")])
prediction = model.predict(img)
print(prediction)
print(arr[int(prediction[0][0])])
print(type(prediction))