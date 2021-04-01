import cv2
cam = cv2.VideoCapture(0)

img = cam.read()
cv2.imwrite("1.jpg", img)

del cam



