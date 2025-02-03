# CTRL + Q = Show the function
# CTRL + P = Show the parameters

import cv2

################### Reading Images ###################
img = cv2.imread("Resources/Photos/cat.jpg")

cv2.imshow("Cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

################### Reading Videos ###################

# capture = cv2.VideoCapture(0) # For webcam
capture = cv2.VideoCapture("Resources/Videos/dog.mp4")

while capture.isOpened():
    isTrue, frame = capture.read()
    # Added try code for an error that will not affect the operation of the code
    try:
        cv2.imshow("Video", frame)
    except Exception:
        break
    key = cv2.waitKey(20) & 0xff # 20 is 60 fps
    if key == ord("d") or key == ord("D"):
        break

capture.release()
cv2.destroyAllWindows()
