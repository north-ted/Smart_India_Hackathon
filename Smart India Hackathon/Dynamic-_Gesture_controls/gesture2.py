# import cv2
# import HandTracking as htm
#
# totalFingers = 0
# fingers = []
#
#
# class gesture():
#     def __init__(self):
#         self.wcam = 640
#         self.hcam = 480
#         # self.cap = cv2.VideoCapture(0)
#         # self.cap.set(3, self.wcam)
#         # self.cap.set(4, self.hcam)
#         self.tipIds = [4, 8, 12, 16, 20]
#         self.x = 0
#         self.y = 0
#         self.z1 = 0
#         self.z2 = 0
#         self.z3 = 0
#         self.detector = htm.handDetector(detectionCon=0.75)
#
#     def hands(self, img):
#         img = self.detector.findHands(img)
#         lmlist = self.detector.findPosition(img, draw=False)
#         if len(lmlist) != 0:
#             fingers = []
#             if lmlist[self.tipIds[0]][1] > lmlist[self.tipIds[0] - 1][1]:
#                 fingers.append(1)
#             else:
#                 fingers.append(0)
#
#             for id in range(1, 5):
#                 if lmlist[self.tipIds[id]][2] < lmlist[self.tipIds[id] - 2][2]:
#                     fingers.append(1)
#                 else:
#                     fingers.append(0)
#             fingers = fingers.count(1)
#             cv2.putText(img, str(fingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
#                         10, (255, 0, 0), 25)
#             cv2.imshow("Image", img)
#             cv2.waitKey(1)
#             # print(lmlist[8])
#             # if fingers == 1:
#             #     return 1
#             # else:
#             #     return 0
#             return fingers
#
#         cv2.imshow("Image", img)
#         cv2.waitKey(1)
#
#     def lm(self, img):
#
#         img = self.detector.findHands(img)
#         lmlist = self.detector.findPosition(img, draw=False)
#         return lmlist
#
#     def pass_frame(self, img):
#         totalFingers, img = self.hands(img)
#         return totalFingers, img
#
#
# def main():
#     cap = cv2.VideoCapture(0)
#     g1 = gesture()
#     while True:
#         temp = g1.hands(cap)
#         # print(temp)
#
#
# if __name__ == '__main__':
#     main()


import cv2
import pyautogui

import HandTracking2 as htm

totalFingers = 0
fingers = []

from pynput.keyboard import Key, Controller
import win32api
from win32con import *

keyboard = Controller()
prev = 0
num = 1



class gesture():
    def __init__(self):
        self.tipIds = [4, 8, 12, 16, 20]
        self.x = 0
        self.y = 0
        self.z1 = 0
        self.z2 = 0
        self.z3 = 0
        self.action = "No action"
        self.detector = htm.handDetector()
        self.previous = 0
        self.present = 0
        self.c = 1

    def hands(self, img):

        img = self.detector.findHands(img,draw=False)
        lmlist = self.detector.findPosition(img, draw=False)

        if len(lmlist) != 0:
            global fingers
            fingers = []
            if lmlist[self.tipIds[0]][1] < lmlist[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                if lmlist[self.tipIds[id]][2] < lmlist[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            return fingers.count(1), img
        return 0, img



    def pass_frame(self,img):
        totalFingers, img = self.hands(img)
        return totalFingers, img

    def lm(self, img):

        img = self.detector.findHands(img)
        lmlist = self.detector.findPosition(img, draw=False)
        return lmlist




