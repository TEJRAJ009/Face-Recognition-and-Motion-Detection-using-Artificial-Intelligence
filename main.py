import tkinter.messagebox
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from motion_detection import Motion_Detection
from student import Student
from train import Train
from attendance import Attendance
from face_recognition import Face_recognition
from developer import Developer
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("FACE RECOGNITION AND MOTION DETECTION SYSTEM")
        self.root.wm_iconbitmap("icon3.ico")

        # 1st Image
        img = Image.open(r"Images\Building.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=500, height=130)

        # 2nd image
        img1 = Image.open(r"Images\gprlogo2.jpg")
        img1 = img1.resize((370, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=550, y=0, width=500, height=130)

        # 3rd image
        img2 = Image.open(r"Images\department.jfif")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=1100, y=0, width=500, height=130)

        # 4th bgimage
        img3 = Image.open(r"Images\bg11.jpg")
        img3 = img3.resize((1600, 900), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1600, height=900)

        title_lb1 = Label(bg_img, text="FACE RECOGNITION AND MOTION DETECTION SYSTEM", font=("times new romen", 35, "bold"), bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1600, height=50)


        # =================================== Time ===============================================

        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000, time)

        lb1 = Label(title_lb1, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lb1.place(x=0, y=(-15), width=110, height=50)
        time()


        
        #--------------------------- STUDENT BUTTON ---------------------------

        img4 = Image.open(r"Images\student-portal_1.jpg")
        img4 = img4.resize((250, 250), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=160, y=90, width=250, heigh=250)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new romen", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=160, y=340, width=250, heigh=40)



        #--------------------------- FACE RECOGNITION BUTTON ---------------------------

        img5 = Image.open(r"Images\face1.jpg")
        img5 = img5.resize((250, 230), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b2.place(x=500, y=90, width=250, heigh=250)

        b2_1 = Button(bg_img, text="Face Recognition ", cursor="hand2", command=self.face_data, font=("times new romen", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=340, width=250, heigh=40)



        #--------------------------- ATTENDANCE BUTTON ---------------------------

        img6 = Image.open(r"Images\atten3.jfif")
        img6 = img6.resize((250, 250), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b3.place(x=840, y=90, width=250, heigh=250)

        b3_1 = Button(bg_img, text="Attendace", cursor="hand2", command=self.attendance_data, font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b3_1.place(x=840, y=340, width=250, heigh=40)



        #--------------------------- MOTION DETECTION BUTTON ---------------------------

        img7 = Image.open(r"Images\motiond.jpg")
        img7 = img7.resize((250, 250), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.motion_det)
        b4.place(x=1180, y=90, width=250, heigh=250)

        b4_1 = Button(bg_img, text="Motion Detection", cursor="hand2", command=self.motion_det, font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b4_1.place(x=1180, y=340, width=250, heigh=40)



        #--------------------------- TRAIN DATA BUTTON ---------------------------

        img8 = Image.open(r"Images\face2.jpg")
        img8 = img8.resize((250, 250), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b5.place(x=160, y=400, width=250, heigh=250)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,
                      font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b5_1.place(x=160, y=650, width=250, heigh=40)



        #--------------------------- PHOTO FOLDER BUTTON ---------------------------

        img9 = Image.open(r"Images\data.jfif")
        img9 = img9.resize((200, 250), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_images)
        b6.place(x=500, y=400, width=250, heigh=250)

        b6_1 = Button(bg_img, text="Photo Data", cursor="hand2", font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white", command=self.open_images)
        b6_1.place(x=500, y=650, width=250, heigh=40)



        #--------------------------- DEVELOPER BUTTON ---------------------------

        img10 = Image.open(r"Images\developer.png")
        img10 = img10.resize((250, 250), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b7.place(x=840, y=400, width=250, heigh=250)

        b7_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white", command=self.developer_data)
        b7_1.place(x=840, y=650, width=250, heigh=40)



        #--------------------------- EXIT BUTTON ---------------------------

        img11 = Image.open(r"Images\exit.png")
        img11 = img11.resize((250, 250), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iexit)
        b8.place(x=1180, y=400, width=250, heigh=250)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iexit, font=("times new romen", 15, "bold"),
                      bg="darkblue", fg="white")
        b8_1.place(x=1180, y=650, width=250, heigh=40)



    def open_images(self):
        os.startfile("data")

    def iexit(self):
        self.iexit = tkinter.messagebox.askyesno("Face Reconition", "Are You Sure You Want To Exit The Appilication", parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return



    # ----------------------------------------- BUTTON FUNCTIONS ----------------------------------------------

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def motion_det(self):
        self.new_window = Toplevel(self.root)
        self.app = Motion_Detection(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()