'''from ImagePoseEstimator import ImagePoseEstimator
from VidePoseEstimator import VideoPoseEstimator
from FirebaseAccess import FirebaseAccess

def main():
    11: "LEFT_SHOULDER",
    12: "RIGHT_SHOULDER",
    13: "LEFT_ELBOW",
    14: "RIGHT_ELBOW",
    15: "LEFT_WRIST"
    16: "RIGHT_WRIST"
    key_points = {
        23: "LEFT_HIP",
        24: "RIGHT_HIP",
        25: "LEFT_KNEE",
        26: "RIGHT_KNEE",
        27: "LEFT_ANKLE",
        28: "RIGHT_ANKLE"
    }
    video_pose = VideoPoseEstimator("Resources/Videos/Video01.mp4", key_points)
    firebaseAccess = FirebaseAccess()
    firebaseAccess.SendCategory()
    firebaseAccess.SendWords()'''
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    EMAIL = "developerbinayak@gmail.com"
    PASSWORD = "Avirtu@l@321"

    driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.

    driver.get('https://merolagani.com/LatestMarket.aspx')
    time.sleep(5)  # Let the user actually see something!
    search = driver.find_element_by_id("live-trading")

    shares = search.find_elements_by_xpath("//table/tbody/tr/td[1]")
    ltp = search.find_elements_by_xpath("//table/tbody/tr/td[2]")
    quantity = search.find_elements_by_xpath("//table/tbody/tr/td[7]")

    myshares = ["SHIVM", "NRIC", "UPPER", "NICL"]
    for index in range(0, len(shares)-1):
        if myshares.__contains__(shares[index].text):
            try:
                print(f"[share name::{shares[index].text},"
                      f" LTP::{ltp[index].text}, "
                      f" Quantity::{quantity[index].text}]")
            except:
                return;
    time.sleep(20)  # Let the user actually see something!
    driver.quit()

    driver.get("https://mail.google.com/");
    time.sleep(5)

    #email = driver.find_elements_by_class_name("whsOnd zHQkBf")
    email.send_keys(EMAIL)
    time.sleep(2)
    email.send_keys(Keys.RETURN)
    email = driver.find_element_by_id("Email")
    print(f"EMAIL::{email.text}")
    time.sleep(20)

    driver.quit()
'''