from VidePoseEstimator import VideoPoseEstimator


def main():
    key_points = {
        0: "NOSE_TIP",  # 0
        11: "LEFT_SHOULDER",  # 1
        12: "RIGHT_SHOULDER",  # 2
        13: "LEFT_ELBOW",  # 3
        14: "RIGHT_ELBOW",  # 4
        15: "LEFT_WRIST",  # 5
        16: "RIGHT_WRIST",  # 6
        23: "LEFT_HIP",  # 7
        24: "RIGHT_HIP",  # 8
        25: "LEFT_KNEE",  # 9
        26: "RIGHT_KNEE",  # 10
        27: "LEFT_ANKLE",  # 11
        28: "RIGHT_ANKLE",  # 12
        31: "LEFT_FOOT",  # 13
        32: "RIGHT_FOOT"  # 14
    }
    try:
        video_pose = VideoPoseEstimator("Videos/Video01.mp4", key_points)
    except:
        print("CANNOT SETUP")


if __name__ == "__main__":
    main()
