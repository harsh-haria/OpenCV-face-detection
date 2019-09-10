import numpy as np
import cv2
import pickle
import math
import os
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
# eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}

cap = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow("frame1", frame)
    # cv2.imshow("frame2",gray)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:  # for printing the face detected values
        # print(x,y,w,h)
        roi_gray = gray[y:y + h, x:x + w]  # (yCord_start, yCord_end)
        roi_color = frame[y:y + h, x:x + w]
        id_, conf = recognizer.predict(roi_gray)
        if conf >= 45:
            print(id_, "", math.floor(conf), " ", labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
        img_item = "my-img.jpg"  # saving picture
        img_item1 = "my_img.jpg"
        cv2.imwrite(img_item, roi_gray)  # display result frame
        cv2.imwrite(img_item1, roi_color)
        color = (255, 0, 255)  # not rgb but bgr
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        # eyes= eye_cascade.detectMultiScale(roi_gray)
        # for(ex,ey,ew,eh) in eyes:
        #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("frame1", frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
