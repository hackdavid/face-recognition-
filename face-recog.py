import os
import face_recognition
import cv2
dataset="dataset"
images=os.listdir(dataset)
img=face_recognition.load_image_file("tom.jpg")
(top,right,bottom,left)=face_recognition.face_locations(img)[0]
cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),3)
unknow_encode=face_recognition.face_encodings(img)[0]
for image in images:
    path=os.path.join(image)
    know_image=face_recognition.load_image_file(path)
    know_encode=face_recognition.face_encodings(know_image)[0]
    result=face_recognition.compare_faces([know_encode],unknow_encode)
    if result[0]==True:
        name=image.split(".")[0]
        print(name)
        cv2.putText(img,name,(left,top+10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(255,0,0),3)
        cv2.imshow("recognize",img)
        cv2.waitKey(0)
        break
    else:
        print("unknow person")
