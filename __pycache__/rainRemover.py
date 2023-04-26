import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('"C:/Users/nithi/Downloads/pexels-kelly-3723675-4096x2160-24fps.mp4"')

while (cap.isOpened()):
    # Read each frame
    ret, frame = cap.read()
    if ret == True:
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Thresholding to identify raindrops
        ret, thresh = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # Morphological opening to remove noise particles
        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # Use the opening image as a mask to remove raindrops
        result = cv2.bitwise_and(frame, frame, mask=opening)

        # Display the resulting video
        cv2.imshow('Result', result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and destroy all windows

cap.release()
cv2.destroyAllWindows()
