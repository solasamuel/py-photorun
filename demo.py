import cv2

image = cv2.imread("abstract-image.jpg")
image = cv2.bitwise_not(image)

cv2.imshow("This is the processed image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()