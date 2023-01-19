from tkinter import *
from tkinter import messagebox
from view import login
from models.signUpModel import signUpModel
from controllers.signUpControll import UserControl


class SignUp:
    def __init__(self, root):
        self.root = root

        self.signupPage()

    def signupPage(self):

        self.signUpFrame = Frame(self.root)
        self.signUpFrame.place(relx=0, rely=0, height=768, width=1366)

        def redirect():
            self.signUpFrame.destroy()

        self.Back = Button(self.signUpFrame)
        self.Back.place(relx=0.644, rely=0.786, height=33, width=93)
        self.Back.configure(activebackground="beige")
        self.Back.configure(background="#FFFFFF")
        self.Back.configure(borderwidth="2")
        self.Back.configure(compound="left")
        self.Back.configure(cursor="fleur")
        self.Back.configure(text="""BACK""", command=redirect)

        self.signup = Button(self.signUpFrame)
        self.signup.place(relx=0.842, rely=0.786, height=33, width=113)
        self.signup.configure(activebackground="beige")
        self.signup.configure(background="#FFFFFF")
        self.signup.configure(borderwidth="2")
        self.signup.configure(compound="left")
        self.signup.configure(text="""SIGN UP""", command=self.signUp)

        self.Lbl_fname = Label(self.signUpFrame)
        self.Lbl_fname.place(relx=0.6, rely=0.203, height=45, width=228)
        self.Lbl_fname.configure(activebackground="#f9f9f9")
        self.Lbl_fname.configure(anchor="w")
        self.Lbl_fname.configure(background="#d5f4e6")
        self.Lbl_fname.configure(compound="left")
        self.Lbl_fname.configure(font="-family {DejaVu Sans} -size 14")
        self.Lbl_fname.configure(text="""First Name""")

        self.lab55 = Label(self.signUpFrame)
        self.lab55.place(relx=0.666, rely=0.083, height=35, width=330)
        self.lab55.configure(activebackground="#f9f9f9")
        self.lab55.configure(anchor="w")
        self.lab55.configure(compound="left")
        self.lab55.configure(cursor="fleur")
        self.lab55.configure(font="-family {Loma} -size 28 -weight bold")
        self.lab55.configure(text="""REGISTER HERE!""")

        self.First_name = Entry(self.signUpFrame)
        self.First_name.place(relx=0.6, rely=0.248, height=33, relwidth=0.151)
        self.First_name.configure(background="white")
        self.First_name.configure(font="TkFixedFont")
        self.First_name.configure(selectbackground="#c4c4c4")

        self.Lbl_lastname = Label(self.signUpFrame)
        self.Lbl_lastname.place(relx=0.798, rely=0.207, height=44, width=219)
        self.Lbl_lastname.configure(activebackground="#f9f9f9")
        self.Lbl_lastname.configure(anchor="w")
        self.Lbl_lastname.configure(background="#d5f4e6")
        self.Lbl_lastname.configure(compound="left")
        self.Lbl_lastname.configure(cursor="fleur")
        self.Lbl_lastname.configure(font="-family {DejaVu Sans} -size 14")
        self.Lbl_lastname.configure(text="""Last Name""")

        self.Lbl_contact = Label(self.signUpFrame)
        self.Lbl_contact.place(relx=0.6, rely=0.331, height=44, width=228)
        self.Lbl_contact.configure(activebackground="#f9f9f9")
        self.Lbl_contact.configure(anchor="w")
        self.Lbl_contact.configure(background="#d5f4e6")
        self.Lbl_contact.configure(compound="left")
        self.Lbl_contact.configure(cursor="fleur")
        self.Lbl_contact.configure(font="-family {DejaVu Sans} -size 14")
        self.Lbl_contact.configure(text="""Contact No""")

        self.Last_name = Entry(self.signUpFrame)
        self.Last_name.place(relx=0.798, rely=0.248, height=33, relwidth=0.151)
        self.Last_name.configure(background="white")
        self.Last_name.configure(font="TkFixedFont")
        self.Last_name.configure(selectbackground="#c4c4c4")

        self.Contact_no = Entry(self.signUpFrame)
        self.Contact_no.place(relx=0.6, rely=0.372, height=33, relwidth=0.151)
        self.Contact_no.configure(background="white")
        self.Contact_no.configure(font="TkFixedFont")
        self.Contact_no.configure(selectbackground="#c4c4c4")

        self.lbl_creditcard = Label(self.signUpFrame)
        self.lbl_creditcard.place(relx=0.6, rely=0.463, height=53, width=225)
        self.lbl_creditcard.configure(activebackground="#f9f9f9")
        self.lbl_creditcard.configure(anchor="w")
        self.lbl_creditcard.configure(background="#d5f4e6")
        self.lbl_creditcard.configure(compound="left")
        self.lbl_creditcard.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_creditcard.configure(text="""Credit Card No""")

        self.lbl_address = Label(self.signUpFrame)
        self.lbl_address.place(relx=0.798, rely=0.332, height=44, width=219)
        self.lbl_address.configure(activebackground="#f9f9f9")
        self.lbl_address.configure(anchor="w")
        self.lbl_address.configure(background="#d5f4e6")
        self.lbl_address.configure(compound="left")
        self.lbl_address.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_address.configure(text="""Address""")

        self.Address = Entry(self.signUpFrame)
        self.Address.place(relx=0.798, rely=0.372, height=33, relwidth=0.151)
        self.Address.configure(background="white")
        self.Address.configure(font="TkFixedFont")
        self.Address.configure(selectbackground="#c4c4c4")

        self.lbl_email = Label(self.signUpFrame)
        self.lbl_email.place(relx=0.798, rely=0.463, height=53, width=219)
        self.lbl_email.configure(activebackground="#f9f9f9")
        self.lbl_email.configure(anchor="w")
        self.lbl_email.configure(background="#d5f4e6")
        self.lbl_email.configure(compound="left")
        self.lbl_email.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_email.configure(text="""E-Mail""")

        self.lbl_pass = Label(self.signUpFrame)
        self.lbl_pass.place(relx=0.6, rely=0.599, height=53, width=228)
        self.lbl_pass.configure(activebackground="#f9f9f9")
        self.lbl_pass.configure(anchor="w")
        self.lbl_pass.configure(background="#d5f4e6")
        self.lbl_pass.configure(compound="left")
        self.lbl_pass.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_pass.configure(text="""Password""")

        self.Lbl_conpass = Label(self.signUpFrame)
        self.Lbl_conpass.place(relx=0.797, rely=0.606, height=45, width=226)
        self.Lbl_conpass.configure(activebackground="#f9f9f9")
        self.Lbl_conpass.configure(anchor="w")
        self.Lbl_conpass.configure(background="#d5f4e6")
        self.Lbl_conpass.configure(compound="left")
        self.Lbl_conpass.configure(font="-family {DejaVu Sans} -size 14")
        self.Lbl_conpass.configure(text="""Confirm Password""")

        self.creditcard = Entry(self.signUpFrame)
        self.creditcard.place(relx=0.6, rely=0.51, height=33, relwidth=0.151)
        self.creditcard.configure(background="white")
        self.creditcard.configure(font="TkFixedFont")
        self.creditcard.configure(selectbackground="#c4c4c4")

        self.email = Entry(self.signUpFrame)
        self.email.place(relx=0.798, rely=0.51, height=33, relwidth=0.151)
        self.email.configure(background="white")
        self.email.configure(font="TkFixedFont")
        self.email.configure(selectbackground="#c4c4c4")

        self.Password = Entry(self.signUpFrame)
        self.Password.place(relx=0.6, rely=0.648, height=33, relwidth=0.151)
        self.Password.configure(background="white")
        self.Password.configure(font="TkFixedFont")
        self.Password.configure(selectbackground="#c4c4c4")

        self.Confirm_password = Entry(self.signUpFrame)
        self.Confirm_password.place(relx=0.798, rely=0.648, height=33, relwidth=0.151)
        self.Confirm_password.configure(background="white")
        self.Confirm_password.configure(font="TkFixedFont")
        self.Confirm_password.configure(selectbackground="#c4c4c4")

        self.Label1 = Label(self.signUpFrame)
        self.Label1.place(relx=-0.015, rely=0.166, height=615, width=580)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor="w")
        self.Label1.configure(compound="left")
        self.Label1.configure(cursor="fleur")
        self.background = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/RegisterImage.png"
        )
        self.Label1.configure(image=self.background)

    def signUp(self):

        user = signUpModel()

        user.setFirstname(self.First_name.get())
        user.setLastname(self.Last_name.get())
        user.setContactNo(self.Contact_no.get())
        user.setCreditcardNo(self.creditcard.get())
        user.setAddress(self.Address.get())
        user.setEmail(self.email.get())
        user.setPassword(self.Password.get())
        user.setConfirmPassword(self.Confirm_password.get())

        letin = user.signUp_validator()

        if letin:
            signUpreg = UserControl()
            signUpreg.signup_controll(user)

        self.signUpFrame.mainloop()
