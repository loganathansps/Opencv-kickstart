######################################################
###Program to validate opencv and camera integrity ###
######################################################

import cv2 #opencv library 

cap = cv2.VideoCapture(0) #Initiating camera. '0' refers to inbuilt/default camera.
                          #change number to switch camera

while(True): #indefinite loop to handle frames one by one. 
    ret,frame = cap.read() #Read the camera frame
    cv2.imshow('video',frame) #Display/show the frame
    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to terminate the program.
        break

cap.release() #Terminate/release the camera
