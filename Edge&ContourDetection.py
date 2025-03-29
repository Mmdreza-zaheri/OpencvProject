import cv2 as cv
import numpy as np


def edge_and_contour_detection(image_path):
    """
    This function performs edge and contour detection on an image.
    It first converts the image to grayscale, then applies Gaussian blur to reduce noise.
    After that, it uses the Canny edge detector to find edges in the image.
    Finally, it finds contours in the edge-detected image and draws them on the original image.
    The function takes the path of the image as input and displays the original image with contours and the edge-detected image.
    """
    img = cv.imread(image_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    cv.imshow("Blurred Image", blurred)
    edges = cv.Canny(blurred, 50, 150)

    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(img, contours, -1, (0, 255, 0), 2)

    cv.imshow("Original Image", img)
    cv.imshow("Edges", edges)
    cv.waitKey(0)
    cv.destroyAllWindows()

edge_and_contour_detection("D:\ImageProcessing\dog1.jpeg")
#
