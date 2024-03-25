from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import time
import datetime


class Motion_Detection:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("MOTION DETECTION")
        self.root.wm_iconbitmap("icon3.ico")

        cap = cv2.VideoCapture(0)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

        detection = False
        detection_stopped_time = None
        timer_started = False
        # seconds to record after detection
        strad = 5

        frame_size = (int(cap.get(3)), int(cap.get(4)))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        while True:
            _, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) + len(bodies) > 0:
                if detection:
                    timer_started = False
                else:
                    detection = True
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                    out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
                    print("Started Recording!!")
            elif detection:
                if timer_started:
                    if time.time() - detection_stopped_time >= strad:
                        detection = False
                        timer_started = False
                        out.release()
                        print('Stop Recording!')
                else:
                    timer_started = True
                    detection_stopped_time = time.time()

            if detection:
                out.write(frame)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

            for (x, y, w, h) in bodies:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)




            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        out.release()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Motion_Detection(root)
    root.mainloop()
