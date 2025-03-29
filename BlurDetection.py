import cv2 as cv
import numpy as np

# Load the image
img = cv.imread(cv.samples.findFile('D:\ImageProcessing\BlurImage.jpeg'))
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def DetectBlur(imgray , threshold=500):
    # Calculate the Laplacian of the image and then the variance
    # to determine if the image is blurry or not
    laplacian = cv.Laplacian(imgray, cv.CV_64F)
    variance = laplacian.var()
    
    # If variance is less than a certain threshold, the image is considered blurry
    if variance > threshold:
        text = "Image is Not Blurry"
        color = (0, 255, 0)
    else:
        text = "Image is Blurry"
        color = (0, 0, 255)
    cv.putText(img, text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


DetectBlur(imgray, threshold=500)
# The function DetectBlur takes an image and a threshold value as input.
# It calculates the Laplacian of the image and its variance.