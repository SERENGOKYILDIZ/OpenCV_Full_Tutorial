import cv2
import matplotlib.pyplot as plt # New image viewer

img = cv2.imread("Resources/Photos/park.jpg")
cv2.imshow("Park", img)

# plt.imshow(img) # Displays the BGR image as if it were RGB.
# plt.show()

######### BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

######### BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

######### BGR to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

######### BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)

######### HSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("HSV ---> BGR", hsv_bgr)

######### LAB to BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow("LAB ---> BGR", lab_bgr)

plt.imshow(rgb)
plt.show()



cv2.waitKey(0)