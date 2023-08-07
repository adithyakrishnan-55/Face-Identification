import cv2
import os

def capface(path,side):
    countuk=0
    print("Streaming started")
    print(path)
    video_capture = cv2.VideoCapture(0)
    while True:
        # grab the frame from the threaded video stream
        myfolder="../dataset/"+path
        print(myfolder)
        ret, frame = video_capture.read()
        if not os.path.exists(myfolder):
                print("create new folder")
                os.makedirs(myfolder)
        cv2.imwrite(myfolder+"/"+side+" img"+str(countuk)+".jpg",frame)
        cv2.imshow("image",frame)
        cv2.waitKey(1)
        countuk+=1
        if(countuk>150):
            break
    video_capture.release()
    cv2.destroyAllWindows()