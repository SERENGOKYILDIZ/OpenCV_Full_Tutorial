import cv2

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return  cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)

################### Rescaling Images ###################

img = cv2.imread("Resources/Photos/cat_large.jpg")
img_resized = rescaleFrame(img, .2)

cv2.imshow("Cat", img)
cv2.imshow("Cat Resized", img_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

################### Rescaling Videos ###################
capture = cv2.VideoCapture("Resources/Videos/dog.mp4")

while capture.isOpened():
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv2.imshow("Video", frame)
    cv2.imshow("Video Resized", frame_resized)
    key = cv2.waitKey(20) & 0xff # 20 is 60 fps
    if key == ord("d") or key == ord("D"):
        break

capture.release()
cv2.destroyAllWindows()
