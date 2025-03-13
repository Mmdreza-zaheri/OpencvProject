import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default(1).xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')


while (True):
    rec , frame = cap.read()
    frame_gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray,1.3,5)
    for (x,y,w,h) in faces:
        # Detect Face
        cv.rectangle(frame , (x,y) , (x+w,y+h) , (255,255,0),2)
        frame_gr_roi = frame_gray[y:y+h , x:x+w]
        frame_roi = frame[y:y+h , x:x+w]
        eyes = eye_cascade.detectMultiScale(frame_gr_roi)
        
        for (ex,ey,ew,eh) in eyes :
            cv.rectangle(frame_roi , (ex , ey) , (ex+ew,ey+eh) , (0,255,0) , 2)
            
        smiles = smile_cascade.detectMultiScale(frame_gr_roi , 1.8,20)

        
        for (sx , sy ,sh , sw) in smiles:
            cv.rectangle(frame_roi , (sx,sy) , (sx+sw , sy+sh) , (0,0,255) ,2)
    cv.imshow('fram',frame)
    
    exit_key = cv.waitKey(5)

    if exit_key == 27 :
        break
    
cv.destroyAllWindows()
cap.release()
