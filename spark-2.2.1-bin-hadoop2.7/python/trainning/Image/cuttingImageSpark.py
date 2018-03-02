import cv2
import numpy as np
from pyspark import SparkContext

img = cv2.imread("/home/superhorse/ApacheSpark/spark-2.2.1-bin-hadoop2.7/python/trainning/Image/Nene.jpg")

def cuttingImage(imag):
    rows = 0
    newImage = []
    while rows < np.shape(imag)[0]:
        columns = 0
        while columns < np.shape(imag)[1]:
            newImage.append(imag[rows:rows + 256, columns:columns + 256, 0:3])
            columns = columns + 256
        rows = rows + 256
    return newImage

newImage = cuttingImage(img)
print np.shape(newImage)

rdd = SparkContext().parallelize(img)

cv2.imshow("original", img)
cv2.waitKey(0)
for image in list(newImage):
    cv2.imshow("image", image)
    cv2.waitKey(0)
