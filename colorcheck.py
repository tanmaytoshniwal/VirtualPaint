import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

# Initializing the webcam feed.
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(a):
    pass

# Create 6 trackbars that will control the lower and upper range of H,S and V channels. The Arguments are like this: Name of trackbar, 
# window name, range,callback function. For Hue the range is 0-179 and for S,V its 0-255.
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)


while True:
    # Start reading the webcam feed frame by frame.
    success,img = cap.read()
    
    # Convert the BGR image to HSV image.
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    # Get the new values of the trackbar in real time as the user changes them
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Set the lower and upper HSV range according to the value selected by the trackbar
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    # Filter the image and get the binary mask, where white represents our target color
    mask = cv2.inRange(imgHSV,lower,upper)
    
    # Visualize the real part of the target color
    result = cv2.bitwise_and(img,img,mask=mask)

    # Converting the binary mask to 3 channel image, this is just so we can stack it with the others
    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    
    cv2.imshow("img",img)
    cv2.imshow("hsv",imgHSV)
    cv2.imshow("result",mask)
    cv2.imshow("result",result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        #thearray = [[h_min,s_min,v_min],[h_max,s_max,v_max]]
        #print(thearray)
        
        # Also save this array 
        #np.save('hsv_value',thearray)
        break

cap.release()
cv2.destroyAllWindows()


