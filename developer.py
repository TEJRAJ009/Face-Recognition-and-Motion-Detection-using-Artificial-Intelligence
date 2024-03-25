from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("DEVELOPER SYSTEM")
        self.root.wm_iconbitmap("icon3.ico")

        title_lb1 = Label(self.root, text="DEVELOPERS", font=("times new romen", 35, "bold"), bg="white", fg="blue")
        title_lb1.place(x=0, y=0, width=1600, height=50)

        img_top = Image.open(r"Images\DeveloperPage.jpeg")
        img_top = img_top.resize((1580, 810), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=5, y=55, width=1580, height=810)

        #------------------------------------------------------------------------------------------------------------------------------
        # ------------------ 1st FRAME ---------------------------
        # first_Frame = Frame(f_lb1, bd=2, bg="white")
        # first_Frame.place(x=0, y=0, width=520, height=400)

        # img_1 = Image.open(r"Images\Sharad.jpeg ")
        # img_1 = img_1.resize((200, 250), Image.LANCZOS)
        # self.photoimg_1 = ImageTk.PhotoImage(img_1)

        # f_lbl1 = Label(first_Frame, image=self.photoimg_1)
        # f_lbl1.place(x=160, y=30, width=200, height=250)

        # dev1_label = Label(first_Frame, text="Sharad Baghel", font=("times new roman", 20, "bold"), bg="white")
        # dev1_label.place(x=170, y=290)

        # dev1_label = Label(first_Frame, text="( Developer )", font=("times new roman", 15), bg="white")
        # dev1_label.place(x=200, y=329)

        # # ------------------ 1st H-FRAME ---------------------------
        # firsth_Frame = Frame(f_lb1, bd=2, bg="white")
        # firsth_Frame.place(x=0, y=405, width=520, height=400)

        # img_2 = Image.open(r"Images\SahilS.jpg ")
        # img_2 = img_2.resize((200, 250), Image.LANCZOS)
        # self.photoimg_2 = ImageTk.PhotoImage(img_2)

        # f_lbl2 = Label(firsth_Frame, image=self.photoimg_2)
        # f_lbl2.place(x=160, y=30, width=200, height=250)

        # dev2_label = Label(firsth_Frame, text="Sahil Shivgan", font=("times new roman", 20, "bold"), bg="white")
        # dev2_label.place(x=175, y=290)

        # dev2_label = Label(firsth_Frame, text="( Developer )", font=("times new roman", 15), bg="white")
        # dev2_label.place(x=200, y=329)


        # #------------------------------------------------------------------------------------------------------------------------------
        # # ------------------ 2nd FRAME ---------------------------
        # second_Frame = Frame(f_lb1, bd=2, bg="white")
        # second_Frame.place(x=527, y=0, width=520, height=400)

        # img_3 = Image.open(r"Images\Tejraj.jpg ")
        # img_3 = img_3.resize((200, 250), Image.LANCZOS)
        # self.photoimg_3 = ImageTk.PhotoImage(img_3)

        # f_lbl3 = Label(second_Frame, image=self.photoimg_3)
        # f_lbl3.place(x=160, y=30, width=200, height=250)

        # dev3_label = Label(second_Frame, text="Tejraj Jadhav", font=("times new roman", 20, "bold"), bg="white")
        # dev3_label.place(x=175, y=290)

        # dev3_label = Label(second_Frame, text="( Developer )", font=("times new roman", 15), bg="white")
        # dev3_label.place(x=200, y=329)

        # # ------------------ 2nd H-FRAME ---------------------------
        # secondh_Frame = Frame(f_lb1, bd=2, bg="white")
        # secondh_Frame.place(x=527, y=405, width=520, height=400)

        # img_4 = Image.open(r"Images\SahilW.jpg ")
        # img_4 = img_4.resize((200, 250), Image.LANCZOS)
        # self.photoimg_4 = ImageTk.PhotoImage(img_4)

        # f_lbl4 = Label(secondh_Frame, image=self.photoimg_4)
        # f_lbl4.place(x=160, y=30, width=200, height=250)

        # dev4_label = Label(secondh_Frame, text="Sahil Wasta", font=("times new roman", 20, "bold"), bg="white")
        # dev4_label.place(x=180, y=290)

        # dev4_label = Label(secondh_Frame, text="( Developer )", font=("times new roman", 15), bg="white")
        # dev4_label.place(x=200, y=329)


        # #------------------------------------------------------------------------------------------------------------------------------
        # # ------------------ 3rd FRAME ---------------------------
        # third_Frame = Frame(f_lb1, bd=2, bg="white")
        # third_Frame.place(x=1054, y=0, width=520, height=400)

        # img_5 = Image.open(r"Images\Raj.jpg ")
        # img_5 = img_5.resize((200, 250), Image.LANCZOS)
        # self.photoimg_5 = ImageTk.PhotoImage(img_5)

        # f_lbl5 = Label(third_Frame, image=self.photoimg_5)
        # f_lbl5.place(x=160, y=30, width=200, height=250)

        # dev5_label = Label(third_Frame, text="Raj Joshi", font=("times new roman", 20, "bold"), bg="white")
        # dev5_label.place(x=200, y=290)

        # dev5_label = Label(third_Frame, text="( Developer )", font=("times new roman", 15), bg="white")
        # dev5_label.place(x=200, y=329)

        # # ------------------ 3rd H-FRAME ---------------------------
        # thirdh_Frame = Frame(f_lb1, bd=2, bg="white")
        # thirdh_Frame.place(x=1054, y=405, width=520, height=400)

        # img_6 = Image.open(r"Images\Raj.jpg ")
        # img_6 = img_6.resize((200, 250), Image.LANCZOS)
        # self.photoimg_6 = ImageTk.PhotoImage(img_6)

        # f_lbl6 = Label(thirdh_Frame, image=self.photoimg_6)
        # f_lbl6.place(x=160, y=30, width=200, height=250)

        # dev6_label = Label(thirdh_Frame, text="MS. G. D. Patne", font=("times new roman", 20, "bold"), bg="white")
        # dev6_label.place(x=165, y=290)

        # dev6_label = Label(thirdh_Frame, text="( Guide )", font=("times new roman", 15), bg="white")
        # dev6_label.place(x=220, y=329)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()