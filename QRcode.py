import cv2 as cv
import qrcode
qrcode_img = cv.imread ('D:\ImageProcessing\qrcode.jpg', cv.IMREAD_COLOR)
detector  = cv.QRCodeDetector()

value, box, _ = detector.detectAndDecode(qrcode_img)
generated = qrcode.make('hi')
generated.save('D:\ImageProcessing\qrcode1.jpg')

generated = cv.imread('D:\ImageProcessing\qrcode1.jpg', cv.IMREAD_COLOR)
value, box, _ = detector.detectAndDecode(generated)

print(value)
print(box)
cv.imshow('QRcode', generated)
cv.waitKey(0)
cv.destroyAllWindows()

# The above code is used to generate a QR code and read the value from it.
# The code generates a QR code with the value 'hi' and saves it as 'qrcode1.jpg'.
# The code then reads the value from the generated QR code and displays it.
# The code also displays the generated QR code.
# The code uses the 'qrcode' library to generate the QR code and the 'cv.QRCodeDetector()' class to read the
