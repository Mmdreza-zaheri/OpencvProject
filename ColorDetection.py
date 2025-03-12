import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while(True):
    rec, frame = cap.read()
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower = np.array([100,50,50])
    upper = np.array([116,255,255])
    mask = cv.inRange(frame_hsv, lower, upper)
    masked = cv.bitwise_and(frame, frame, mask = mask)
    cv.imshow('frame', frame)
    cv.imshow('mask_red', mask)
    cv.imshow('frame_masked', masked)
    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()