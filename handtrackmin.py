import cv2
import mediapipe as mp
import time
import vlc
import time
import os
import math
import numpy as np

path = r"/home/katniss/Downloads/Friends/Friends1"
songs = os.listdir(path)
#print(songs)
        
for s in songs:
    if '.mkv' in s:
        des = path + '/' + s
        print(des)
os.system(f"vlc-ctrl play -p {des}")
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(0.9)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
lis = []
dic = {}

while True:

    success , img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,hand,mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(hand.landmark):
                h,w,c = img.shape
                #print(h,w,c)
                cx,cy = int(lm.x*w), int(lm.y*w)
                para = [id,cx,cy]
                lis.append(para)

                coordinates = [2,4,6,8,16,14,20,18,12,10]
                for i in coordinates:
                    if id == i:
                        dic[i] = cx,cy
                        #cv2.circle(img, (cx,cy),15,(255,0,255),cv2.FILLED)

                

                
                
            #volume
            #print(dic)
            #print(dic[2],dic[4])
            minvol = 0
            maxvol = 1
            cv2.line(img, (dic[4][0],dic[4][1]),(dic[8][0],dic[8][1]),(255,0,255),3)
            cv2.circle(img, (dic[4][0],dic[4][1]),15,(255,0,255),cv2.FILLED)
            cv2.circle(img, (dic[8][0],dic[8][1]),15,(255,0,255),cv2.FILLED)
            midx = (dic[4][0] + dic[8][0] )// 2
            midy = (dic[4][1] + dic[8][1]) // 2
            #print(midx,midy)
            cv2.circle(img, (midx,midy),15,(255,0,255),cv2.FILLED)
            length = math.dist(dic[4],dic[8])
            volper = np.interp(length,[50,230],[0,100])
            cv2.putText(img,f"{int(volper)}%",(40,200),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)


            
            print(length)
            if length < 55:
                cv2.circle(img, (midx,midy),15,(0,255,0),cv2.FILLED)
            volume = np.interp(length,[50,230],[minvol,maxvol])
            if dic[18][1] < dic[20][1]:
                os.system(f"vlc-ctrl volume {volume}")
                print(volume)
            
            

            


            



            
            if dic[6][1] < dic[8][1]:
                os.system("vlc-ctrl play")
                print("TWO")
            #elif dic[2][0] > dic[4][0]:
                #os.system("vlc-ctrl pause")
            #    print("THUMB")
            
            else:
                os.system("vlc-ctrl pause")
                print("NORMAL")





    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)


    