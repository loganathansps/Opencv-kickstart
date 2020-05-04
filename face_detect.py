####################################################################
###Simple program with haarcascade classifier for face detection.###
###Place the cascade xml file in the working directory           ###
#################################################################### 


import cv2 #opencv library 

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')#place the xml file in the working directly

 
cap = cv2.VideoCapture(0) #Initiating camera. '0' refers to inbuilt/default camera.
                          #change number to switch camera
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
font = cv2.FONT_HERSHEY_SIMPLEX # To put text on output screen. 

def Enquiry(faces): 
    if len(faces) == 0:
        return 0
    else:
        return 1


while True:
    #read camera frames one by one
    ret, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray,1.3,5,minSize=(20,20))
    # Draw the rectangle around each face
    if Enquiry(faces):
        cv2.putText(img, 'FACE_DETECTED',(50,50),font,1,(0,255,255),2,cv2.LINE_4) #Print confirmation over display
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()

