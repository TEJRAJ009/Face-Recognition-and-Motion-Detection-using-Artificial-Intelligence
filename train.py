from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("TRAIN DATA")
        self.root.wm_iconbitmap("icon3.ico")

        title_lb1 = Label(self.root, text="Train Data Set", font=("times new romen", 35, "bold"), bg="white",
                          fg="dark green")
        title_lb1.place(x=0, y=0, width=1600, height=50)

        #----------------------- IMAGE ----------------------------------

        img_top = Image.open(r"Images\facialrecognition.png ")
        img_top = img_top.resize((1580, 330), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=5, y=55, width=1580, height=330)

        img_bottom = Image.open(r"Images\opencv_face_reco_more_data.jpg ")
        img_bottom = img_bottom.resize((1580, 400), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb1 = Label(self.root, image=self.photoimg_bottom)
        f_lb1.place(x=5, y=470, width=1580, height=400)


        #--------------------------- BUTTON --------------------------------

        b1_1 = Button(self.root, text="Train Data", cursor="hand2", font=("times new romen", 30, "bold"),
                      bg="blue", fg="white", command=self.train_classifier)
        b1_1.place(x=5, y=387, width=1580, heigh=80)



    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            # img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            img = Image.open(image).convert('L')  # converting to grey scale
            imgnp = np.array(img, 'uint8')  # array data type
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imgnp)
            ids.append(id)
            cv2.imshow('Training', imgnp)
            cv2.waitKey(1)
        ids = np.array(ids)



        # ====================== Train the classifier and save ==========================

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training data completed", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
