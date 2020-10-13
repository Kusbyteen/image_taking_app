from datetime import datetime as dt
import time
import cv2
import os


capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
img_counter = 0
frame_set = []
start_time = time.time()

if dt(dt.now().year, dt.now().month, dt.now().day, 18) < dt.now() <  dt(dt.now().year, dt.now().month, dt.now().day, 21):
    while True:
        current_time = dt(dt.now().year, dt.now().month, dt.now().day,dt.now().hour,dt.now().minute,dt.now().second)
        time_stamp = current_time.strftime('%Y-%m-%d-%H-%M-%S')
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time.time() - start_time >= 60: #<---- Check if 5 sec passed

            img_name = "{}.png".format(time_stamp)
            cv2.imwrite(img_name, frame)
            print("{} {} written!".format(current_time, img_counter))
            start_time = time.time()
        img_counter += 1
else:
    print("You are out of the time range")
