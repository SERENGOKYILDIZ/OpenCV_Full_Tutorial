import cv2

img = cv2.imread("Resources/Photos/cats.jpg")
cv2.imshow("Cats", img)

######### Averaging
average = cv2.blur(img, (3, 3))
cv2.imshow("Average Blur", average)

######### Gaussian Blur
gauss = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow("Gaussian Blur", gauss)

######### Median Blur
median = cv2.medianBlur(img, 3)
cv2.imshow("Median Blur", median)

######### Bilateral Blur
bilateral = cv2.bilateralFilter(img, 10, 35, 25)
cv2.imshow("Bilateral Blur", bilateral)

cv2.waitKey(0)