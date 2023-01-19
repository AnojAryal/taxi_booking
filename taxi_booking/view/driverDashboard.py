from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from view import driverProfile


class driverDashboard:
    def __init__(self, root, record, driverRegistercontroll):

        self.root = root
        self.record = record
        self.tablerecords = record
        self.driverRegistercontroll = driverRegistercontroll
        self.driverDashboardPage()

    def driverDashboardPage(self):

        self.driverDashboardFrame = Frame(self.root)
        self.driverDashboardFrame.place(relx=0, rely=0, height=768, width=1366)

        # self.booking_table = Label(self.driverDashboardFrame)
        # self.booking_table.place(relx=0.073, rely=0.317, height=301, width=1164)
        # self.booking_table.configure(activebackground="#f9f9f9")
        # self.booking_table.configure(anchor="w")
        # self.booking_table.configure(background="#FFFFFF")
        # self.booking_table.configure(compound="left")
        # self.booking_table.configure(text="""Label""")

        self.Label2 = Label(self.driverDashboardFrame)
        self.Label2.place(relx=0.073, rely=0.234, height=53, width=285)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor="w")
        self.Label2.configure(compound="left")
        self.Label2.configure(font="-family {DejaVu Sans} -size 22 -weight bold")
        self.Label2.configure(text="""Your Trip History""")

        self.Label_logo = Label(self.driverDashboardFrame)
        self.Label_logo.place(relx=0.417, rely=0.014, height=83, width=179)
        self.Label_logo.configure(activebackground="#f9f9f9")
        self.Label_logo.configure(anchor="w")
        self.Label_logo.configure(compound="left")
        self.Label_logo.configure(font="-family {Purisa} -size 24 -weight bold")
        self.Label_logo.configure(text="""RIDE X""")

        self.Button1_back = Button(self.driverDashboardFrame)
        self.Button1_back.place(relx=0.886, rely=0.869, height=33, width=103)
        self.Button1_back.configure(activebackground="beige")
        self.Button1_back.configure(background="#00FFFF")
        self.Button1_back.configure(borderwidth="2")
        self.Button1_back.configure(compound="left")
        self.Button1_back.configure(text="""Logout""", command=self.logout1)

        self.Button1_profile = Button(self.driverDashboardFrame)
        self.Button1_profile.place(relx=0.056, rely=0.869, height=33, width=103)
        self.Button1_profile.configure(activebackground="beige")
        self.Button1_profile.configure(background="#00FFFF")
        self.Button1_profile.configure(borderwidth="2")
        self.Button1_profile.configure(compound="left")
        self.Button1_profile.configure(
            text="""PROFILE""", command=self.redirectdriverProfile
        )

        self.bookingTable()
        self.driverDashboardFrame.mainloop()

    def bookingTable(self):

        self.booking_table = Frame(self.driverDashboardFrame, bg="#FFFFFF")
        self.booking_table.place(relx=0.073, rely=0.317, height=301, width=1164)
        table_scroll_bar = Scrollbar(self.booking_table)
        table_scroll_bar.place(relx=0.980, rely=0.00, height=160, width=15)
        self.user_booking_table = ttk.Treeview(
            self.booking_table,
            yscrollcommand=table_scroll_bar.set,
            selectmode="extended",
        )
        self.user_booking_table.place(
            relx=0.020,
            rely=0.025,
            height=160,
            width=1090,
        )
        # table_scroll_bar.config(
        #     command=driver_booking_table.yview,
        # )

        self.user_booking_table["columns"] = (
            "BookingID",
            "Fullname",
            "E-Mail",
            "Contact",
            "Pickupdate",
            "Pickuptime",
            "Pickuplocation",
            "Droplocation",
            "Status",
        )

        self.user_booking_table.column("#0", width=0, stretch=NO)
        self.user_booking_table.column("BookingID", width=40, anchor=W)
        self.user_booking_table.column("Fullname", width=70, anchor=W)
        self.user_booking_table.column("E-Mail", width=120, anchor=W)
        self.user_booking_table.column("Contact", width=40, anchor=W)
        self.user_booking_table.column("Pickupdate", width=40, anchor=W)
        self.user_booking_table.column("Pickuptime", width=40, anchor=W)
        self.user_booking_table.column("Pickuplocation", width=70, anchor=W)
        self.user_booking_table.column("Droplocation", width=70, anchor=W)
        self.user_booking_table.column("Status", width=60, anchor=W)

        self.user_booking_table.heading("#0", text="", anchor=W)
        self.user_booking_table.heading("BookingID", text="BookingID", anchor=W)
        self.user_booking_table.heading("Fullname", text="Fullname", anchor=W)
        self.user_booking_table.heading("E-Mail", text="E-Mail", anchor=W)
        self.user_booking_table.heading("Contact", text="Contact", anchor=W)
        self.user_booking_table.heading("Pickupdate", text="Pickupdate", anchor=W)
        self.user_booking_table.heading("Pickuptime", text="Pickuptime", anchor=W)
        self.user_booking_table.heading(
            "Pickuplocation", text="Pickuplocation", anchor=W
        )
        self.user_booking_table.heading("Droplocation", text="Droplocation", anchor=W)
        self.user_booking_table.heading("Status", text="Status", anchor=W)

        for info in self.tablerecords:
            driverID = info[0]

        booking = self.driverRegistercontroll()

        records = booking.assignedDetails(driverID)

        for data in records:
            self.user_booking_table.insert(
                "",
                index="end",
                values=(
                    data[8],
                    data[10],
                    data[11],
                    data[12],
                    data[13],
                    data[14],
                    data[15],
                    data[16],
                    data[17],
                ),
            )

    def logout1(self):
        response = messagebox.askquestion(
            title="Log Out !",
            message="Are You Sure?",
            icon="warning",
        )

        if response == "yes":
            self.driverDashboardFrame.destroy()

    def redirectdriverProfile(self):
        driverProfile.driverProfile(self.root, self.record)
