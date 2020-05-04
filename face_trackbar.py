###############################################################
### Program to control servo based camera pan & tilt        ###
### with face detection.Place Xml file in working directory ###
###############################################################


import cv2  #opencv library
import serial  #Serial communication library to communicate with arduino 
import time 
import sys

arduino = serial.Serial('/dev/ttyACM0', 9600)  #arduino port setup. 
time.sleep(2)
print("Connection to arduino...") 

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(1)#Initiating camera. '0' refers to inbuilt/default camera.
                          #change number to switch camera
font = cv2.FONT_HERSHEY_SIMPLEX # To put text on output screen. 

def nothing(x): #dummy variable for trackbar
    pass

#Initialize track_bar
cv2.namedWindow('img')
cv2.createTrackbar("Tilt","img",0,180,nothing)
cv2.createTrackbar("pan","img",0,180,nothing)
cv2.setTrackbarPos("Tilt","img",90) #set initial servo postion to 90 deg
cv2.setTrackbarPos("pan","img",90)  ##set initial servo postion to 90 deg
 
def Enquiry(faces):
    if len(faces) == 0:
        return 0
    else:
        return 1 

while True:
    # Read the frame
    ret, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray,1.3,5,minSize=(20,20))
    
    if Enquiry(faces):
        cv2.putText(img, 'FACE_DETECTED',(50,50),font,1,(0,255,255),2,cv2.LINE_4)# Print on display if face detected
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        
    # Display
    tilt = cv2.getTrackbarPos("Tilt","img") #Get track bar position value
    pan = cv2.getTrackbarPos("pan","img") #Get track bar position value
    data = str(tilt)+','+str(pan) #Convert interger data to string 
    data = str.encode(data) #encode data to bytes
    arduino.write(data) #send encoded data
    arduino.write(str.encode("\n")) #Terminate data
    arduino.flush()#Wait for till tha data is sent 
    cv2.imshow('img', img) #Show display
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the camera 
cap.release()

