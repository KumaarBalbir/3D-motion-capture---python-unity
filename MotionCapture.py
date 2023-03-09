import cv2
# get 33 landmark (33 x 3 =99 parameter ) using cvzone PoseDetector library
# we will save the landmarks pts in text file & using those text file we will make animation with unity
from cvzone.PoseModule import PoseDetector


cap=cv2.VideoCapture('Video.mp4')
detector=PoseDetector()
posList=[]
while True:
    success,img=cap.read()
    img=detector.findPose(img)
    lmList,bboxInfo=detector.findPosition(img)

    # if bbox is created loop through all lm and store it
    # lm format : [index, x,y,z ] where index will be 0 to 32
    if bboxInfo:
        lmString=''
        for lm in lmList:
            # print(lm)
            # y coordinate in opencv starts from top while in unity it starts from bottom so shift is reqd
            lmString+=f'{lm[1]},{img.shape[1]-lm[2]},{lm[3]},'
        posList.append(lmString)

    print(len(posList))





    cv2.imshow("output image",img)
    key=cv2.waitKey(1)
    if key==ord('s'):
        with open("AnimationText.txt",'w') as f:
            f.writelines(["%s\n" % item for item in posList])


