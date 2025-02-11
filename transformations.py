import cv2
import numpy as np

img = cv2.imread("Resources/Photos/park.jpg")

cv2.imshow("Park", img)

######### Translation

# def translate(img, x, y):
#     # (-x) -> Left
#     # (-y) -> Up
#     # (+x) -> Right
#     # (+y) -> Down
#     transMat = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv2.warpAffine(img, transMat, dimensions)
#
#
# translated = translate(img, 100, 100)
# cv2.imshow("Translated", translated)

######### Rotation

# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
#
#     rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)
#
#     return cv2.warpAffine(img, rotMat, dimensions)
#
#
# rotated = rotate(img, 45)
# cv2.imshow("Rotated", rotated)
# rotated_rotated = rotate(rotated, 45)
# cv2.imshow("Twice Rotated", rotated_rotated)

######### Resizing

# resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
# cv2.imshow("Resized", resized)

######### Flipping (Mirroring)

# # flip = cv2.flip(img, 0) # Vertical flip
# # flip = cv2.flip(img, 1) # Horizontal flip
# flip = cv2.flip(img, -1) # Vertical and Horizontal flipping
# cv2.imshow("flip", flip)

######### Cropping

cropped = img[200:400, 300:400]
cv2.imshow("Cropped", cropped)


cv2.waitKey(0)