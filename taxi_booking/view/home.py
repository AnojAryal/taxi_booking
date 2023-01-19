from tkinter import *
from view import booking, aboutUs, profile, viewBooking, login
from tkinter import messagebox


class home:
    def __init__(self, root, record):
        self.root = root
        self.record = record
        # self.homeFrame = None
        self.homePage()

    def homePage(self):
        # self.root = Tk()
        # self.root.title("Main Frame")
        self.homeFrame = Frame(self.root)
        self.homeFrame.place(relx=0, rely=0, height=768, width=1366)

        for data in self.record:
            Firstname = data[1]

        # self.homeFrame = Toplevel(self.root)
        # self.homeFrame.title("Home Page")

        # # self.homeFrame.geometry("1366x725+-13+-11")
        # self.homeFrame.geometry("1366x725+-13+-11")
        # self.homeFrame.minsize(1, 1)
        # self.homeFrame.maxsize(1351, 738)
        # self.homeFrame.resizable(1,  1)
        # self.homeFrame.title("Home")

        self.Label1_2 = Label(self.homeFrame)
        self.Label1_2.place(relx=0.088, rely=0.386, height=221, width=250)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(anchor="w")
        self.Label1_2.configure(compound="left")
        self.photo = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/heee_1_249x241.png"
        )
        self.Label1_2.configure(image=self.photo)
        # self.Label1_2.configure(image=self.background)

        self.Label1_2_1 = Label(self.homeFrame)
        self.Label1_2_1.place(relx=0.542, rely=0.359, height=371, width=506)
        self.Label1_2_1.configure(activebackground="#f9f9f9")
        self.Label1_2_1.configure(anchor="w")
        self.Label1_2_1.configure(compound="left")
        self.photo1 = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/driver.png"
        )
        self.Label1_2_1.configure(image=self.photo1)
        # self.Label1_2_1.configure(image=self.background)

        self.Label1_2_1_1 = Label(self.homeFrame)
        self.Label1_2_1_1.place(relx=0.307, rely=0.372, height=240, width=260)
        self.Label1_2_1_1.configure(activebackground="#f9f9f9")
        self.Label1_2_1_1.configure(anchor="w")
        self.Label1_2_1_1.configure(compound="left")
        self.photo2 = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/77.png"
        )
        self.Label1_2_1_1.configure(image=self.photo2)
        # self.Label1_2_1_1.configure(image=self.background)

        self.Label1 = Label(self.homeFrame)
        self.Label1.place(relx=0.059, rely=0.069, height=101, width=108)
        self.Label1.configure(anchor="w")
        self.Label1.configure(compound="left")
        self.Label1.configure(cursor="fleur")
        self.photo3 = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/profile1.png"
        )
        self.Label1.configure(image=self.photo3)
        # self.Label1.configure(image=self.background)

        self.Label1_1 = Label(self.homeFrame)
        self.Label1_1.place(relx=0.417, rely=0.179, height=42, width=179)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor="w")
        self.Label1_1.configure(compound="left")
        self.Label1_1.configure(
            font="-family {Droid Sans Fallback} -size 12 -weight bold"
        )
        self.Label1_1.configure(text="""TRAVEL WITH EASE""")

        self.Label2 = Label(self.homeFrame)
        self.Label2.place(relx=0.425, rely=0.041, height=101, width=166)
        self.Label2.configure(anchor="w")
        self.Label2.configure(compound="left")
        self.Label2.configure(font="-family {Karumbi} -size 32 -weight bold")
        self.Label2.configure(text="""RIDE X""")

        def redirect():
            booking.booking(self.root, self.record)

        self.Button1 = Button(self.homeFrame)
        self.Button1.place(relx=0.736, rely=0.083, height=53, width=143)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(background="#d5f4e6")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound="left")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(font="-family {DejaVu Sans} -size 14")
        self.Button1.configure(text="""BOOK NOW""", command=redirect)

        # def redirectHome(backup):
        #     backup.withdraw()
        #     booking.booking(backup)

        self.Button1_1 = Button(self.homeFrame)
        self.Button1_1.place(relx=0.052, rely=0.226, height=53, width=123)
        self.Button1_1.configure(activebackground="beige")
        self.Button1_1.configure(background="#d5f4e6")
        self.Button1_1.configure(borderwidth="2")
        self.Button1_1.configure(compound="left")
        self.Button1_1.configure(font="-family {DejaVu Sans} -size 14")
        self.Button1_1.configure(text="""Profile""", command=self.redirectProfile)

        # def redirectProfile(backup):
        #     backup.withdraw()
        #     profile.profile(backup)

        self.Label1_1_1 = Label(self.homeFrame)
        self.Label1_1_1.place(relx=0.124, rely=0.097, height=42, width=290)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(anchor="w")
        self.Label1_1_1.configure(compound="left")
        self.Label1_1_1.configure(cursor="fleur")
        self.Label1_1_1.configure(
            font="-family {Droid Sans Fallback} -size 16 -weight bold"
        )
        self.Label1_1_1.configure(text="""---- Welcome """ + Firstname + """...!""")

        self.Button1_2 = Button(self.homeFrame)
        self.Button1_2.place(relx=0.608, rely=0.083, height=53, width=173)
        self.Button1_2.configure(activebackground="beige")
        self.Button1_2.configure(background="#d5f4e6")
        self.Button1_2.configure(borderwidth="2")
        self.Button1_2.configure(compound="left")
        self.Button1_2.configure(cursor="fleur")
        self.Button1_2.configure(font="-family {DejaVu Sans} -size 14")
        self.Button1_2.configure(
            text="""VIEW BOOKINGS""", command=self.redirectviewBooking
        )

        self.Label4 = Label(self.homeFrame)
        self.Label4.place(relx=0.088, rely=0.727, height=21, width=559)
        self.Label4.configure(anchor="w")
        self.Label4.configure(compound="left")
        self.Label4.configure(font="-family {DejaVu Sans} -size 11")
        self.Label4.configure(
            text="""You are welcome to the official home page of RIDE X taxi booking system"""
        )

        self.Label4_1 = Label(self.homeFrame)
        self.Label4_1.place(relx=0.088, rely=0.763, height=21, width=611)
        self.Label4_1.configure(activebackground="#f9f9f9")
        self.Label4_1.configure(anchor="w")
        self.Label4_1.configure(compound="left")
        self.Label4_1.configure(font="-family {DejaVu Sans} -size 10")
        self.Label4_1.configure(
            text="""We provide the best taxi booking system over all other apps.You can now book your trip"""
        )

        self.Button1_3 = Button(self.homeFrame)
        self.Button1_3.place(relx=0.842, rely=0.083, height=53, width=143)
        self.Button1_3.configure(activebackground="beige")
        self.Button1_3.configure(background="#d5f4e6")
        self.Button1_3.configure(borderwidth="2")
        self.Button1_3.configure(compound="left")
        self.Button1_3.configure(font="-family {DejaVu Sans} -size 14")
        self.Button1_3.configure(
            text="""About Us""", command=lambda: self.redirectAboutUs(self.root)
        )

        self.Button_logout = Button(self.homeFrame)
        self.Button_logout.place(relx=0.850, rely=0.850, height=45, width=110)
        self.Button_logout.configure(activebackground="beige")
        self.Button_logout.configure(background="#d5f4e6")
        # self.login.login()re(background="#d5f4e6")
        self.Button_logout.configure(borderwidth="2")
        self.Button_logout.configure(compound="left")
        self.Button_logout.configure(font="-family {DejaVu Sans} -size 14")
        self.Button_logout.configure(text="""Logout""", command=self.logout12)

        self.Label4_1_1 = Label(self.homeFrame)
        self.Label4_1_1.place(relx=0.088, rely=0.8, height=21, width=609)
        self.Label4_1_1.configure(activebackground="#f9f9f9")
        self.Label4_1_1.configure(anchor="w")
        self.Label4_1_1.configure(compound="left")
        self.Label4_1_1.configure(
            text="""Travel with ease!! Travel with comfort. we provide safe and enjoyful trip to our customers"""
        )

    def redirectAboutUs(self, root):
        aboutUs.aboutUs(root)

    def redirectviewBooking(self):
        viewBooking.viewBooking(self.root, self.record)

    def redirectProfile(self):
        profile.profile(self.root, self.record)

        self.homeFrame.mainloop()

    def logout12(self):
        response = messagebox.askquestion(
            title="Log Out !",
            message="Are You Sure?",
            icon="warning",
        )

        if response == "yes":
            self.homeFrame.destroy()
