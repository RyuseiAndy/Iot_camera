 # -*- coding: utf-8 -*-
import time
import datetime
import cv2 as cv
import requests,os
import urllib.parse as parse

token = 'LOCAL_LINENOTIF_TOKEN'
api = "https://notify-api.line.me/api/notify"

#save pisture
save_dir  = '/home/pi/image/'

#File name should be a string containing the date and time.
#Specify the file name to be appended after the date and time.
fn_suffix = 'picture.jpg'

# Create an instance of VideoCapture.
cap = cv.VideoCapture(0) 

cap.set(cv.CAP_PROP_FRAME_WIDTH, 680)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 650)

DELTA_MAX = 255

# Threshold for detecting changes in each dot
DOT_TH = 20

#How much more should we record
MOTHON_FACTOR_TH = 0.03

avg = None

while True:

    ret, frame = cap.read()     
    motion_detected = False     
    dt_now = datetime.datetime.now() 
    #date and time get
    dt_format_string = dt_now.strftime('%Y-%m-%d %H:%M:%S') 
    f_name = dt_now.strftime('%Y%m%d%H%M%S%f') + "_" + fn_suffix
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #egt compare frame
    if avg is None:
        avg = gray.copy().astype("float")
        continue

    # Calculate the difference between the current frame and the change average
    cv.accumulateWeighted(gray, avg, 0.6)
    frameDelta = cv.absdiff(gray, cv.convertScaleAbs(avg))

    # Threshold the delta image
    thresh = cv.threshold(frameDelta, DOT_TH, DELTA_MAX, cv.THRESH_BINARY)[1]
    # Calculate the motion factor. How much of the overall percentage has changed.
    motion_factor = thresh.sum() * 1.0 / thresh.size / DELTA_MAX 
    motion_factor_str = '{:.08f}'.format(motion_factor)

    # Write the date and time to the image
    cv.putText(frame,dt_format_string,(25,50),cv.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,255), 2)
    # write motion_factor value to image
    cv.putText(frame,motion_factor_str,(25,470),cv.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,255), 2)

    # If the motion factor exceeds the threshold, then motion is detected.
    if motion_factor > MOTHON_FACTOR_TH:
        motion_detected = True

        # Save the image if it has motion detection.
    if motion_detected  == True:
        #save
        cv.imwrite(save_dir + f_name, frame)
        print("DETECTED:" + f_name)

    # From here, process the image to be displayed on the screen.
    # Outline the threshold of an image
    image, contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    frame = cv.drawContours(frame, contours, -1, (0, 255, 0), 3)
    cv.imshow('camera', frame)

    # Notify line
    post_data = {'message': 'Notify'}
    headers = {'Authorization': 'Bearer ' + token}
    files={'imageFile': open(frame,'rb')}
    res = requests.post(api, data=post_data,headers=headers,files=files)
    print(res)

    k = cv.waitKey(1000)  
    if k == 27: 
        break

print("Bye!\n")

cap.release()
cv.destroyAllWindows()
