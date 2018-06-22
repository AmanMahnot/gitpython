import cv2
import os
import PIL
from PIL import Image
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'
recognizer.read('recg/trainData.yml')
cam = cv2.VideoCapture(0)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        
        if(conf<50):
            if(Id==0):    
                cv2.putText(im, "Ram",(100, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 1):
                cv2.putText(im, "Rahul",(125, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 2):
                cv2.putText(im, "Rajesh",(150, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 3):
                cv2.putText(im, "x",(200, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 4):
                cv2.putText(im, "y",(220, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 5):
                cv2.putText(im, "z",(250, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 6):
                cv2.putText(im, "w",(300, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))    
            else:
                cv2.putText(im, "unknown",(350, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))    
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
