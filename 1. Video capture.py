import cv2
from tracker import * #tracking contain 8 tracking algo

# https://pyimagesearch.com/2018/07/30/opencv-object-tracking/


cap = cv2.VideoCapture(r"C:\Users\nithi\OneDrive\Desktop\full stack data science & ai with chatgpt\10OCTOBER\11oct-timeseries, object tracking live\object_tracking\highway.mp4")

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()