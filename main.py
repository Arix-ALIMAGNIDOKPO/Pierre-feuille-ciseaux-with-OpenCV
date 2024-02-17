import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random
#ouvrir la webcam
cap = cv2.VideoCapture(0)
cap.set(3,286) #largeur
cap.set(4,303)#hauteur

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0,0] #[AI,Player]

while True :
    imgBG = cv2.imread("IMAGES/BGG.png")
    success, img = cap.read()
    desired_width = 285
    desired_height = 302
    img = cv2.resize(img, (desired_width, desired_height))
    #Find Hands 
    hands, img = detector.findHands(img)
    
    
    
    
    if startGame:
        
        if stateResult is False :
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (430,340), cv2.FONT_HERSHEY_PLAIN, 6, (255,255,255),4)
            if timer>3 :
                stateResult = True
                timer = 0
                if hands :
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0,0,0,0,0] :
                        playerMove = 1
                    if fingers == [1,1,1,1,1] :
                        playerMove = 2
                    if fingers == [0,1,1,0,0] :
                        playerMove = 3
                        
                    randnumber = random.randint(1,3)
                    imgAI =cv2.imread(f'IMAGES/{randnumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (70,200))
                    
                    print(playerMove) 
                    
                    if playerMove :
                        if playerMove == 1 :
                            if randnumber == 3 :
                                scores[1] = scores[1]+1
                            if randnumber == 2 :
                                scores[0] = scores[0]+1
                        
                        if playerMove == 2 :
                            if randnumber == 3 :
                                scores[0] = scores[0]+1
                            if randnumber == 1 :
                                scores[1] = scores[1]+1
                                
                        if playerMove == 3 :
                            if randnumber == 1 :
                                scores[0] = scores[0]+1
                            if randnumber == 2 :
                                scores[1] = scores[1]+1
                                
    
    
    
    imgBG[180:482, 573:858] = img
    
    
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (70,200))
    cv2.putText(imgBG, str(scores[0]), (260,176), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),4)
    cv2.putText(imgBG, str(scores[1]), (780,176), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),4)
    cv2.imshow("BG", imgBG)
    key = cv2.waitKey(1)
    if key == ord('s') :
        startGame = True
        initialTime = time.time()
        stateResult = False
    