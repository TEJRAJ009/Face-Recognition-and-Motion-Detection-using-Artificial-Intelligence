from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("STUDENT DETAILS SYSTEM")
        self.root.wm_iconbitmap("icon3.ico")

        # ------------------------------------------- VARIABLES -------------------------------------

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_enroll_no = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        # 1st Image
        img = Image.open(r"Images\face-recognition.png")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=500, height=130)

        # 2nd image
        img1 = Image.open(r"Images\smart-attendance.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=550, y=0, width=500, height=130)

        # 3rd image
        img2 = Image.open(r"Images\students.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=1100, y=0, width=500, height=130)

        # 4th bgimage
        img3 = Image.open(r"Images\bg13.png")
        img3 = img3.resize((1600, 900), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1600, height=900)

        title_lb1 = Label(bg_img, text="Student Management System", font=("times new romen", 35, "bold"), bg="white",
                          fg="dark green")
        title_lb1.place(x=0, y=0, width=1600, height=50)

        main_Frame = Frame(bg_img, bd=2, bg="white")
        main_Frame.place(x=10, y=55, width=1570, height=675)


        #------------------------------- LEFT LABEL FRAME -------------------------------

        Left_Frame = LabelFrame(main_Frame, bd=2, bg="white", relief=RIDGE, text="Student Information",
                                font=("times new roman", 20, "bold"), fg="red")
        Left_Frame.place(x=10, y=10, width=770, height=660)

        img_left = Image.open(r"Images\students.jpg")
        img_left = img_left.resize((760, 150), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb1 = Label(Left_Frame, image=self.photoimg_left)
        f_lb1.place(x=5, y=0, width=760, height=130)


        #------------------------ CURRENT COURSE ------------------------

        current_course_Frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                          font=("times new roman", 15, "bold"), fg="green")
        current_course_Frame.place(x=5, y=135, width=760, height=125)


        #------------------------------- DEPARTMENT -------------------------------

        dep_label = Label(current_course_Frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"),
                                 width=20, state="readonly")
        dep_combo["values"] = (
            "Select Department", "Computer Engineering", "Mechanical Enineering", "Civil Engineering",
            "Electrical Engineering", "Mechatronics")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        #------------------------------- COURSE -------------------------------
        
        course_label = Label(current_course_Frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_course,
                                    font=("times new roman", 13, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select Course", "FY", "SY", "TY", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        #------------------------------- ACADEMIC YEAR -------------------------------

        year_label = Label(current_course_Frame, text="Academic Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_year,
                                  font=("times new roman", 13, "bold"), width=20, state="readonly")
        year_combo["values"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        #------------------------------- SEMESTER -------------------------------

        sem_label = Label(current_course_Frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_sem, font=("times new roman", 13, "bold"),
                                 width=20, state="readonly")
        sem_combo["values"] = ("Select Semester", "Odd Semester", "Even Semester")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        #------------------------------------ STUDENT CLASS INFORMATION ------------------------------------

        class_student_Frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, text="Student Class Information",
                                         font=("times new roman", 15, "bold"), fg="green")
        class_student_Frame.place(x=5, y=265, width=760, height=340)


        #------------------------------------ STUDENT ID ------------------------------------
        
        stud_id_label = Label(class_student_Frame, text="Student ID :", font=("times new roman", 13, "bold"),
                              bg="white")
        stud_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        stud_id_entry = ttk.Entry(class_student_Frame, textvariable=self.var_std_id, width=20,
                                  font=("times new roman", 13, "bold"))
        stud_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        #------------------------------------ STUDENT NAME ------------------------------------

        stud_name_label = Label(class_student_Frame, text="Student Name :", font=("times new roman", 13, "bold"),
                                bg="white")
        stud_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        stud_name_entry = ttk.Entry(class_student_Frame, textvariable=self.var_std_name, width=20,
                                    font=("times new roman", 13, "bold"))
        stud_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        #------------------------------------ STUDENT ENROLLMENT NO ------------------------------------

        enroll_no_label = Label(class_student_Frame, text="Enrollment No :", font=("times new roman", 13, "bold"),
                                bg="white")
        enroll_no_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        enroll_no_entry = ttk.Entry(class_student_Frame, textvariable=self.var_enroll_no, width=20,
                                    font=("times new roman", 13, "bold"))
        enroll_no_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        #------------------------------------ ROLL NO ------------------------------------
        roll_no_label = Label(class_student_Frame, text="Roll No :", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_Frame, textvariable=self.var_roll, width=20,
                                  font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        #------------------------------------ GENDER ------------------------------------

        gender_label = Label(class_student_Frame, text="Gender :", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_Frame, textvariable=self.var_gender,
                                    font=("times new roman", 13, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        #------------------------------------ DATE OF BIRTH ------------------------------------

        dob_label = Label(class_student_Frame, text="D-O-B :", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_Frame, textvariable=self.var_dob, width=20,
                              font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)


        #------------------------------------ EMAIL ------------------------------------

        email_label = Label(class_student_Frame, text="Email :", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_Frame, textvariable=self.var_email, width=20,
                                font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        #------------------------ PHONE NO ------------------------

        phone_label = Label(class_student_Frame, text="Phone No :", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_Frame, textvariable=self.var_phone, width=20,
                                font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        #------------------------ ADDRESS ------------------------

        address_label = Label(class_student_Frame, text="Address :", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_Frame, textvariable=self.var_address, width=20,
                                  font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)


        #------------------------ RADIO BUTTONS ------------------------

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_Frame, variable=self.var_radio1, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        radiobtn2 = ttk.Radiobutton(class_student_Frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1, padx=10, pady=5, sticky=W)


        #-------------------------------- BUTTONS FRAME --------------------------------

        btn_Frame = Frame(class_student_Frame, bd=2, relief=RIDGE, bg="white")
        btn_Frame.place(x=0, y=220, width=754, height=35)

        btn_save = Button(btn_Frame, text="Save", command=self.add_data, width=18, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white", bd=4)
        btn_save.grid(row=0, column=0)

        btn_update = Button(btn_Frame, text="Update", command=self.update_data, width=18,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white", bd=4)
        btn_update.grid(row=0, column=1)

        btn_delete = Button(btn_Frame, text="Delete", command=self.delete_data, width=18,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white", bd=4)
        btn_delete.grid(row=0, column=2)

        btn_reset = Button(btn_Frame, text="Reset", command=self.reset_data, width=18,
                           font=("times new roman", 13, "bold"), bg="blue", fg="white", bd=4)
        btn_reset.grid(row=0, column=3)

        btn_photo_Frame = Frame(class_student_Frame, bd=2, relief=RIDGE, bg="white")
        btn_photo_Frame.place(x=0, y=255, width=754, height=35)

        btn_take_photo = Button(btn_photo_Frame, command=self.generate_dataset, text="Take Photo Sample", width=37,
                                font=("times new roman", 13, "bold"), bg="blue", fg="white", bd=4)
        btn_take_photo.grid(row=0, column=1)


        #-------------------------------- RIGHT LABEL FRAME --------------------------------

        Right_Frame = LabelFrame(main_Frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_Frame.place(x=790, y=10, width=770, height=650)

        img_right = Image.open(r"Images\student2.jpg")
        img_right = img_right.resize((760, 150), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lb1 = Label(Right_Frame, image=self.photoimg_right)
        f_lb1.place(x=5, y=0, width=760, height=130)



        # -----------------------------------------------------TABLE Frame-------------------------------------------

        table_Frame = Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
        table_Frame.place(x=5, y=150, width=758, height=470)

        scroll_x = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_Frame, columns=(
            "dep", "course", "year", "sem", "id", "name", "enroll", "roll", "gender", "dob", "email", "phone", "address",
            "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Academic Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("enroll", text="Enrollment No")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="D-O-B")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("enroll", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    # -------------------------------------------Function declaration--------------------------------------------------

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_enroll_no.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "Select Gender" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        elif len(self.var_phone.get())!=10:
            messagebox.showerror("Error", "Enter valid phone number", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="BlackBerry@0314",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_enroll_no.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)



    # --------------------------------------FETCH DATA------------------------------------------------

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="BlackBerry@0314",
                                       database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()



    # ------------------------------------------GET CURSOR-------------------------------------------------------

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_enroll_no.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])



    # -------------------------------------- UPDATE FUNCTION -----------------------------------------------------

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="BlackBerry@0314",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s, Course=%s, Year=%s, Sem=%s, Name=%s, Enroll_no=%s, Roll=%s, "
                        "Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, PhotoSample=%s where Student_id=%s",
                        (

                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_std_name.get(),
                            self.var_enroll_no.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()

                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student Details Successfully Updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)



    # ----------------------------------------------DELETE FUNCTION----------------------------------------------

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student detail",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="BlackBerry@0314",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)



    # ----------------------------------------------------------RESET-------------------------------------------------

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_enroll_no.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")



    # ========================== Generate data set or Take photo Smaples ==========================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="BlackBerry@0314",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student set Dep=%s, Course=%s, Year=%s, Sem=%s, Name=%s, Enroll_no=%s, Roll=%s, Gender=%s,"
                    " Dob=%s, Email=%s, Phone=%s, Address=%s, PhotoSample=%s where Student_id=%s",
                    (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_enroll_no.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1

                    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ==================== Load predifiend data on face frontals from opencv ===================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor+1.3
                    # Minimum Neighbor=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, m_frame = cap.read()
                    if face_cropped(m_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(m_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
