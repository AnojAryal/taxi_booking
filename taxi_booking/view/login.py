from tkinter import *
from view import signUp
from tkinter import messagebox
from models.signUpModel import signUpModel
from controllers.signUpControll import UserControl


class Login:
    def __init__(self, root):
        self.root = root
        # self.root.title("Taxi Booking System")
        # self.root.resizable(0, 0)
        # self.root.configure(background="#000000")
        # self.root.geometry("1366x768")

        self.loginPage()

    def loginPage(self):
        self.loginFrame = Frame(self.root, background="#d5f4e6")
        self.loginFrame.place(relx=0, rely=0, height=768, width=1366)

        self.Label1 = Label(self.loginFrame)
        self.Label1.place(relx=0.0, rely=-0.055,height=781, width=688)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor="w")
        self.Label1.configure(background="#fefbd8")
        self.Label1.configure(compound="left")
        self.background = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/background.png"
        )
        self.Label1.configure(image=self.background)

        self.Label_top = Label(self.loginFrame)
        self.Label_top.place(relx=0.703, rely=0.055, height=53, width=137)
        self.Label_top.configure(activebackground="#f9f9f9")
        self.Label_top.configure(anchor="w")
        self.Label_top.configure(background="#d5f4e6")
        self.Label_top.configure(compound="left")
        self.Label_top.configure(
            font="-family {MathJax_Caligraphic} -size 24 -weight bold"
        )
        self.Label_top.configure(text="""LOGIN""")

        def del_char(event):
            self.entry_email.delete(0, END)

        self.entry_email = Entry(self.loginFrame)
        self.entry_email.place(relx=0.637, rely=0.302, height=43, relwidth=0.231)
        self.entry_email.configure(background="white")
        self.entry_email.configure(font="TkFixedFont")
        self.entry_email.configure(selectbackground="#c4c4c4")
        self.entry_email.insert(0, "Enter the e-mail")
        self.entry_email.bind("<FocusIn>", del_char)

        def showpassword(event):
            if self.Entry_pass.get() != "Enter the Password":
                if self.ayo.get() == 1:
                    self.Entry_pass.config(show="*")
                else:
                    self.Entry_pass.config(show="")

        self.ayo = IntVar()
        self.showButton = Checkbutton(
            self.loginFrame,
            variable=self.ayo,
            onvalue=1,
            offvalue=0,
            background="#d5f4e6",
            text="""Show Password""",
        )
        self.showButton.place(relx=0.637, rely=0.52, relheight=0.042, relwidth=0.100)
        self.showButton.bind("<Button-1>", showpassword)

        self.Label_email = Label(self.loginFrame)
        self.Label_email.place(relx=0.637, rely=0.249, height=32, width=88)
        self.Label_email.configure(activebackground="#f9f9f9")
        self.Label_email.configure(anchor="w")
        self.Label_email.configure(background="#d5f4e6")
        self.Label_email.configure(compound="left")
        self.Label_email.configure(font="-family {DejaVu Sans} -size 18")
        self.Label_email.configure(text="""E-Mail""")

        self.Label_password = Label(self.loginFrame)
        self.Label_password.place(relx=0.637, rely=0.398, height=42, width=137)
        self.Label_password.configure(activebackground="#f9f9f9")
        self.Label_password.configure(anchor="w")
        self.Label_password.configure(background="#d5f4e6")
        self.Label_password.configure(compound="left")
        self.Label_password.configure(font="-family {DejaVu Sans} -size 18")
        self.Label_password.configure(text="""Password""")

        def del_pass(event):
            if self.Entry_pass.get() == "Enter the password":

                self.Entry_pass.delete(0, END)
                self.Entry_pass.configure(show="*")

        self.Entry_pass = Entry(self.loginFrame)
        self.Entry_pass.place(relx=0.637, rely=0.454, height=43, relwidth=0.231)
        self.Entry_pass.configure(background="white")
        self.Entry_pass.configure(font="TkFixedFont")
        self.Entry_pass.configure(selectbackground="#c4c4c4")
        self.Entry_pass.insert(0, "Enter the password")
        self.Entry_pass.bind("<FocusIn>", del_pass)

        self.Button1 = Button(self.loginFrame)
        self.Button1.place(relx=0.637, rely=0.649, height=43, width=321)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(background="#d5f4e6")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound="left")
        self.Button1.configure(font="-family {DejaVu Sans} -size 18")
        self.Button1.configure(text="""LOGIN""", command=self.login_btn)

        self.Label2_2 = Label(self.loginFrame)
        self.Label2_2.place(relx=0.644, rely=0.735, height=32, width=229)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(anchor="w")
        self.Label2_2.configure(background="#d5f4e6")
        self.Label2_2.configure(compound="left")
        self.Label2_2.configure(cursor="fleur")
        self.Label2_2.configure(font="-family {DejaVu Sans} -size 14")
        self.Label2_2.configure(text="""Dont Have Account ...?""")

        def tbsredirect():
            self.loginFrame.destroy()

        self.Back = Button(self.loginFrame)
        self.Back.place(relx=0.900, rely=0.880, height=33, width=85)
        self.Back.configure(activebackground="beige")
        self.Back.configure(background="#FFFFFF")
        self.Back.configure(borderwidth="2")
        self.Back.configure(compound="left")
        self.Back.configure(text="""BACK""", command=tbsredirect)

        self.welcome = Label(self.loginFrame)
        self.welcome.place(relx=0.63, rely=0.152, height=32, width=330)
        self.welcome.configure(activebackground="#f9f9f9")
        self.welcome.configure(anchor="w")
        self.welcome.configure(background="#d5f4e6")
        self.welcome.configure(compound="left")
        self.welcome.configure(font="-family {DejaVu Sans} -size 12")
        self.welcome.configure(text="""Welcome! Login to book first ride with us""")

        self.Button2 = Button(self.loginFrame)
        self.Button2.place(relx=0.813, rely=0.732, height=33, width=73)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(background="#d5f4e6")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(compound="left")
        self.Button2.configure(text="""SIGN UP """, command=lambda: redirect(self.root))

        def redirect(root):
            signUp.SignUp(root)

        self.loginFrame.mainloop()

    def login_btn(self):

        user = signUpModel()

        user.setEmail(self.entry_email.get())
        user.setPassword(self.Entry_pass.get())
        self.entry_email.delete("0", "end")
        self.Entry_pass.delete("0", "end")

        signUpreg = UserControl()
        signUpreg.login(user, self.root)
