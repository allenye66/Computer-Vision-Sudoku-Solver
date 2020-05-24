import joblib
from sklearn import datasets
# hog is used for object detection
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy

# download the dataset from openml
dataset = datasets.fetch_openml('mnist_784')
# save images of digits in a numpy array
features = numpy.array(dataset.data, 'int16')
# save correct corresponding digits in a numpy array
labels = numpy.array(dataset.target, 'int')

# find and save HOG features in a numpy array
list_hog_fd = []
for feature in features:
    # reshape each image to 28x28
    # create four cells/blocks of size 14x14
    fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualize=False)
    list_hog_fd.append(fd)
hog_features = numpy.array(list_hog_fd, 'float64')

# create classifier
clf = LinearSVC()
# train classifier with handwritten digits
clf.fit(hog_features, labels)
# save classifier in a file
joblib.dump(clf, "digits_cls.pkl", compress=3)