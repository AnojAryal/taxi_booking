from tkinter import *
from view import adminLogin, login, driverLogin


class Ridex_tbs:
    def __init__(self):
        # self.root = root
        self.root = Tk()
        self.root.title("Taxi Booking System")
        self.root.resizable(0, 0)
        self.root.configure(background="#000000")
        self.root.geometry("1366x768")
        # self.root.geometry("1266x748")
        # self.root.attributes("-fullscreen", True)

        self.tbsPage()

    def tbsPage(self):
        self.tbsFrame = Frame(self.root, background="#d5f4e6")
        self.tbsFrame.place(relx=0, rely=0, height=768, width=1366)

        self.Label1 = Label(self.tbsFrame)
        self.Label1.place(relx=0.0, rely=-0.055, height=781, width=688)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor="w")
        self.Label1.configure(background="#fefbd8")
        self.Label1.configure(compound="left")
        self.background = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/background.png"
        )
        self.Label1.configure(image=self.background)

        self.Button_customer = Button(self.tbsFrame)
        self.Button_customer.place(relx=0.703, rely=0.718, height=143, width=151)
        self.Button_customer.configure(activebackground="beige")
        self.Button_customer.configure(background="#d5f4e6")
        self.Button_customer.configure(borderwidth="2")
        self.Button_customer.configure(compound="left")
        self.Button_customer.configure(cursor="fleur")
        self.Button_customer.configure(font="-family {DejaVu Sans} -size 18")
        self.background1ed = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/customer.png",
        )
        self.Button_customer.configure(image=self.background1ed)
        self.Button_customer.configure(command=lambda: redirectlog(self.root))

        def redirectlog(root):
            login.Login(root)

        # self.Button_customer.configure(text="""Customer""")

        self.level3 = Label(self.tbsFrame)
        self.level3.place(relx=0.534, rely=0.29, height=62, width=612)
        self.level3.configure(activebackground="#f9f9f9")
        self.level3.configure(anchor="w")
        self.level3.configure(background="#d5f4e6")
        self.level3.configure(compound="left")
        self.level3.configure(cursor="fleur")
        self.level3.configure(font="-family {Karumbi} -size 34 -weight bold")
        self.level3.configure(text="""Ride x Taxi Booking System""")

        self.level1 = Label(self.tbsFrame)
        self.level1.place(relx=0.659, rely=0.041, height=63, width=633)
        self.level1.configure(activebackground="#f9f9f9")
        self.level1.configure(anchor="w")
        self.level1.configure(background="#d5f4e6")
        self.level1.configure(compound="left")
        self.level1.configure(cursor="fleur")
        self.level1.configure(font="-family {Karumbi} -size 38 -weight bold")
        self.level1.configure(text="""WELCOME""")

        self.level2 = Label(self.tbsFrame)
        self.level2.place(relx=0.717, rely=0.166, height=62, width=103)
        self.level2.configure(activebackground="#f9f9f9")
        self.level2.configure(anchor="w")
        self.level2.configure(background="#d5f4e6")
        self.level2.configure(compound="left")
        self.level2.configure(cursor="fleur")
        self.level2.configure(font="-family {Karumbi} -size 38 -weight bold")
        self.level2.configure(text="""TO""")

        self.Button_admin = Button(self.tbsFrame)
        self.Button_admin.place(relx=0.542, rely=0.718, height=143, width=161)
        self.Button_admin.configure(activebackground="beige")
        self.Button_admin.configure(background="#d5f4e6")
        self.Button_admin.configure(borderwidth="2")
        self.Button_admin.configure(compound="left")
        self.Button_admin.configure(cursor="fleur")
        self.Button_admin.configure(font="-family {DejaVu Sans} -size 18")
        self.background1e = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/admin.png"
        )
        self.Button_admin.configure(image=self.background1e)
        self.Button_admin.configure(command=lambda: redirectan(self.root))

        def redirectan(root):
            adminLogin.adminLogin(root)

        # self.Button_admin.configure(text="""ADMIN""")

        self.Button_driver = Button(self.tbsFrame)
        self.Button_driver.place(relx=0.857, rely=0.718, height=143, width=151)
        self.Button_driver.configure(activebackground="beige")
        self.Button_driver.configure(background="#d5f4e6")
        self.Button_driver.configure(borderwidth="2")
        self.Button_driver.configure(compound="left")
        self.Button_driver.configure(font="-family {DejaVu Sans} -size 18")
        self.background1ead = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/driverlogo.png"
        )
        self.Button_driver.configure(image=self.background1ead)
        self.Button_driver.configure(command=lambda: redirectdr(self.root))
        # self.Button_driver.configure(text="""Driver""")

        def redirectdr(root):
            driverLogin.driverLogin(root)

        self.selectlevel = Label(self.tbsFrame)
        self.selectlevel.place(relx=0.695, rely=0.58, height=63, width=204)
        self.selectlevel.configure(activebackground="#f9f9f9")
        self.selectlevel.configure(anchor="w")
        self.selectlevel.configure(background="#d5f4e6")
        self.selectlevel.configure(compound="left")
        self.selectlevel.configure(cursor="fleur")
        self.selectlevel.configure(font="-family {FreeSerif} -size 30 -weight bold")
        self.selectlevel.configure(text="""Login As:""")

        self.tbsFrame.mainloop()
