import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# adding the data images to the list for encoding 
path = 'Images Data'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

# Appending the current images in the images list
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

# finding the encodings and changing images from BGR to RGB
def findEncodings(images):
    encodeList= []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        # print(myDataList)
        nameList=[]
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')



encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Turning on the webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    # resizing the images for fast execution
    imgS= cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
# Detecting the face location from webcam and encoding it as well
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        # calculating face distance
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)

        print(faceDis)
        # Taking the minimum value of facedistance
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex]
            # Printing the name of the matched person in the terminal
            print(name)
            y1,x2,y2,x1 = faceLoc
            # resizing the cordinates so that the box around the face looks accurate
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4 
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,0),cv2.FILLED)
            # Printing the name of the person in the webcam and also a black rectangular around his face
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_ITALIC,1,(255,255,255),2)
            markAttendance(name)


    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
