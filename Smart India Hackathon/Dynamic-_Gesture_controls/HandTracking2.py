import cv2
import mediapipe as mp
import numpy as np
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        # To create an object for mpHands module
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()

        # To create an object for mpDraw module used to join landmarks for a hand
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    for id, lm in enumerate(handLms.landmark):
                        # print(id,lm)

                        # height,width and channel of the image
                        h, w, c = img.shape

                        # position of each points in int
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        # print(id, cx, cy)

                        # To highlight a specific landmark
                        # if id==4:
                        #     cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
                        # if id==12:
                        #     cv2.circle(img,(cx,cy),10,(0,255,255),cv2.FILLED)
                    # To draw landmarks
                    if draw:
                        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS,
                        self.mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=3),
                        self.mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))
        return img

    # def distance(self,x1, x2, y1, y2):
    #     return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        # print(lmList)
        return lmList


def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 3)
        cv2.imshow("Video", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()


# import cv2
# import mediapipe as mp
# import time
#
#
# class handDetector():
#     def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
#         self.mode = mode
#         self.maxHands = maxHands
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#
#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands()
#         self.mpDraw = mp.solutions.drawing_utils
#
#     def findHands(self, img, draw=True):
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)
#         # print(results.multi_hand_landmarks)
#
#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, handLms,
#                                                self.mpHands.HAND_CONNECTIONS)
#         return img
#
#     def findPosition(self, img, handNo=0, draw=True):
#
#         lmList = []
#         if self.results.multi_hand_landmarks:
#             myHand = self.results.multi_hand_landmarks[handNo]
#             for id, lm in enumerate(myHand.landmark):
#                 # print(id, lm)
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 # print(id, cx, cy)
#                 lmList.append([id, cx, cy])
#                 if draw:
#                     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
#
#         return lmList
#
#
# def main():
#     pTime = 0
#     cTime = 0
#     cap = cv2.VideoCapture(1)
#     detector = handDetector()
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img)
#         if len(lmList) != 0:
#             print(lmList[4])
#
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#
#         cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
#                     (255, 0, 255), 3)
#
#         cv2.imshow("Image", img)
#         cv2.waitKey(1)
#
#
# if __name__ == "__main__":
#     main()
