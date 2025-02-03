import cv2
import numpy as np

# (500, 500, 3) = (width, height, colour channel)
blank = np.zeros((500, 500, 3), dtype="uint8")
cv2.imshow("Blank", blank)

######### 1. Paint the image a certain colour

# blank[:] = 0, 255, 0 # Full coloring
# blank[200:300, 300:400] = 0, 255, 0 # Specific coloring
# cv2.imshow("Green", blank)

######### 2. Draw a Rectangle

# cv2.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=10)
# cv2.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1) # Filled Rectangle
# center_x = blank.shape[1]//2
# center_y = blank.shape[0]//2
# cv2.rectangle(blank, (0, 0), (center_x, center_y), (0, 255, 0), thickness=-1)
# cv2.imshow("Rectangle", blank)

######### 3. Draw a Circular

# cv2.circle(blank, (center_x, center_y), 40, (0, 0, 255), thickness=3)
# cv2.circle(blank, (center_x, center_y), 40, (0, 0, 255), thickness=-1) # Filled Circular
# cv2.imshow("Circular", blank)

######### 4. Draw a Line

# cv2.line(blank, (0, 0), (250, 250), (255, 0, 255), thickness=10)
# cv2.imshow("Line", blank)

######### 5. Write Text

cv2.putText(blank, "Eren", (0, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
cv2.imshow("Text", blank)


cv2.waitKey(0)