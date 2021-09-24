from VidePoseEstimator import VideoPoseEstimator

def main():
        #video_pose = VideoPoseEstimator("Resources/Videos/Video01.mp4", key_points)
    
    '''jsonObj= json.dumps(keypoints)
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 8500                # Reserve a port for your service.

    s.connect((host, port))
    connection = True

    while(connection):
        message = input(" > ")
        s.sendall(bytes(jsonObj,encoding="utf-8"))
        #s.send(message.encode("UTF-8"))
        print(f"{s.recv(1024)}")

        if(message=="exit"):
            connection = False

    s.close()'''

if __name__=="__main__":
    key_points = {
        0: "NOSE_TIP", #0
        11: "LEFT_SHOULDER", #1
        12: "RIGHT_SHOULDER", #2
        13: "LEFT_ELBOW",   #3
        14: "RIGHT_ELBOW",  #4
        15: "LEFT_WRIST",   #5
        16: "RIGHT_WRIST",  #6
        23: "LEFT_HIP", #7
        24: "RIGHT_HIP",    #8
        25: "LEFT_KNEE",    #9
        26: "RIGHT_KNEE",   #10
        27: "LEFT_ANKLE",   #11
        28: "RIGHT_ANKLE",   #12
        31: "LEFT_FOOT", #13
        32: "RIGHT_FOOT" #14
        }
    video_pose = VideoPoseEstimator("Resources/Videos/Video01.mp4", key_points)
'''
import numpy as np
import cv2
import time

import socket
host = socket.gethostname()
port = 9000
Message = "0"
clientSock = socket.socket()
clientSock.connect((host, port))
connection = True
'''

#lower = { 'blue':(100,100,100),'green':(40, 40, 100),'orange':(5, 40, 100),'red':(166, 84, 141) }
#upper = { 'blue':(140,255,255),'green':(60,255,255),'orange':(20,255,255),'red':(186,255,255)}

'''font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (50,50)
fontScale              = 1
color              = (0,255,0)
thickness              = 2

img_width, img_height = 400,300
dim = (img_width, img_height)

lower_blue = np.array([100,100,60])
upper_blue = np.array([150,255,200])

cap = cv2.VideoCapture(0)
while(connection):
    ret, frame = cap.read()
    #frame = cv2.convertScaleAbs(frame, alpha=1, beta=-20)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    blur = cv2.blur(hsv,(3,3))
    #blur = cv2.GaussianBlur(hsv,(2,2),3)
    #median = cv2.medianBlur(hsv,5)
    hsv=blur

    kernel = np.ones((5,5),np.uint8)
    #closing = cv2.morphologyEx(hsv, cv2.MORPH_CLOSE, kernel)
    #hsv=closing


    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('mask',mask)
    

    contours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]

    areas = [cv2.contourArea(c) for c in contours]
    #print(areas)
    try:
        max_index = np.argmax(areas)
        cnt=contours[max_index]
        M = cv2.moments(cnt)
        #print(M)
        
        area = cv2.contourArea(cnt)

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        #print(area)
        print(cx,cy)
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(hsv,(x,y),(x+w,y+h),(0,255,0),2)

        Message=str(-(cx-320)*(3.7/320))

        clientSock.send(Message.encode("UTF-8"))
    except:
        Message = "0"
        clientSock.send(Message.encode("UTF-8"))
    #print("none exist")
        pass

    frame = cv2.putText(hsv, str(str(cx)+","+str(Message)), (cx,cy), font,  fontScale, color, thickness, cv2.LINE_AA) 
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        connection = False
        clientSock.close()
        cv2.destroyAllWindows()
'''