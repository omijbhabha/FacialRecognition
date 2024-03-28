import cv2
from deepface import DeepFace
import threading

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter=0

face_match=False

reference_img=cv2.imread('reference.jpg')

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(reference_img, frame)['verified']:
            face_match=True
        else:
            face_match=False
    except ValueError:
        pass
while True:
    ret,frame=cap.read()
    if ret:
        if counter%30==0:
            try:
                threading.Thread(target=check_face,args=(frame,)).start()
            except ValueError:
                pass
        counter+=1

        if face_match:
            cv2.putText(frame,'Face Matched',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        else:
            cv2.putText(frame,'Face Not Matched',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        
        cv2.imshow('VIDEO',frame)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

cv.destroyAllWindows()