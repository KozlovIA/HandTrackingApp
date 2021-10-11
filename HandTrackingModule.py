import cv2
import mediapipe as mp
import time
from pynput import mouse
from pynput.mouse import Button, Controller
from win32api import GetSystemMetrics
import numpy as np
import autopy



#from mediapipe.python.solutions.hands import HandLandmark

#from mediapipe.python.solutions import hands

class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5, CameraNumber = 0):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.CameraNumber = CameraNumber
        self.finishWhile = False
        self.screenWidth = GetSystemMetrics(0)
        self.screenHeight = GetSystemMetrics(1)
        self.mousePreviousPos = "None"
        self.mouseRectangleCoord = [(100, 75), (500, 325)]


    def findHands(self, img, draw = True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo = 0, draw = True):       # handNo = 0 or -1
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                #print(id, cx, cy)
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 100, 100), cv2.FILLED)
        return lmList




    def main(self, CameraNumber = 0, outputCam = True):
        pTime = 0   #previous
        cTime = 0   #current
        #detector = handDetector(CameraNumber = CameraNumber)
        cap = cv2.VideoCapture(CameraNumber)

        while True:
            success, img = cap.read()    # success = True/false. if frame is reading
            img = cv2.resize(img, (600, 400))
            img = self.findHands(img)
            lmList = self.findPosition(img)
            lmList_1 = self.findPosition(img, -1, True)
            # Работа с мышью -------------------------------------------------
            if len(lmList) > 8:
                cv2.rectangle(img, self.mouseRectangleCoord[0], self.mouseRectangleCoord[1], (100, 250, 20), 3)
                cv2.circle(img, ([lmList[8][1], lmList[8][2]]), 10, (200, 100, 250), cv2.FILLED)
                if lmList[8][1] >= self.mouseRectangleCoord[0][0] and lmList[8][2] >= self.mouseRectangleCoord[0][1] and lmList[8][1] <= self.mouseRectangleCoord[1][0] and lmList[8][2] <= self.mouseRectangleCoord[1][1]:
                    self.mouse_control([lmList[8][1], lmList[8][2]])   # 8 значит что работаем с верхней фалангой указательного пальца
            #if len(lmList) !=0:
            #    print(lmList[4])
            #if len(lmList_1) !=0:
            #    print(lmList_1[4])
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (25, 240, 10), 2)
            if outputCam:
                cv2.imshow("Image", img)
            cv2.waitKey(1)
            if self.finishWhile:
                break

    def close_window(self):
        cv2.destroyWindow("Image")

    def mouse_control(self, pos):
        mouseMove = Controller()
        if self.mousePreviousPos == "None":
            self.mousePreviousPos = mouseMove.position
        newPos = [np.interp(pos[0], [self.mouseRectangleCoord[0][0], self.mouseRectangleCoord[1][0]], [0, self.screenWidth-1]),
        np.interp(pos[1], [self.mouseRectangleCoord[0][1], self.mouseRectangleCoord[1][1]], [0, self.screenHeight-1])]
        print("IINNFFOO", pos, int(newPos[0]), int(newPos[1]))
        #mouseMove.move(int(tuple(newPos)[0] - self.mousePreviousPos[0]), int(tuple(newPos)[1] - self.mousePreviousPos[1]))
        autopy.mouse.move(self.screenWidth-1 - int(newPos[0]), int(newPos[1]))
        #self.mousePreviousPos = mouseMove.position



if __name__ == "__main__":
    test = handDetector()
    test.main(1)

    """     while True:
        break
    test.mouse_control() """