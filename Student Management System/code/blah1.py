from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database='stud',
    user="postgres",
    password="psql",
)

cur = conn.cursor()

class Student(object):

    def __init__(self,root):


        
        self.root = root

        self.root.title("welcome page,  .")

        self.root.geometry("500x500")

        admin_img = ImageTk.PhotoImage(Image.open("admin.png"))
        user_img = ImageTk.PhotoImage(Image.open("user.png"))

        def admin_click():
            self.Admin_page()
            return

        def user_click():
            self.login()
            import sys
            #sys.exit()
        
    

        main_frame = Frame(self.root, bg="SteelBlue")
        main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        note_point = LabelFrame(main_frame, text="Login Type......",
                                width=200, height=100, bg="SteelBlue", fg="white")
        note_point.place(x=140, y=380)

        label_note_point = Label(note_point, bg='SlateBlue', fg="white",
                                text="The admin login has the  advantage \n of the accessing all the users\n details and can modify and delete them", font=40).pack()

        admin_label = Label(main_frame, image=admin_img, width=150, height=150)
        admin_label.place(x=50, y=100)

        user_label = Label(main_frame, image=user_img, width=130, height=130)
        user_label.place(x=290, y=100)

        admin_button = Button(main_frame, text="Admin Login",
                            font=30, width=15, command=admin_click)
        admin_button.place(x=40, y=290)

        user_button = Button(main_frame, text="User Login",
                            font=30, width=15, command=user_click)
        user_button.place(x=270, y=290)
        

        

        self.root.mainloop()


        # Welcome()

        
    def Admin_page(self):
        

        self.root.title("admin Page")

        self.root.geometry("700x700")

        con = psycopg2.connect(
            host="localhost",
            database='stud',
            user="postgres",
            password="psql",
        )



        def fetch_data():
            con = psycopg2.connect(
                host="localhost",
                database='stud',
                user="postgres",
                password="psql",
            )
            cur = con.cursor()
            cur.execute("select * from login")
            rows = cur.fetchall()

            if len(rows) != 0:
                User_table.delete(*User_table.get_children())
                for row in rows:
                    User_table.insert('', END, values=row)
                    con.commit()
            con.close()

        def click():
            fetch_data()

        def delete():
            k = str(user_id.get('1.0', END))
            print(k)

            cur = con.cursor()

            cur.execute("select * from login")
            rows = cur.fetchall()

            for i in rows:
                if i[0] == k:
                    s = f"delete from login where user_id = {k}"
                    #cur.execute(f"delete from login where user_id = {k}")
                    print("delete from login where user_id")
                    print(k)
            con.commit()
            messagebox.showinfo(
                "success", "the user name {} has been deleted".format(user_id.get('1.0', END)))

        def clear():
            user_id.delete('1.0', END)
            user_name.delete('1.0', END)
            password.delete('1.0', END)

        def get_cursor(ev):
            curosor_row = User_table.focus()
            contents = User_table.item(curosor_row)
            row = contents['values']
            user_id.delete('1.0', END),
            user_id.insert(END, row[0]),
            user_name.delete('1.0', END),
            user_name.insert(END, row[1]),
            password.delete(0, END)
            password.insert(END, row[2])

        def show():

            def show2():
                password = Entry(main_frame, width=25, show="*", font=20)
                password.place(x=220, y=280)
                curosor_row = User_table.focus()
                contents = User_table.item(curosor_row)
                row = contents['values']
                password.delete(0, END)
                password.insert(END, row[2])
                show()
            password = Entry(main_frame, width=25, font=20)
            password.place(x=220, y=280)
            curosor_row = User_table.focus()
            contents = User_table.item(curosor_row)
            row = contents['values']
            password.delete(0, END)
            password.insert(END, row[2])

            eye_button = Button(main_frame, text="-->*", command=show2)
            eye_button.place(x=530, y=280)

        def back():
            self.__init__(self.root)
        main_frame = Frame(self.root, bg="PowderBlue")
        main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        back_button = Button(main_frame, text="<--  Back", bg="PowderBlue",font=30,command=back)
        back_button.place(x=5,y=15)

        get_user_details = Button(
            main_frame, text="click to get all user details", font=30, command=click, width=30)
        get_user_details.place(x=140, y=370)

        user_id_label = Label(main_frame, text="user id", bg="PowderBlue", font=30)
        user_id_label.place(x=100, y=120)

        user_id = Text(main_frame, width=25, height=1, font=20)
        user_id.place(x=220, y=120)

        user_name_label = Label(main_frame, text="user name",
                                bg="PowderBlue", font=30)
        user_name_label.place(x=100, y=200)

        user_name = Text(main_frame, width=25, height=1, font=20)
        user_name.place(x=220, y=200)

        password_label = Label(main_frame, text="Password",
                            bg="PowderBlue", font=30)
        password_label.place(x=100, y=280)

        password = Entry(main_frame, width=25, show="*", font=20)
        password.place(x=220, y=280)

        eye_button = Button(main_frame, text="-->*", command=show)
        eye_button.place(x=530, y=280)

        #modify = Button(main_frame,text="Modify",width=15,font=5)
        #modify.place(x=50,y=300)

        #delete = Button(main_frame, text="Delete", width=15, font=5,command=delete)
        #delete.place(x=400,y=300)

        heading = Label(main_frame, text="Administration Page",
                        bg="Salmon", font=40)
        heading.place(x=190, y=50)


        ###################################################################
        #################################################################
        ######################################################################
        Table_Frame = Frame(main_frame, bd=2, bg="white")
        Table_Frame.place(x=20, y=430, width=600, height=250)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)

        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        User_table = ttk.Treeview(Table_Frame, columns=(
            'id', 'User_name', 'password'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=User_table.xview)
        scroll_y.config(command=User_table.yview)

        User_table.heading("id", text="Id no")
        User_table.heading("User_name", text="User_Name")
        User_table.heading("password", text="password")
        User_table['show'] = 'headings'
        User_table.column("id", width=100)
        User_table.column("User_name", width=100)
        User_table.column("password", width=100)
        User_table.pack(fill=BOTH, expand=1)
        User_table.bind("<ButtonRelease-1>", get_cursor)

        con.commit()
        # self.root.mainloop()













    def project(self):
        

        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.bg = 'blue'

        def add_students():
            if txt_Roll.get('1.0', END) == "":
                messagebox.showerror("error", "All fields are required")
            else:
                pass

            con = psycopg2.connect(
                host="localhost",
                database='stud',
                user="postgres",
                password="psql",


            )
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (
                txt_Roll.get('1.0', END),
                txt_name.get('1.0', END),
                txt_Email.get('1.0', END),
                combo_gender.get(),
                txt_Contact.get('1.0', END),
                txt_DOB.get('1.0', END),
                txt_Address.get('1.0', END)


            ))
            con.commit()
            fetch_data()
            clear()
            con.close()
            messagebox.showinfo("Success", " Record has been inserted!")

        def fetch_data():
            con = psycopg2.connect(
                host="localhost",
                database='stud',
                user="postgres",
                password="psql",
            )
            cur = con.cursor()
            cur.execute("select * from students")
            rows = cur.fetchall()

            if len(rows) != 0:
                Student_table.delete(*Student_table.get_children())
                for row in rows:
                    Student_table.insert('', END, values=row)
                    con.commit()
            con.close()

        def clear():
            txt_Roll.delete('1.0', END)
            txt_name.delete('1.0', END)
            txt_Email.delete('1.0', END)
            combo_gender.set("")
            txt_Contact.delete('1.0', END)
            txt_DOB.delete('1.0', END)
            txt_Address.delete('1.0', END)

        def get_cursor(ev):
            curosor_row = Student_table.focus()
            contents = Student_table.item(curosor_row)
            row = contents['values']
            txt_Roll.delete('1.0', END),
            txt_Roll.insert(END, row[0]),
            txt_name.delete('1.0', END),
            txt_name.insert(END, row[1]),
            txt_Email.delete('1.0', END),
            txt_Email.insert(END, row[2]),
            combo_gender.set(row[3]),
            txt_Contact.delete('1.0', END),
            txt_Contact.insert(END, row[4]),
            txt_DOB.delete('1.0', END),
            txt_DOB.insert(END, row[5]),
            txt_Address.delete('1.0', END)
            txt_Address.insert(END, row[6])

        def update_data():
            con = psycopg2.connect(
                host="localhost",
                database='stud',
                user="postgres",
                password="psql",


            )
            cur = con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where  roll_no=%s", (
                txt_name.get('1.0', END),
                txt_Email.get('1.0', END),
                combo_gender.get(),
                txt_Contact.get('1.0', END),
                txt_DOB.get('1.0', END),
                txt_Address.get('1.0', END),
                txt_Roll.get('1.0', END)
            ))
            con.commit()
            fetch_data()
            clear()
            con.close()
            messagebox.showinfo(
                "Success", "data has been successfully updated")

        def delete_data():

            con = psycopg2.connect(
                host="localhost",
                database='stud',
                user="postgres",
                password="psql",
            )
            cur = con.cursor()
            cur.execute("delete from students where roll_no={}".format(
                txt_Roll.get('1.0', END)))
            con.commit()
            con.close()
            fetch_data()
            clear()
            messagebox.showinfo("Success", "data has been successfully ")

        def search_data():
            con = psycopg2.connect(
                host="localhost",
                database='stud',
                user="postgres",
                password="psql",
            )
            cur = con.cursor()
            v = txt_Search.get()
            s = combo_search.get()

            if s == 'Roll_no':

                cur.execute("select * from students where " +
                            str(combo_search.get()) + f" ={v}")
            elif s == 'Name':
                cur.execute("select * from students where " + str(combo_search.get()
                                                                ) + " like '%" + str(txt_Search.get()) + "%'")

            elif s == "Contact":
                cur.execute("select * from students where " + str(combo_search.get()
                                                                ) + " like '%" + str(txt_Search.get()) + "%'")

            rows = cur.fetchall()
            print(rows)

            if len(rows) != 0:
                Student_table.delete(*Student_table.get_children())
                for row in rows:
                    Student_table.insert('', END, values=row)
            con.commit()
            con.close()

        def wiki():

            messagebox.showinfo("wikipedia", "Wikipedia is increasingly used by people in the \n academic community, from freshman students to \n professors, as an easily accessible tertiary source \n for information about anything and everything, and \n as a quick 'ready reference' , to get a sense of a \n concept or idea.")

            import wikipedia

            def question_answer():
                question = el.get()
                answer = wikipedia.summary(question)
                messagebox.showinfo("answer", answer)
                return

            root = Tk()
            root.geometry("400x400")
            root.title("Wikipedia search")

            n1_frame = Frame(root, relief=RIDGE, bg="teal")
            n1_frame.place(x=1, y=1, width=400, height=400)

            Wiki_label = Label(n1_frame, text="wikipedia..", bg="teal", font=40)
            Wiki_label.place(x=140, y=50)

            n2_frame = Frame(n1_frame, relief=RIDGE, bg="teal")
            n2_frame.place(x=50, y=100, width=300, height=100)

            n3_frame = Frame(n1_frame, relief=RIDGE, bg="teal")
            n3_frame.place(x=50, y=200, width=300, height=300)

            question = StringVar()

            el = Entry(n2_frame, textvariable=question, width=30, font=100)

            el.grid(ipady=5)

            b1 = Button(n3_frame, text='search', bg="silver", font=40,
                        width=12, command=question_answer, padx=30, pady=20)
            b1.pack()

            root.mainloop()

            return


































        
        Main_Frame = Frame(self.root, relief=RIDGE, bg="green")
        Main_Frame.place(x=1, y=1, width=1350, height=700)

        New_Frame = Frame(Main_Frame, relief=RIDGE, bg="green")
        New_Frame.place(x=820, y=600, width=550, height=200)

        l1 = Label(
            New_Frame, text="open wikipedia if u have net access", bg="green", font=40)
        l1.grid(row=0, column=0)
        l2 = Label(New_Frame, text="   --->     ", bg="green", font=40)
        l2.grid(row=0, column=1)

        title = Label(Main_Frame, text="Student Management System", bd=5,
                    relief=GROOVE, font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        txt_Roll = StringVar()
        txt_name = StringVar()
        txt_Email = StringVar()
        combo_gender = StringVar()
        txt_Contact = StringVar()
        txt_DOB = StringVar()

        combo_search = StringVar()
        txt_Search = StringVar()
        Manage_Frame = Frame(Main_Frame, bd=20, relief=RIDGE, bg="blue")
        Manage_Frame.place(x=1, y=76, width=495, height=620)

        m_title = Label(Manage_Frame, text="Manage Student", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll no.", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        txt_Roll = Text(Manage_Frame, width=20, height=1, font=(
            "times new roman", 15, "bold"), relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        lbl_name = Label(Manage_Frame, text="name", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        txt_name = Text(Manage_Frame, width=20, height=1, font=(
            "times new roman", 15, "bold"), relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        lbl_Email = Label(Manage_Frame, text="Email", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        txt_Email = Text(Manage_Frame, width=20, height=1, font=(
            "times new roman", 15, "bold"), relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        lbl_Gender = Label(Manage_Frame, text="Gender", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        combo_gender = ttk.Combobox(Manage_Frame, font=(
            "times new roman", 13, "bold"), state='readonly')

        combo_gender['values'] = ('male', 'female', 'other')

        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        lbl_Contact = Label(Manage_Frame, text="Contact", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        txt_Contact = Text(Manage_Frame, width=20, height=1, font=(
            "times new roman", 15, "bold"),  relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        lbl_DOB = Label(Manage_Frame, text="DOB", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky='w')

        txt_DOB = Text(Manage_Frame, width=20, height=1, font=(
            "times new roman", 15, "bold"), relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        lbl_Address = Label(Manage_Frame, text="Address", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        txt_Address = Text(Manage_Frame, width=26, height=2)
        txt_Address.grid(
            row=7, column=1, pady=10, padx=20, sticky='w')

        btn_Frame = Frame(Manage_Frame, relief=RIDGE, bg="blue")
        btn_Frame.place(x=10, y=510, width=400)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=add_students).grid(
            row=0, column=0, padx=10, pady=10)

        #clickme = Button(btn_Frame,text="clickme",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)

        updatebtn = Button(btn_Frame, text="update", width=10, command=update_data).grid(
            row=0, column=1, padx=10, pady=10)

        deletebtn = Button(btn_Frame, text="Delete", width=10, command=delete_data).grid(
            row=0, column=2, padx=10, pady=10)

        clearbtn = Button(btn_Frame, text="Clear", width=10, command=clear).grid(
            row=0, column=3, padx=10, pady=10)

        #####################################################
        ###################################################

        Detail_Frame = Frame(Main_Frame, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=76, width=850, height=485)

        lbl_search = Label(Detail_Frame, text="Search_By", font=(
            "times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        combo_search = ttk.Combobox(Detail_Frame, width=10, font=(
            "times new roman", 13, "bold"), state='readonly')

        combo_search['values'] = ('Roll_no', 'Name', 'Contact')

        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')

        txt_Search = Entry(Detail_Frame, width=15, font=(
            "times new roman", 14, "bold"))
        txt_Search.grid(row=0, column=2, padx=20, pady=10)

        searchbtn = Button(Detail_Frame, text="search", command=search_data, width=10).grid(
            row=0, column=3, padx=10, pady=5)

        showallbtn = Button(Detail_Frame, text="show all",
                            command=fetch_data, width=10).grid(
            row=0, column=4, padx=10, pady=5)

        ########################
        #=====================Table frame======

        Table_Frame = Frame(Detail_Frame, bd=2, bg="white")
        Table_Frame.place(x=30, y=100, width=800, height=400)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        Student_table = ttk.Treeview(Table_Frame, columns=(
            'roll', 'name', 'gender', 'contact', 'email', 'dob', 'Address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)

        Student_table.heading("roll", text="Roll No.")
        Student_table.heading("name", text="Name")
        Student_table.heading("email", text="Email")
        Student_table.heading("gender", text="Gender")
        Student_table.heading("contact", text="contact")
        Student_table.heading("dob", text="D.O.B")
        Student_table.heading("Address", text="Address")

        Student_table['show'] = 'headings'
        Student_table.column("roll", width=100)
        Student_table.column("name", width=100)
        Student_table.column("email", width=120)
        Student_table.column("gender", width=100)
        Student_table.column("contact", width=100)
        Student_table.column("dob", width=100)
        Student_table.column("Address", width=150)
        Student_table.pack(fill=BOTH, expand=1)

        Student_table.bind("<ButtonRelease-1>", get_cursor)
        fetch_data()

        close_button = Button(Main_Frame, text="close", padx=10, pady=15,
                            bd=5, font=40, bg="black", fg="white", command=self.root.quit)
        close_button.place(x=700, y=630)

        clickme = Button(New_Frame, text="wikipedia", padx=10, pady=15,
                        bd=10, font=40, bg="black", fg="white", command=wiki)
        clickme.grid(row=0, column=2)

       

        root.mainloop()


















    def keys(self):
        key = '12341234'

        k = Tk()

        k.geometry("300x140")
        k.title("Key Validation")

        la = Label(k, text="enter the key to create an login account").pack()
        e = Entry(k, font=30, width=30)
        e.pack()

        def click():
            global g
            g = e.get()

            if g == key:
                messagebox.showinfo("success ,,,!!","valid key entered for verification")
                k.destroy()
                self.root.destroy()
            else:
                messagebox.showerror("ERROR ,,,!!", "Invalid key entered for verification")
                self.root.destroy()
                k.destroy()
        b = Button(k, text="verify..", padx=30,
                pady=20, bg="#808000", command=click)
        b.pack()

        k.mainloop()
        return g











    def start(self):
        self.project()







    def create(self):
        self.root = Tk()
        self.root.title("create user .")

        self.root.geometry("300x400")

        def click():
            try:
                d = []
                for i in s:
                    d.append(i[1])

                if fname not in d:
                    cur.execute(
                        f"insert into login(user_name,password) values('{fname}','{pas}')")
                    messagebox.showinfo(
                        "success", "user has been succesfully created")
                    conn.commit()
                else:
                    messagebox.showerror(
                        "ERROR!!.,,", "User name already exits!!...")

            except:
                messagebox.showerror("ERROR!!.,,", "User name already exits!!...")

        def ins():
            global fname
            global pas
            global s
            fname = e1.get()
            pas = e2.get()

            cur.execute("select * from login")
            s = cur.fetchall()
            print(s)
            click()
        frame = Frame(self.root, bg="#102301")
        frame.place(x=1, y=1, width=300, height=400)

        l1 = Label(frame, text="enter user name", padx=30,
                pady=20, bg="#102301", fg="white", font=40)
        l1.pack()

        e1 = Entry(frame, width=30, font=30)
        e1.pack()

        l2 = Label(frame, text="enter user Password", padx=30,
                pady=20, bg="#102301", fg="white", font=40)
        l2.pack()

        e2 = Entry(frame, width=30, font=30)
        e2.pack()

        l3 = Label(frame, text="            ", padx=30,
                pady=20, bg="#102301", font=40)
        l3.pack()

        sub = Button(frame, text="create", font=30,
                    padx=30, pady=10, command=ins).pack()

        self.root.mainloop()

        conn.commit()
        cur.close()
        conn.commit()










    def login(self):

        cur = conn.cursor()
        #cur.execute("INSERT INTO login(user_name ,password) VALUES('firoz','ramzan')")
        cur.execute("select * from login")
        data = cur.fetchall()

        
        self.root.title("Student Management System.")
        self.root.geometry("600x400")

        fmain = Frame(self.root, bg="Aquamarine")
        fmain.place(x=1, y=1, width=700, height=400)

        label = Label(fmain, text="           ",
                    bg="Aquamarine", font=40)
        label.grid(row=0, column=1)

        label = Label(fmain, text="Welcome to Login Page.",
                    bg="Coral", font=40)
        label.grid(row=0, column=2)

        l1 = Label(fmain, text="User name:", bg="Aquamarine",
                font=35, padx=30, pady=30)
        l1.grid(row=1, column=1)

        fn = Entry(fmain, width=30, font=20)
        fn.grid(row=1, column=2)

        l2 = Label(fmain, text="password", bg="Aquamarine",
                font=35, padx=30, pady=30)
        l2.grid(row=2, column=1)

        ps = Entry(fmain, width=30, show="*", font=20)
        ps.grid(row=2, column=2)

        def click():
            s = fn.get()
            p = ps.get()
            con = False

            for i in data:
                if s == i[1] and p == i[2]:
                    con = True

            if con == True:
                messagebox.showinfo("Login", "successfully logged in!!")
                #print("succesfully logged in")
                self.start()

            else:
                messagebox.showerror("Error", "Invalid  User name Or Pass word!!!")
                #import sys
                #sys.exit()
                self.root.destroy()

        def new():
            s = self.keys()

            if s == "12341234":
                #messagebox.showinfo("success ,,,!!", "valid key entered for verification")

                self.create()

        f = Frame(fmain, bg="Aquamarine")
        f.place(x=100, y=210, width=700, height=200)

        f2 = Frame(fmain, bg="Aquamarine")
        f2.place(x=350, y=210, width=700, height=200)
        b = Button(f2, text="login", font=35, padx=40, pady=20, bd=5,
                fg="red", command=click).grid(row=3, column=2)

        b2 = Button(f, text="Create User", font=35, padx=30, pady=18, bd=5,
                    fg="red", command=new).grid(row=3, column=3)

        self.root.mainloop()


    # login()






root = Tk()
ob=Student(root)
root.mainloop()
