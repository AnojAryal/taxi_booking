from tkinter import *
from view import driverRegister
from models.driverRegisterModel import driverRegisterModel
from controllers.driverRegisterControll import driverRegistercontroll


class driverLogin:
    def __init__(self, root):
        self.root = root
        # self.root.title("Taxi Booking System")
        # self.root.resizable(0, 0)
        # self.root.configure(background="#000000")
        # self.root.geometry("1366x768")

        self.driverloginPage()

    def driverloginPage(self):
        self.driverLoginFrame = Frame(self.root, background="#d5f4e6")
        self.driverLoginFrame.place(relx=0, rely=0, height=768, width=1366)

        self.Label1a = Label(self.driverLoginFrame)
        self.Label1a.place(relx=0.0, rely=0.0, height=781, width=688)
        self.Label1a.configure(anchor="w")
        self.Label1a.configure(compound="left")
        self.Label1a.configure(font="-family {DejaVu Sans} -size 10")
        self.background = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/background.png"
        )
        self.Label1a.configure(image=self.background)

        self.Label2a = Label(self.driverLoginFrame)
        self.Label2a.place(relx=0.534, rely=0.055, height=102, width=641)
        self.Label2a.configure(anchor="w")
        self.Label2a.configure(background="#d5f4e6")
        self.Label2a.configure(compound="left")
        self.Label2a.configure(cursor="fleur")
        self.Label2a.configure(font="-family {Purisa} -size 30 -weight bold")
        self.Label2a.configure(text="""Login As Driver...!!!""")

        self.Label3a = Label(self.driverLoginFrame)
        self.Label3a.place(relx=0.615, rely=0.314, height=50, width=107)
        self.Label3a.configure(anchor="w")
        self.Label3a.configure(background="#d5f4e6")
        self.Label3a.configure(compound="left")
        self.Label3a.configure(font="-family {Purisa} -size 16")
        self.Label3a.configure(text="""E-MAIL""")

        def tbsredirect1():
            self.driverLoginFrame.destroy()

        self.Back = Button(self.driverLoginFrame)
        self.Back.place(relx=0.900, rely=0.880, height=33, width=85)
        self.Back.configure(activebackground="beige")
        self.Back.configure(background="#FFFFFF")
        self.Back.configure(borderwidth="2")
        self.Back.configure(compound="left")
        self.Back.configure(text="""BACK""", command=tbsredirect1)

        self.Label3_1a = Label(self.driverLoginFrame)
        self.Label3_1a.place(relx=0.6, rely=0.425, height=51, width=138)
        self.Label3_1a.configure(activebackground="#f9f9f9")
        self.Label3_1a.configure(anchor="w")
        self.Label3_1a.configure(background="#d5f4e6")
        self.Label3_1a.configure(compound="left")
        self.Label3_1a.configure(font="-family {Purisa} -size 16")
        self.Label3_1a.configure(text="""PASSWORD""")

        def del_char(event):
            self.Entry1a.delete(0, END)

        self.Entry1a = Entry(self.driverLoginFrame)
        self.Entry1a.place(relx=0.71, rely=0.314, height=43, relwidth=0.202)
        self.Entry1a.configure(background="white")
        self.Entry1a.configure(font="TkFixedFont")
        self.Entry1a.insert(0, "Enter the E-Mail")
        self.Entry1a.bind("<FocusIn>", del_char)

        def del_passw(event):
            self.Entry1_1b.delete(0, END)
            if self.Entry1_1b.get() == "Enter the password":

                self.Entry1_1b.configure(show="*")

        def showpassword(event):
            if self.Entry1_1b.get() != "Enter the Password":
                if self.ayoo11.get() == 1:
                    self.Entry1_1b.config(show="*")
                else:
                    self.Entry1_1b.config(show="")

        self.ayoo11 = IntVar()
        self.showButton = Checkbutton(
            self.driverLoginFrame,
            variable=self.ayoo11,
            onvalue=1,
            offvalue=0,
            background="#d5f4e6",
            text="""Show Password""",
        )
        self.showButton.place(relx=0.71, rely=0.49, relheight=0.042, relwidth=0.100)
        self.showButton.bind("<Button-1>", showpassword)

        self.Entry1_1b = Entry(self.driverLoginFrame)
        self.Entry1_1b.place(relx=0.71, rely=0.425, height=43, relwidth=0.202)
        self.Entry1_1b.configure(background="white")
        self.Entry1_1b.configure(font="TkFixedFont")
        self.Entry1_1b.configure(selectbackground="#c4c4c4")
        self.Entry1_1b.insert(0, "Enter the Password")
        self.Entry1_1b.bind("<FocusIn>", del_passw)

        self.Button1login = Button(self.driverLoginFrame)
        self.Button1login.place(relx=0.71, rely=0.649, height=43, relwidth=0.202)
        self.Button1login.configure(activebackground="beige")
        self.Button1login.configure(background="#d5f4e6")
        self.Button1login.configure(borderwidth="2")
        self.Button1login.configure(compound="left")
        self.Button1login.configure(font="-family {DejaVu Sans} -size 18")
        self.Button1login.configure(text="""LOGIN""", command=self.login_btn1)

        self.Label2_21 = Label(self.driverLoginFrame)
        self.Label2_21.place(relx=0.70, rely=0.735, height=32, width=229)
        self.Label2_21.configure(activebackground="#f9f9f9")
        self.Label2_21.configure(anchor="w")
        self.Label2_21.configure(background="#d5f4e6")
        self.Label2_21.configure(compound="left")
        self.Label2_21.configure(cursor="fleur")
        self.Label2_21.configure(font="-family {DejaVu Sans} -size 14")
        self.Label2_21.configure(text="""Dont Have Account ...?""")

        self.Button2s = Button(self.driverLoginFrame)
        self.Button2s.place(relx=0.86, rely=0.732, height=33, width=71)
        self.Button2s.configure(activebackground="beige")
        self.Button2s.configure(background="#d5f4e6")
        self.Button2s.configure(borderwidth="2")
        self.Button2s.configure(compound="left")
        self.Button2s.configure(
            text="""SIGN UP""", command=lambda: driredirect(self.root)
        )

        def driredirect(root):
            driverRegister.driverRegister(root)

        self.driverLoginFrame.mainloop()

    def login_btn1(self):

        user = driverRegisterModel()

        user.setEmail(self.Entry1a.get())
        user.setPassword(self.Entry1_1b.get())
        self.Entry1a.delete("0", "end")
        self.Entry1_1b.delete("0", "end")

        driversignUpreg = driverRegistercontroll()
        driversignUpreg.driverlogin(user, self.root)
