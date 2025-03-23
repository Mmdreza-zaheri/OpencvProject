import numpy as np
import cv2 as cv

cap = cv.VideoCapture('D:\ImageProcessing\StreetVideo4.mp4', cv.CAP_FFMPEG)

ret, prev_frame = cap.read()
while cap.isOpened():
    rec, frame = cap.read()
    if not rec:
        break
    
    frame_diff = cv.absdiff(prev_frame, frame)
    frame_diff = cv.cvtColor(frame_diff, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(frame_diff, (3, 3), 1)
    _, threshold = cv.threshold(blurred, 50, 255, cv.THRESH_BINARY)
    
    contours, _ = cv.findContours(threshold , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv.contourArea(contour) > 100:
            (x,y,w,h) = cv.boundingRect(contour)
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        
    cv.imshow('frame_diff', frame_diff)
    cv.imshow('frame', frame)
    cv.imshow('threshold', threshold)
    
    prev_frame = frame.copy()

    if cv.waitKey(30) & 0xFF == ord('q'):  
        break

cap.release()
cv.destroyAllWindows()
"""

code above is used to detect moving object in a video
we use absdiff to get the difference between two frames
then we convert it to grayscale
then we blur it using GaussianBlur
then we threshold it
then we find contours
then we draw rectangle around the moving object
then we show the result
then we update the previous frame
then we wait for 30 ms
if we press q we break the loop
then we release
then we destroy all windows

"""