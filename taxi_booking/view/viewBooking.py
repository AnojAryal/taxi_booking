from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers.bookingControll import bookingControl


class viewBooking:
    def __init__(self, root, record):

        self.root = root
        self.tablerecords = record
        self.viewBookingPage()

    def viewBookingPage(self):

        self.viewBookingFrame = Frame(self.root)
        self.viewBookingFrame.place(relx=0, rely=0, height=768, width=1366)

        self.Label2 = Label(self.viewBookingFrame)
        self.Label2.place(relx=0.073, rely=0.240, height=65, width=278)
        self.Label2.configure(anchor="w")
        self.Label2.configure(compound="left")
        self.Label2.configure(font="-family {DejaVu Sans} -size 22 -weight bold")
        self.Label2.configure(text="""Booking Details""")

        self.button_edit = Button(self.viewBookingFrame)
        self.button_edit.place(relx=0.400, rely=0.750, height=33, width=133)
        self.button_edit.configure(activebackground="beige")
        self.button_edit.configure(background="#00FFFF")
        self.button_edit.configure(borderwidth="2")
        self.button_edit.configure(compound="left")
        self.button_edit.configure(text="""Edit Bookings""")

        self.Button_cancell = Button(self.viewBookingFrame)
        self.Button_cancell.place(relx=0.500, rely=0.750, height=33, width=143)
        self.Button_cancell.configure(activebackground="beige")
        self.Button_cancell.configure(background="#00FFFF")
        self.Button_cancell.configure(borderwidth="2")
        self.Button_cancell.configure(compound="left")
        self.Button_cancell.configure(text="""Cancel Booking""",command=self.cancelbooking)

        self.Label_logo = Label(self.viewBookingFrame)
        self.Label_logo.place(relx=0.417, rely=0.028, height=83, width=179)
        self.Label_logo.configure(activebackground="#f9f9f9")
        self.Label_logo.configure(anchor="w")
        self.Label_logo.configure(compound="left")
        self.Label_logo.configure(font="-family {Purisa} -size 24 -weight bold")
        self.Label_logo.configure(text="""RIDE X""")

        self.Button1_back = Button(self.viewBookingFrame)
        self.Button1_back.place(relx=0.908, rely=0.860, height=35, width=93)
        self.Button1_back.configure(activebackground="beige")
        self.Button1_back.configure(background="#00FFFF")
        self.Button1_back.configure(borderwidth="2")
        self.Button1_back.configure(compound="left")
        self.Button1_back.configure(text="""BACK""", command=self.redirect11)

        self.bookingTable()

        self.viewBookingFrame.mainloop()

    def redirect11(self):
        self.viewBookingFrame.destroy()
    
    def cancelbooking(self):
        selectedbooking = self.user_booking_table.focus()
        selected_booking_row = self.user_booking_table.item(
            selectedbooking,
            "values",
        )
        selected_booking_Id = selected_booking_row[0]
        print(selected_booking_row[0])
        cencel_booking_control = bookingControl()
        cencel_booking_control.Cancelbooking(selected_booking_Id)
        messagebox.showinfo(
            "SUCCESS", "Booking request of "+" " + selected_booking_Id  + " has been cancelled"
            )


  
    def bookingTable(self):

        self.booking_table = Frame(self.viewBookingFrame, bg="#FFFFFF")
        self.booking_table.place(relx=0.073, rely=0.331, height=260, width=1164)
        table_scroll_bar = Scrollbar(self.booking_table)
        table_scroll_bar.place(relx=0.980, rely=0.110, height=210, width=15)
        self.user_booking_table = ttk.Treeview(
            self.booking_table,
            yscrollcommand=table_scroll_bar.set,
            selectmode="extended",
        )
        self.user_booking_table.place(
            relx=0.020,
            rely=0.110,
            height=210,
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
        self.user_booking_table.column("BookingID", width=70, anchor=W)
        self.user_booking_table.column("Fullname", width=70, anchor=W)
        self.user_booking_table.column("E-Mail", width=70, anchor=W)
        self.user_booking_table.column("Contact", width=40, anchor=W)
        self.user_booking_table.column("Pickupdate", width=40, anchor=W)
        self.user_booking_table.column("Pickuptime", width=40, anchor=W)
        self.user_booking_table.column("Pickuplocation", width=120, anchor=W)
        self.user_booking_table.column("Droplocation", width=120, anchor=W)
        self.user_booking_table.column("Status", width=60, anchor=W)

        self.user_booking_table.heading("#0", text="", anchor=W)
        self.user_booking_table.heading("BookingID", text="BookingID", anchor=W)
        self.user_booking_table.heading("Fullname", text="Fullname", anchor=W)
        self.user_booking_table.heading("E-Mail", text="E-Mail", anchor=W)
        self.user_booking_table.heading("Contact", text="Contact", anchor=W)
        self.user_booking_table.heading("Pickupdate", text="Pickupdate", anchor=W)
        self.user_booking_table.heading("Pickuptime", text="Pickuptime", anchor=W)
        self.user_booking_table.heading("Pickuplocation", text="Pickuplocation", anchor=W)
        self.user_booking_table.heading("Droplocation", text="Droplocation", anchor=W)
        self.user_booking_table.heading("Status", text="Status", anchor=W)

        self.booking = bookingControl()
        for info in self.tablerecords:
            userID = info[0]
            records = self.booking.bookingDetails(userID)
            # print(records)
            for data in records:
                self.user_booking_table.insert(
                    "",
                    index="end",
                    values=(
                        data[0],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                        data[8],
                        data[9],
                    ),

                )
          