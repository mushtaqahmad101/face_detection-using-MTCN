import cv2
from mtcnn import MTCNN

cap = cv2.VideoCapture(0)
detector = MTCNN()
while True:

    ret, frame = cap.read()
    output = detector.detect_faces(frame)

    for single_output in output:
        x,y,width,height =  single_output['box']
        cv2.rectangle(frame,pt1 = (x,y),pt2 = ( x+ width, y +height), color = (255,0,0),thickness = 3)

    cv2.imshow('live camera',frame)
    if cv2.waitKey(10) & 0xFF == ord('a'):

        break

cv2.destroyAllWindows()







