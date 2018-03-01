import cv2

img = cv2.imread("F:\\Python\\Image\\Nene.jpg", 0)

def cuttingImage(image):
    rows = 0
    newImage = []
    while rows < img.shape[0]:
        columns = 0
        while columns < img.shape[1]:
            newImage.append(image[rows:rows + 256, columns:columns + 256])
            columns = columns + 256
        rows = rows + 256
    return newImage

newImage = cuttingImage(img)

cv2.imshow("original", img)
cv2.waitKey(0)
for image in list(newImage):
    cv2.imshow("image", image)
    cv2.waitKey(0)