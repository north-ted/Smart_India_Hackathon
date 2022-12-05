import cv2
import HandTracking as htm
totalFingers = 0
fingers = []


class gesture():
    def __init__(self):
        self.wcam = 640
        self.hcam = 480
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.wcam)
        self.cap.set(4, self.hcam)
        self.tipIds = [4, 8, 12, 16, 20]
        self.x = 0
        self.y = 0
        self.z1 = 0
        self.z2 = 0
        self.z3 = 0
        self.detector = htm.handDetector(detectionCon=0.75)

    def hands(self):
        success, img = self.cap.read()
        img = self.detector.findHands(img)
        lmlist = self.detector.findPosition(img, draw=False)
        if len(lmlist) != 0:
            global fingers
            fingers = []
            if lmlist[self.tipIds[0]][1] > lmlist[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                if lmlist[self.tipIds[id]][2] < lmlist[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            global totalFingers
            # if len(fingers) != 0:
            #     print(lmlist[4][2]-lmlist[8][2])
            # print(abs(lmlist[0][2]-lmlist[17][2]) > abs(lmlist[0][1]-lmlist[17][1]))
            if lmlist[4][2]-lmlist[8][2] <30 and fingers[2]:
                print("Super")
            # if lmlist[0][2]-lmlist[17][2] > 100 or lmlist[0][2]-lmlist[17][2] < -75:
            #     totalFingers= fingers.count(1)
            if abs(lmlist[0][2]-lmlist[17][2]) > abs(lmlist[0][1]-lmlist[17][1]):
                totalFingers = fingers.count(1)
            else:
                totalFingers = 1
                if(lmlist[4][2]>lmlist[3][2]): print("Thumbs down")
                else: print("Thumbs up")
                print(lmlist[4][2]-lmlist[8][2])

            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
            return totalFingers
            # i = 0
            # for i in range(0, 20):
            #     fingers.append(totalFingers)
            #     i = i + 1
            # i = 0
            # for i in range(0, 4):
            #     if fingers.count(i) > 12:
            #         totalFingers = i

        cv2.imshow("Image", img)
        cv2.waitKey(1)


    def direction(self):
        success, img = self.cap.read()
        img = self.detector.findHands(img)
        lmlist = self.detector.findPosition(img, draw=False)
        # print(self.x)
        # print(fingers)
        dirn = -1
        if len(lmlist) != 0:

            if self.y - lmlist[0][2] > 10:
                dirn = 0
            elif self.y - lmlist[0][2] < -10:
                dirn = 1
            elif self.x - lmlist[0][1] > 10:
                dirn = 2
            elif self.x - lmlist[0][1] < -10:
                dirn = 3
            elif ((self.z1 - lmlist[4][2]) - (self.z2 - lmlist[8][2]))< -5 and fingers==[1,1,0,0,0] :
                dirn = 4
                # print("Zoom in")
            elif ((self.z1 - lmlist[4][2]) - (self.z2 - lmlist[8][2]))> 5 and fingers==[1,1,0,0,0]:
                dirn = 5
                # print("Zoom out")
            # if (self.z2  - lmlist[8][2])*(-self.z3 + lmlist[8][1]) > 100:
            #     print("clockwise")
            # elif (self.z2  - lmlist[8][2])*(-self.z3 + lmlist[8][1]) < -100:
            #     print("Anti")
            # print((self.z2  - lmlist[8][2])*(-self.z3 + lmlist[8][1]))
            self.x = lmlist[0][1]
            self.y = lmlist[0][2]
            self.z1 = lmlist[4][2]
            self.z2  = lmlist[8][2]
            # self.z3 = lmlist[8][1]
            # print("fffffffffff")
            # print(totalFingers)

            cv2.imshow("Image", img)
            cv2.waitKey(1)
            return dirn

        cv2.imshow("Image", img)
        cv2.waitKey(1)


def main():
    cap = cv2.VideoCapture(0)
    g1 = gesture()
    while True:
        temp = g1.hands()
        print(temp)
        g1.direction()




if __name__ == '__main__':
    main()
