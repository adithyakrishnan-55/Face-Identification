import face_recognition
import imutils
import pickle
import time
import cv2
import os


import paho.mqtt.client as mqtt
import smtplib


sendermail=""
sender_pass=""
receiver_mail=""
# # Authentication
# s.login(sendermail,sender_pass)

# message to be sent
message = "An unknown person detected!!!"
def on_message(client, userdata, message):
    print ("Service ") ,str(message.payload.decode("utf-8"))
    
client1 = mqtt.Client() #create new instance
client1.on_message=on_message #attach function to callback
print("connecting to broker")
client1.connect("broker.hivemq.com", 1883, 60)
def sendloc(name):
    print(name)
    print("sending user name!!!")
    client1.publish("empface",name)
#find path of xml file containing haarcascade file 
# cascPathface = os.path.dirname(
#  cv2.__file__) + "haarcascade_frontalface_alt2.xml"
# load the harcaascade in the cascade classifier
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
# load the known faces and embeddings saved in last file
data = pickle.loads(open('face_enc4', "rb").read())
countuk=0
print("Streaming started")
video_capture = cv2.VideoCapture(0)
# loop over frames from the video file stream
while True:
    # grab the frame from the threaded video stream
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
 
    # convert the input frame from BGR to RGB 
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # the facial embeddings for face in input
    encodings = face_recognition.face_encodings(rgb)
    names = []
    # loop over the facial embeddings incase
    # we have multiple embeddings for multiple fcaes
    for encoding in encodings:
       #Compare encodings with encodings in data["encodings"]
       #Matches contain array with boolean values and True for the embeddings it matches closely
       #and False for rest
        matches = face_recognition.compare_faces(data["encodings"],
         encoding)
        #set name =inknown if no encoding matches
        name = "Unknown"
        # check to see if we have found a match
        if True in matches:
            #Find positions at which we get True and store them
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                #Check the names at respective indexes we stored in matchedIdxs
                name = data["names"][i]
                #increase count for the name we got
                counts[name] = counts.get(name, 0) + 1
            #set name which has highest count
            name = max(counts, key=counts.get)
 
 
        # update the list of names
        names.append(name)
        # loop over the recognized faces
        for ((x, y, w, h), name) in zip(faces, names):
            # rescale the face coordinates
            # draw the predicted face name on the image
            if(name=='unknown' or name=="Unknown"):
                countuk+=1
            if(countuk>5):
                # creates SMTP session
                # s = smtplib.SMTP('smtp.gmail.com', 587)

                # # start TLS for security
                # s.starttls()
                # s.sendmail(sendermail, receiver_mail, message)

                # # terminating the session
                # s.quit()
                break
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            sendloc(name)
            # cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
            #  0.75, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()