import cv2 as cv
import mediapipe as mp
import time
import json
import socket


class Estimator:
    def __init__(self, video_path):
        self.key_points = {
            0: "NOSE_TIP",  # 0
            11: "LEFT_SHOULDER",  # 1
            12: "RIGHT_SHOULDER",  # 2
            13: "LEFT_ELBOW",  # 3
            14: "RIGHT_ELBOW",  # 4
            15: "LEFT_WRIST",  # 5
            16: "RIGHT_WRIST",  # 6
            23: "LEFT_HIP",  # 7
            24: "RIGHT_HIP",  # 8
            27: "LEFT_ANKLE",  # 9
            28: "RIGHT_ANKLE",  # 10
            31: "LEFT_FOOT",  # 11
            32: "RIGHT_FOOT",  # 12
            7: "LEFT_EAR", #13
            8: "RIGHT_EAR" #14
        }
        self.keypoints = [
            {
                "name": "NOSE_TIP",
                "x": 1.0, "y": 5.5
            },
            {
                "name": "LEFT_SHOULDER",
                "x": 1.1, "y": 2.4
            },
            {
                "name": "RIGHT_SHOULDER",
                "x": 1.0, "y": 5.5
            },
            {
                "name": "LEFT_ELBOW",
                "x": 1.1, "y": 2.4
            },
            {
                "name": "RIGHT_ELBOW",
                "x": 1.0, "y": 5.5
            },
            {
                "name": "LEFT_WRIST",
                "x": 1.1, "y": 2.4
            },
            {
                "name": "RIGHT_WRIST",
                "x": 1.0, "y": 5.5
            },
            {
                "name": "LEFT_HIP",
                "x": 1.1, "y": 2.4
            },
            {
                "name": "RIGHT_HIP",
                "x": 1.1, "y": 2.4
            },
            {
                "name": "LEFT_ANKLE",
                "x": 1.0, "y": 5.5
            },
            {
                "name": "RIGHT_ANKLE",
                "x": 1.1, "y": 2.4
            },
            {
                "name": "LEFT_FOOT",
                "x": 1.0, "y": 5.5
            },
            {
                "name": "RIGHT_FOOT",
                "x": 1.1, "y": 2.4
            },
            {
                "name": "LEFT_EAR",
                "x": 1.0, "y": 5.5
            },
            {
                "name": "RIGHT_EAR",
                "x": 1.1, "y": 2.4
            },
        ]
        self.s = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = 9001  # Reserve a port for your service.
        self.s.connect((host, port))
        self.connection = True


        self.path = video_path

        self.mPose = mp.solutions.pose
        self.mp_holistic = mp.solutions.holistic
        self.pose = self.mPose.Pose()
        self.joint = {}
        try:
            choice = self.s.recv(1024).decode()
            print(f"GOT::{choice}")
            if choice == "0":
                self.cap = cv.VideoCapture(0)	#For WebCam Capture
                w,h = 120,150
            
            elif choice == "1":
                self.cap = cv.VideoCapture(video_path)
                w,h= 40,40
            #self.cap.open(video_path) 	#For IPWebCam Capture
            self.ptime = 0
            print("Camera SetUp Success")
        except:
            print("File not found")

        while self.connection:
            time.sleep = 0.5
            success, self.frame = self.cap.read()

            self.frame = self.resizeImage(self.frame, w, h)
            results = self.pose.process(self.frame)

            ctime = time.time()
            fps = 1 / (ctime - self.ptime)
            self.ptime = ctime

            cv.putText(self.frame, f"FPS:{int(fps)}", (30, 30), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
            self.determinePose(results)
            self.display('frame', self.frame)

            jsonObj = json.dumps(self.keypoints)
            self.s.sendall(bytes(jsonObj, encoding="utf-8"))

            key = cv.waitKey(1) & 0xFF
            msg = self.s.recv(1024).decode()
            print(f"status::{msg}")
            if key == 27 or msg == "stop":
                self.s.send("stop".encode("UTF-8"))
                connection = False
                self.s.close()
                self.close()

    def determinePose(self, results):
        if results.pose_landmarks:
            for index, lm in enumerate(results.pose_landmarks.landmark):
                if self.key_points.__contains__(index):
                    h, w, c = self.frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    value = self.key_points[index]

                    width = int(self.frame.shape[1] * 50 / 100)
                    height = int(self.frame.shape[0] * 50 / 100)

                    cv.putText(self.frame,
                               f'({round(lm.x, 2)},{round(lm.y, 2)},{round(lm.z, 2)})',
                               (cx - 50, cy + 10), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 255, 55), 1)
                    cv.putText(self.frame, f'({value})', (cx - 50, cy - 10),
                               cv.FONT_HERSHEY_PLAIN, 0.8, (0, 25, 255), 1)

                    if len(self.joint) == len(self.key_points):
                        xdiff = round(abs(lm.x - self.joint[value]['x']), 5)
                        ydiff = round(abs(lm.y - self.joint[value]['y']), 5)
                        zdiff = round(abs(lm.z - self.joint[value]['z']), 5)

                        if xdiff > 0.09 or ydiff > 0.09 or zdiff > 0.09:
                            if lm.visibility > 0.8:
                                index=1
                                if index%3==0:
                                    print(f'Push Value::{value}--diff::{xdiff},{ydiff},{zdiff}')
                                    index=index+1
                                # self.firebaseAccess.SendData(value, lm.x, lm.y, lm.z)

                    for i in range(0, len(self.key_points)):
                        if (self.keypoints[i]["name"] == value):
                            self.keypoints[i]["x"] = lm.x
                            self.keypoints[i]["y"] = lm.y
                            self.keypoints[i]["z"] = lm.z
                            print(f"{value} (x:{lm.x}, y:{lm.y}, z:{lm.z})")

    def resizeImage(self, image, widthScale= 50, heightScale= 50):
        width = int(image.shape[1] * widthScale / 100)
        height = int(image.shape[0] * heightScale / 100)
        dim = (width, height)
        image = cv.resize(image, dim, interpolation=cv.INTER_AREA)
        return image

    def display(self, name, image):
        cv.namedWindow(name)
        cv.imshow(name, image)

    def close(self):
        self.cap.release()
        cv.destroyAllWindows()
        print('Closed!')


if __name__ == "__main__":
    print("PLEASE")
    video = Estimator("Videos/Video08.mp4")
    #video = Estimator("http://192.168.1.175:8080/video")
    #video = Estimator("http://192.168.137.167:8080//video")