import os
import cv2
import numpy as np

import PIL
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'

def getImagesWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')

        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNp)
        IDs.append(Id)

        cv2.imshow('trainer',faceNp)

        cv2.waitKey(10)
    return faces, np.array(IDs)

faces, Ids = getImagesWithID(path)
recognizer.train(faces, Ids)
recognizer.write('recg/trainData.yml')
cv2.destroyAllWindows()
