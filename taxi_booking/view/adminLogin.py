from tkinter import *
from models.adminModel import adminModel
from controllers.adminControll import adminControl


class adminLogin:
    def __init__(self, root):
        self.root = root

        self.adminloginPage()

    def adminloginPage(self):
        self.adminLoginFrame = Frame(self.root, background="#d5f4e6")
        self.adminLoginFrame.place(relx=0, rely=0, height=768, width=1366)
        # self.adminLoginFrame = Toplevel(self.root)

        # self.adminLoginFrame.title("Admin Page")

        # self.adminLoginFrame.geometry("1366x724+-13+-11")
        # self.adminLoginFrame.minsize(1, 1)
        # self.adminLoginFrame.maxsize(1351, 738)
        # self.adminLoginFrame.resizable(1, 1)
        # self.adminLoginFrame.title("Admin")
        # self.adminLoginFrame.configure(background="#87cefa")

        self.Label1 = Label(self.adminLoginFrame)
        self.Label1.place(relx=0.0, rely=0.0,height=781, width=688)
        self.Label1.configure(anchor="w")
        self.Label1.configure(compound="left")
        self.Label1.configure(font="-family {DejaVu Sans} -size 10")
        self.background = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/background.png"
        )
        self.Label1.configure(image=self.background)

        self.Label2 = Label(self.adminLoginFrame)
        self.Label2.place(relx=0.534, rely=0.055, height=102, width=641)
        self.Label2.configure(anchor="w")
        self.Label2.configure(background="#d5f4e6")
        self.Label2.configure(compound="left")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(font="-family {Purisa} -size 30 -weight bold")
        self.Label2.configure(text="""Welcome Back Admin...!!!""")

        self.Label3 = Label(self.adminLoginFrame)
        self.Label3.place(relx=0.615, rely=0.414, height=50, width=107)
        self.Label3.configure(anchor="w")
        self.Label3.configure(background="#d5f4e6")
        self.Label3.configure(compound="left")
        self.Label3.configure(font="-family {Purisa} -size 16")
        self.Label3.configure(text="""E-MAIL""")

        self.Label3_1 = Label(self.adminLoginFrame)
        self.Label3_1.place(relx=0.6, rely=0.525, height=51, width=138)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(anchor="w")
        self.Label3_1.configure(background="#d5f4e6")
        self.Label3_1.configure(compound="left")
        self.Label3_1.configure(font="-family {Purisa} -size 16")
        self.Label3_1.configure(text="""PASSWORD""")

        def del_char(event):
            self.Entry1.delete(0, END)

        self.Entry1 = Entry(self.adminLoginFrame)
        self.Entry1.place(relx=0.71, rely=0.414, height=43, relwidth=0.202)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.insert(0, "Enter the E-Mail")
        self.Entry1.bind("<FocusIn>", del_char)

        def del_passw(event):
            self.Entry1_1.delete(0, END)
            if self.Entry1_1.get() == "Enter the password":

                self.Entry1_1.configure(show="*")

        def showpassword(event):
            if self.Entry1_1.get() != "Enter the Password":
                if self.ayoo1.get() == 1:
                    self.Entry1_1.config(show="*")
                else:
                    self.Entry1_1.config(show="")

        self.ayoo1 = IntVar()
        self.showButton = Checkbutton(
            self.adminLoginFrame,
            variable=self.ayoo1,
            onvalue=1,
            offvalue=0,
            background="#d5f4e6",
            text="""Show Password""",
        )
        self.showButton.place(relx=0.71, rely=0.59, relheight=0.042, relwidth=0.100)
        self.showButton.bind("<Button-1>", showpassword)

        self.Entry1_1 = Entry(self.adminLoginFrame)
        self.Entry1_1.place(relx=0.71, rely=0.525, height=43, relwidth=0.202)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.insert(0, "Enter the Password")
        self.Entry1_1.bind("<FocusIn>", del_passw)

        self.Button1 = Button(self.adminLoginFrame)
        self.Button1.place(relx=0.830, rely=0.740, height=33, width=93)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound="left")
        self.Button1.configure(background="#FFFFFF")
        self.Button1.configure(text="""LOGIN""", command=self.login_btn1)

        def adminredirect():
            self.adminLoginFrame.destroy()

        self.Back = Button(self.adminLoginFrame)
        self.Back.place(relx=0.660, rely=0.740, height=33, width=93)
        self.Back.configure(activebackground="beige")
        self.Back.configure(background="#FFFFFF")
        self.Back.configure(borderwidth="2")
        self.Back.configure(compound="left")
        self.Back.configure(text="""BACK""", command=adminredirect)

        self.adminLoginFrame.mainloop()

    def login_btn1(self):

        user = adminModel()

        user.setEmail(self.Entry1.get())
        user.setPassword(self.Entry1_1.get())
        self.Entry1.delete("0", "end")
        self.Entry1_1.delete("0", "end")

        adminLog = adminControl()
        adminLog.adminlogin(user, self.root)
