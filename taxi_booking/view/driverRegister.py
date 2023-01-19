from tkinter import *
from tkinter import ttk
from models.driverRegisterModel import driverRegisterModel
from controllers.driverRegisterControll import driverRegistercontroll


class driverRegister:
    def __init__(self, root):
        self.root = root

        self.driverRegisterPage()

    def driverRegisterPage(self):

        self.driverRegisterFrame = Frame(self.root)
        self.driverRegisterFrame.place(relx=0, rely=0, height=768, width=1366)

        def driverredirect():
            self.driverRegisterFrame.destroy()

        self.Back = Button(self.driverRegisterFrame)
        self.Back.place(relx=0.593, rely=0.840, height=33, width=93)
        self.Back.configure(activebackground="beige")
        self.Back.configure(background="#FFFFFF")
        self.Back.configure(borderwidth="2")
        self.Back.configure(compound="left")
        self.Back.configure(text="""BACK""", command=driverredirect)

        self.signup = Button(self.driverRegisterFrame)
        self.signup.place(relx=0.827, rely=0.840, height=33, width=113)
        self.signup.configure(activebackground="beige")
        self.signup.configure(background="#FFFFFF")
        self.signup.configure(borderwidth="2")
        self.signup.configure(compound="left")
        self.signup.configure(text="""SIGN UP""", command=self.Register)

        self.Lbl_fname = Label(self.driverRegisterFrame)
        self.Lbl_fname.place(relx=0.564, rely=0.166, height=45, width=230)
        self.Lbl_fname.configure(activebackground="#f9f9f9")
        self.Lbl_fname.configure(anchor="w")
        self.Lbl_fname.configure(background="#d5f4e6")
        self.Lbl_fname.configure(compound="left")
        self.Lbl_fname.configure(font="-family {DejaVu Sans} -size 14")
        self.Lbl_fname.configure(text="""First Name""")

        self.lab55 = Label(self.driverRegisterFrame)
        self.lab55.place(relx=0.637, rely=0.028, height=55, width=331)
        self.lab55.configure(activebackground="#f9f9f9")
        self.lab55.configure(anchor="w")
        self.lab55.configure(compound="left")
        self.lab55.configure(font="-family {Loma} -size 28 -weight bold")
        self.lab55.configure(text="""Driver Register...!!!""")

        self.First_name = Entry(self.driverRegisterFrame)
        self.First_name.place(relx=0.564, rely=0.207, height=33, relwidth=0.151)
        self.First_name.configure(background="white")
        self.First_name.configure(font="TkFixedFont")
        self.First_name.configure(selectbackground="#c4c4c4")

        self.Lbl_lastname = Label(self.driverRegisterFrame)
        self.Lbl_lastname.place(relx=0.777, rely=0.166, height=45, width=219)
        self.Lbl_lastname.configure(activebackground="#f9f9f9")
        self.Lbl_lastname.configure(anchor="w")
        self.Lbl_lastname.configure(background="#d5f4e6")
        self.Lbl_lastname.configure(compound="left")
        self.Lbl_lastname.configure(font="-family {DejaVu Sans} -size 14")
        self.Lbl_lastname.configure(text="""Last Name""")

        self.Lbl_contact = Label(self.driverRegisterFrame)
        self.Lbl_contact.place(relx=0.563, rely=0.276, height=44, width=230)
        self.Lbl_contact.configure(activebackground="#f9f9f9")
        self.Lbl_contact.configure(anchor="w")
        self.Lbl_contact.configure(background="#d5f4e6")
        self.Lbl_contact.configure(compound="left")
        self.Lbl_contact.configure(font="-family {DejaVu Sans} -size 14")
        self.Lbl_contact.configure(text="""Contact No""")

        self.Last_name = Entry(self.driverRegisterFrame)
        self.Last_name.place(relx=0.776, rely=0.207, height=33, relwidth=0.151)
        self.Last_name.configure(background="white")
        self.Last_name.configure(font="TkFixedFont")
        self.Last_name.configure(selectbackground="#c4c4c4")

        self.Contact_no = Entry(self.driverRegisterFrame)
        self.Contact_no.place(relx=0.562, rely=0.318, height=33, relwidth=0.151)
        self.Contact_no.configure(background="white")
        self.Contact_no.configure(font="TkFixedFont")
        self.Contact_no.configure(selectbackground="#c4c4c4")

        self.lbl_creditcard = Label(self.driverRegisterFrame)
        self.lbl_creditcard.place(relx=0.564, rely=0.391, height=53, width=226)
        self.lbl_creditcard.configure(activebackground="#f9f9f9")
        self.lbl_creditcard.configure(anchor="w")
        self.lbl_creditcard.configure(background="#d5f4e6")
        self.lbl_creditcard.configure(compound="left")
        self.lbl_creditcard.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_creditcard.configure(text="""E-Mail""")

        self.lbl_address = Label(self.driverRegisterFrame)
        self.lbl_address.place(relx=0.777, rely=0.278, height=44, width=219)
        self.lbl_address.configure(activebackground="#f9f9f9")
        self.lbl_address.configure(anchor="w")
        self.lbl_address.configure(background="#d5f4e6")
        self.lbl_address.configure(compound="left")
        self.lbl_address.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_address.configure(text="""Address""")

        self.Address = Entry(self.driverRegisterFrame)
        self.Address.place(relx=0.776, rely=0.318, height=33, relwidth=0.151)
        self.Address.configure(background="white")
        self.Address.configure(font="TkFixedFont")
        self.Address.configure(selectbackground="#c4c4c4")

        self.lbl_email = Label(self.driverRegisterFrame)
        self.lbl_email.place(relx=0.777, rely=0.394, height=52, width=219)
        self.lbl_email.configure(activebackground="#f9f9f9")
        self.lbl_email.configure(anchor="w")
        self.lbl_email.configure(background="#d5f4e6")
        self.lbl_email.configure(compound="left")
        self.lbl_email.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_email.configure(text="""Vehicle No""")

        self.lbl_pass = Label(self.driverRegisterFrame)
        self.lbl_pass.place(relx=0.562, rely=0.517, height=52, width=229)
        self.lbl_pass.configure(activebackground="#f9f9f9")
        self.lbl_pass.configure(anchor="w")
        self.lbl_pass.configure(background="#d5f4e6")
        self.lbl_pass.configure(compound="left")
        self.lbl_pass.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_pass.configure(text="""Vehicle Model""")

        self.Lbl_conpass = Label(self.driverRegisterFrame)
        self.Lbl_conpass.place(relx=0.777, rely=0.519, height=45, width=226)
        self.Lbl_conpass.configure(activebackground="#f9f9f9")
        self.Lbl_conpass.configure(anchor="w")
        self.Lbl_conpass.configure(background="#d5f4e6")
        self.Lbl_conpass.configure(compound="left")
        self.Lbl_conpass.configure(font="-family {DejaVu Sans} -size 14")
        self.Lbl_conpass.configure(text="""Liscence No""")

        self.Email_ent = Entry(self.driverRegisterFrame)
        self.Email_ent.place(relx=0.562, rely=0.441, height=33, relwidth=0.151)
        self.Email_ent.configure(background="white")
        self.Email_ent.configure(font="TkFixedFont")
        self.Email_ent.configure(selectbackground="#c4c4c4")

        self.vehicle_ent = Entry(self.driverRegisterFrame)
        self.vehicle_ent.place(relx=0.776, rely=0.442, height=33, relwidth=0.151)

        self.vehicle_ent.configure(background="white")
        self.vehicle_ent.configure(font="TkFixedFont")
        self.vehicle_ent.configure(selectbackground="#c4c4c4")

        self.vehiclemod_ent = Entry(self.driverRegisterFrame)
        self.vehiclemod_ent.place(relx=0.564, rely=0.58, height=33, relwidth=0.151)
        self.vehiclemod_ent.configure(background="white")
        self.vehiclemod_ent.configure(font="TkFixedFont")
        self.vehiclemod_ent.configure(selectbackground="#c4c4c4")

        self.lis_entry = Entry(self.driverRegisterFrame)
        self.lis_entry.place(relx=0.776, rely=0.566, height=33, relwidth=0.151)
        self.lis_entry.configure(background="white")
        self.lis_entry.configure(font="TkFixedFont")
        self.lis_entry.configure(selectbackground="#c4c4c4")

        self.Label1 = Label(self.driverRegisterFrame)
        self.Label1.place(relx=-0.007, rely=0.191, height=601, width=581)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor="w")
        self.Label1.configure(compound="left")
        self.background = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/RegisterImage.png"
        )
        self.Label1.configure(image=self.background)

        self.TSeparator1 = ttk.Separator(self.driverRegisterFrame)
        self.TSeparator1.place(relx=0.563, rely=0.648, relwidth=0.389)

        self.lbl_pass_1 = Label(self.driverRegisterFrame)
        self.lbl_pass_1.place(relx=0.56, rely=0.684, height=52, width=229)
        self.lbl_pass_1.configure(activebackground="#f9f9f9")
        self.lbl_pass_1.configure(anchor="w")
        self.lbl_pass_1.configure(background="#d5f4e6")
        self.lbl_pass_1.configure(compound="left")
        self.lbl_pass_1.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_pass_1.configure(text="""Password""")

        self.Password_ent = Entry(self.driverRegisterFrame)
        self.Password_ent.place(relx=0.559, rely=0.732, height=33, relwidth=0.151)
        self.Password_ent.configure(background="white")
        self.Password_ent.configure(font="TkFixedFont")
        self.Password_ent.configure(selectbackground="#c4c4c4")

        self.lbl_pass_1_1 = Label(self.driverRegisterFrame)
        self.lbl_pass_1_1.place(relx=0.777, rely=0.682, height=52, width=230)
        self.lbl_pass_1_1.configure(activebackground="#f9f9f9")
        self.lbl_pass_1_1.configure(anchor="w")
        self.lbl_pass_1_1.configure(background="#d5f4e6")
        self.lbl_pass_1_1.configure(compound="left")
        self.lbl_pass_1_1.configure(font="-family {DejaVu Sans} -size 14")
        self.lbl_pass_1_1.configure(text="""Confirm Password""")

        self.conpass_ent = Entry(self.driverRegisterFrame)
        self.conpass_ent.place(relx=0.776, rely=0.732, height=33, relwidth=0.151)

        self.conpass_ent.configure(background="white")
        self.conpass_ent.configure(font="TkFixedFont")
        self.conpass_ent.configure(selectbackground="#c4c4c4")

        self.driverRegisterFrame.mainloop()

    def Register(self):

        user = driverRegisterModel()

        user.setFirstname(self.First_name.get())
        user.setLastname(self.Last_name.get())
        user.setContactNo(self.Contact_no.get())
        user.setAddress(self.Address.get())
        user.setEmail(self.Email_ent.get())
        user.setVehicleno(self.vehicle_ent.get())
        user.setVehiclemod(self.vehiclemod_ent.get())
        user.setLiscenceno(self.lis_entry.get())
        user.setPassword(self.Password_ent.get())
        user.setConfirmPassword(self.conpass_ent.get())

        letmein = user.driverRegister_validator()

        if letmein:
            driverreg = driverRegistercontroll()
            driverreg.driverRegister_controll(user)
