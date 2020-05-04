#############################################################################
### program-"color_spaces.py" shows simple demo on different color spaces ###
### available in opencv through live video capture.                       ###
############################################################################# 




import cv2  #opencv library
cap = cv2.VideoCapture(0) #Initiating camera. '0' refers to inbuilt/default camera.
                          #change number to switch camera


while(True):
    ret,frame = cap.read() #reading camera frames one by one
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # creating hsv from bgr
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB) # creating lab from bgr
    ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb) # creating ycrcb from bgr
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # creating gray scale from bgr
    #displaying different color spaces in different windows respectively
    cv2.imshow('BGR',frame)
    cv2.imshow('HSV',hsv)
    cv2.imshow('LAB',lab)
    cv2.imshow('YCrCb', ycrcb)
    cv2.imshow('GRAY', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to quit the program. 
        break

cap.release() #Terminate the camera
