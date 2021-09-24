import cv2 as cv
import mediapipe as mp


class ImagePoseEstimator:
    def __init__(self, image_path, key_points):
        self.key_points = key_points
        image = cv.imread(image_path)
        mDraw = mp.solutions.drawing_utils
        mPose = mp.solutions.pose
        mp_holistic = mp.solutions.holistic
        pose = mPose.Pose()

        scale_percent = 70  # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)
        image = resized
        result = pose.process(image)

        myList = []
        if result.pose_landmarks.landmark:
            # print(result.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER])
            for index, lm in enumerate(result.pose_landmarks.landmark):
                h, w, c = image.shape
                if self.key_points.__contains__(index):
                    if lm.visibility > 0.8:
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        value = self.key_points[index]
                        cv.circle(image, (cx, cy), 2, (0, 0, 255), 2)
                        cv.putText(image, value, (cx, cy), cv.FONT_HERSHEY_PLAIN, 0.8, (255, 0, 0), 1)
                        print(f'{value}[{lm}]')
        cv.imshow("IMAGE", image)
        key = cv.waitKey(0) & 0xFF
        if key == 27:
            cv.destroyAllWindows()
