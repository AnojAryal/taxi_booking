from tkinter import *
from view import home
from tkcalendar import DateEntry
from models.bookingModel import bookingModel
from controllers.bookingControll import bookingControl


class booking:
    def __init__(self, root, record):
        self.root = root
        self.record = record
        self.bookingPage()

    def bookingPage(self):

        self.bookingFrame = Frame(self.root)
        self.bookingFrame.place(relx=0, rely=0, height=768, width=1366)

        # self.bookingFrame = Toplevel()
        # self.bookingFrame.geometry("1366x724+-13+-11")
        # self.bookingFrame.minsize(1, 1)
        # self.bookingFrame.maxsize(1351, 738)
        # self.bookingFrame.title("Booking")
        self.bookingFrame.configure(background="#FFFFFF")
        # self.bookingFrame.configure(highlightcolor="black")

        self.Label1 = Label(self.bookingFrame)
        self.Label1.place(relx=0.3, rely=0.014, height=82, width=579)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor="w")
        self.Label1.configure(background="#FFFFFF")
        self.Label1.configure(compound="left")
        self.Label1.configure(font="-family {Purisa} -size 48 -weight bold")
        self.Label1.configure(foreground="#800080")
        self.Label1.configure(text="""BoOk NoW...!!!""")

        self.Label2 = Label(self.bookingFrame)
        self.Label2.place(relx=0.556, rely=0.17, height=52, width=260)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor="w")
        self.Label2.configure(background="#ff6347")
        self.Label2.configure(compound="left")
        self.Label2.configure(font="-family {Purisa} -size 14 -weight bold")
        self.Label2.configure(text="""Full Name""")

        self.Label3 = Label(self.bookingFrame)
        self.Label3.place(relx=0.783, rely=0.169, height=61, width=255)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor="w")
        self.Label3.configure(background="#ff6347")
        self.Label3.configure(compound="left")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(font="-family {Purisa} -size 14 -weight bold")
        self.Label3.configure(text="""E-Mail""")

        self.Label4 = Label(self.bookingFrame)
        self.Label4.place(relx=0.556, rely=0.326, height=52, width=260)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor="w")
        self.Label4.configure(background="#ff6347")
        self.Label4.configure(compound="left")
        self.Label4.configure(font="-family {Purisa} -size 14 -weight bold")
        self.Label4.configure(text="""Contact No""")

        self.Label5 = Label(self.bookingFrame)
        self.Label5.place(relx=0.783, rely=0.322, height=52, width=255)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor="w")
        self.Label5.configure(background="#ff6347")
        self.Label5.configure(compound="left")
        self.Label5.configure(font="-family {Purisa} -size 14 -weight bold")
        self.Label5.configure(text="""Pickup Date""")

        self.Label6 = Label(self.bookingFrame)
        self.Label6.place(relx=0.556, rely=0.472, height=52, width=260)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor="w")
        self.Label6.configure(background="#ff6347")
        self.Label6.configure(compound="left")
        self.Label6.configure(font="-family {Purisa} -size 14 -weight bold")
        self.Label6.configure(text="""Pickup Time""")

        self.Label7 = Label(self.bookingFrame)
        self.Label7.place(relx=0.783, rely=0.461, height=52, width=258)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor="w")
        self.Label7.configure(background="#ff6347")
        self.Label7.configure(compound="left")
        self.Label7.configure(font="-family {Purisa} -size 14 -weight bold")
        self.Label7.configure(text="""Pickup Location""")

        self.Label8 = Label(self.bookingFrame)
        self.Label8.place(relx=0.556, rely=0.624, height=52, width=260)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(anchor="w")
        self.Label8.configure(background="#ff6347")
        self.Label8.configure(compound="left")
        self.Label8.configure(font="-family {Purisa} -size 14 -weight bold")
        self.Label8.configure(text="""Drop Location""")

        self.Entry1 = Entry(self.bookingFrame)
        self.Entry1.place(relx=0.556, rely=0.221, height=43, relwidth=0.173)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")

        self.Entry2 = Entry(self.bookingFrame)
        self.Entry2.place(relx=0.783, rely=0.221, height=43, relwidth=0.173)
        self.Entry2.configure(background="white")
        self.Entry2.configure(cursor="fleur")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")

        self.Entry3 = Entry(self.bookingFrame)
        self.Entry3.place(relx=0.556, rely=0.372, height=43, relwidth=0.173)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")

        self.Entry4 = Entry(self.bookingFrame)
        self.Entry4.place(relx=0.783, rely=0.372, height=43, relwidth=0.173)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(selectbackground="#c4c4c4")

        self.Entry5 = Entry(self.bookingFrame)
        self.Entry5.place(relx=0.556, rely=0.523, height=43, relwidth=0.173)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(selectbackground="#c4c4c4")

        self.Entry6 = Entry(self.bookingFrame)
        self.Entry6.place(relx=0.783, rely=0.51, height=43, relwidth=0.173)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(selectbackground="#c4c4c4")

        self.Entry7 = Entry(self.bookingFrame)
        self.Entry7.place(relx=0.556, rely=0.677, height=43, relwidth=0.173)
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(selectbackground="#c4c4c4")

        self.Button1 = Button(self.bookingFrame)
        self.Button1.place(relx=0.571, rely=0.843, height=33, width=66)
        self.Button1.configure(background="#d5f4e6")
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound="left")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(text="""BACK""", command=self.redirect_home)

        self.Button2 = Button(self.bookingFrame)
        self.Button2.place(relx=0.849, rely=0.843, height=33, width=143)
        self.Button2.configure(background="#d5f4e6")
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(compound="left")
        self.Button2.configure(text="""REQUEST BOOKING""", command=self.booking)

        self.Label9 = Label(self.bookingFrame)
        self.Label9.place(relx=0.0, rely=0.207, height=591, width=652)
        self.Label9.configure(anchor="w")
        self.Label9.configure(background="#FFFFFF")
        self.Label9.configure(compound="left")
        self.photo = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/bookingback.png"
        )
        self.Label9.configure(image=self.photo)

    def redirect_home(self):
        self.bookingFrame.destroy()

    def booking(self):
        for data in self.record:
            userID = (data[0],)

        user = bookingModel()

        user.setFullname(self.Entry1.get())
        user.setEmail(self.Entry2.get())
        user.setContact(self.Entry3.get())
        user.setPickupDate(self.Entry4.get())
        user.setPickupTime(self.Entry5.get())
        user.setPickupLocation(self.Entry6.get())
        user.setDropLocation(self.Entry7.get())

        letbook = user.booking_validator()

        if letbook:
            bookingreg = bookingControl()
            bookingreg.booking_controll(user, userID)

        self.bookingFrame.mainloop()
