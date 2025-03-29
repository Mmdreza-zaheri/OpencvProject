import cv2 as cv
import numpy as np

img = cv.imread('D:\ImageProcessing\dog1.jpeg')
count = 0
circles = np.zeros((4,2), int)
print(circles)


def mousepoints(event , x , y , flags , params):
    global count
    if event == cv.EVENT_LBUTTONDOWN :
        circles[count] = x,y
        print(circles)
        count += 1
        print ('mouse clicked No' , count)
        
        
        
while True:
    if count == 4 :
        width , height = 500,500
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0] , [0,height] , [width, height]])
        matrix = cv.getPerspectiveTransform(pts1 , pts2)
        imageoutput = cv.warpPerspective(img , matrix ,(width,height))
        cv.imshow('final' , imageoutput)
        
    for x in range(0,4):
        cv.circle(img , (circles[x][0], circles[x][1]) , 3 , (255,0,0),-1)
        
    cv.imshow('dog', img)
    cv.setMouseCallback('dog', mousepoints)
    if cv.waitKey(1) & 0xFF == ord('1'):
        break

cv.destroyAllWindows()
    