from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        self.root.wm_iconbitmap("icon3.ico")

        title_lb1 = Label(self.root, text="Face Recognition", font=("times new romen", 35, "bold"), bg="white", fg="dark green")
        title_lb1.place(x=0, y=0, width=1600, height=50)

        img_left = Image.open(r"Images\face_detector1.jpg  ")
        img_left = img_left.resize((650, 800), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_left)

        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=650, height=800)

        img_right = Image.open(
            r"Images"
            r"\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3"
            r"-100740902-large.jpg  ")
        img_right = img_right.resize((950, 800), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_right)

        f_lb1 = Label(self.root, image=self.photoimg_bottom)
        f_lb1.place(x=650, y=55, width=950, height=800)

        # button
        b1_1 = Button(f_lb1, text="Face Recognition", cursor="hand2", font=("times new romen", 18, "bold"),
                      bg="blue", fg="white", command=self.recogintion)
        b1_1.place(x=370, y=710, width=210, heigh=40)


    #------------------------------------- ATTENDANCE --------------------------------------------

    def mark_attendance(self,i,r,n,d):
        with open("attendance_report/Attendance.csv", "r+", newline="\n")as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



    # +++++++++++++++++++++++++++++face Recognition++++++++++++++++++++++++++++++++++++++++++++++++

    def recogintion(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
 
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="BlackBerry@0314",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                # to print id on output window
                my_cursor.execute("select Name from student where Student_id =" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id =" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id =" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id =" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 80:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll No:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("FACE_RECOGNITION", img)

            if cv2.waitKey(1) == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
