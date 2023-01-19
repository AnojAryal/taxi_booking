from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class adminDashboard:
    def __init__(self, root, record, adminControl):

        self.root = root
        self.tablerecords = record
        self.admincontrol = adminControl

        self.adminDashboardPage()

    def adminDashboardPage(self):

        self.adminDashboardFrame = Frame(self.root)
        self.adminDashboardFrame.place(relx=0, rely=0, height=768, width=1366)

        # self.cust_table = Label(self.adminDashboardFrame)
        # self.cust_table.place(relx=0.081, rely=0.248, height=180, width=1162)
        # self.cust_table.configure(activebackground="#f9f9f9")
        # self.cust_table.configure(anchor="w")
        # self.cust_table.configure(background="#FFFFFF")
        # self.cust_table.configure(compound="left")
        # self.cust_table.configure(cursor="fleur")
        # self.cust_table.configure(text="""Label""")

        self.Labelcust = Label(self.adminDashboardFrame)
        self.Labelcust.place(relx=0.081, rely=0.179, height=43, width=307)
        self.Labelcust.configure(activebackground="#f9f9f9")
        self.Labelcust.configure(anchor="w")
        self.Labelcust.configure(compound="left")
        self.Labelcust.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.Labelcust.configure(text="""Customer Details""")

        self.Label_top = Label(self.adminDashboardFrame)
        self.Label_top.place(relx=0.344, rely=0.028, height=83, width=438)
        self.Label_top.configure(activebackground="#f9f9f9")
        self.Label_top.configure(anchor="w")
        self.Label_top.configure(compound="left")
        self.Label_top.configure(font="-family {Purisa} -size 24 -weight bold")
        self.Label_top.configure(text="""RIDE X Administration""")

        self.logout_btn = Button(self.adminDashboardFrame)
        self.logout_btn.place(relx=0.893, rely=0.87, height=33, width=103)
        self.logout_btn.configure(activebackground="beige")
        self.logout_btn.configure(background="#00FFFF")
        self.logout_btn.configure(borderwidth="2")
        self.logout_btn.configure(compound="left")
        self.logout_btn.configure(text="""Logout""", command=self.logout)

        self.assign_btn = Button(self.adminDashboardFrame)
        self.assign_btn.place(relx=0.460, rely=0.530, height=35, width=103)
        self.assign_btn.configure(activebackground="beige")
        self.assign_btn.configure(background="#00FFFF")
        self.assign_btn.configure(borderwidth="2")
        self.assign_btn.configure(compound="left")
        self.assign_btn.configure(text="""ASSIGN""", command=self.assign)

        self.Labeldriver = Label(self.adminDashboardFrame)
        self.Labeldriver.place(relx=0.081, rely=0.538, height=43, width=278)
        self.Labeldriver.configure(activebackground="#f9f9f9")
        self.Labeldriver.configure(anchor="w")
        self.Labeldriver.configure(compound="left")
        self.Labeldriver.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.Labeldriver.configure(text="""Driver Details""")

        # self.driver_table = Label(self.adminDashboardFrame)
        # self.driver_table.place(relx=0.081, rely=0.607, height=190, width=1162)
        # self.driver_table.configure(activebackground="#f9f9f9")
        # self.driver_table.configure(anchor="w")
        # self.driver_table.configure(background="#FFFFFF")
        # self.driver_table.configure(compound="left")
        # self.driver_table.configure(text="""Label""")

        self.bookingTable()
        self.driverTable()

        self.adminDashboardFrame.mainloop()

    def bookingTable(self):

        self.booking_table = Frame(self.adminDashboardFrame, bg="#FFFFFF")
        self.booking_table.place(relx=0.081, rely=0.248, height=180, width=1162)
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

        self.booking = self.admincontrol()
        # for info in self.tablerecords:

        records = self.booking.allbookingDetails()
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

    def driverTable(self):

        self.drbooking_table = Frame(self.adminDashboardFrame, bg="#FFFFFF")
        self.drbooking_table.place(relx=0.081, rely=0.607, height=190, width=1162)
        table_scroll_bar = Scrollbar(self.drbooking_table)
        table_scroll_bar.place(relx=0.980, rely=0.00, height=160, width=15)
        self.driver_booking_table = ttk.Treeview(
            self.drbooking_table,
            yscrollcommand=table_scroll_bar.set,
            selectmode="extended",
        )
        self.driver_booking_table.place(
            relx=0.020,
            rely=0.030,
            height=160,
            width=1090,
        )
        # table_scroll_bar.config(
        #     command=driver_booking_table.yview,
        # )

        self.driver_booking_table["columns"] = (
            "DriverID",
            "FullName",
            "Contact",
            "Email",
            "Address",
            "VehicleNo",
            "VehicleModel",
            "LiscenceN0",
            "DriverStatus",
        )

        self.driver_booking_table.column("#0", width=0, stretch=NO)
        self.driver_booking_table.column("DriverID", width=40, anchor=W)
        self.driver_booking_table.column("FullName", width=70, anchor=W)
        self.driver_booking_table.column("Contact", width=40, anchor=W)
        self.driver_booking_table.column("Email", width=120, anchor=W)
        self.driver_booking_table.column("Address", width=40, anchor=W)
        self.driver_booking_table.column("VehicleNo", width=70, anchor=W)
        self.driver_booking_table.column("VehicleModel", width=70, anchor=W)
        self.driver_booking_table.column("LiscenceN0", width=70, anchor=W)
        self.driver_booking_table.column("DriverStatus", width=60, anchor=W)

        self.driver_booking_table.heading("#0", text="", anchor=W)
        self.driver_booking_table.heading("DriverID", text="DriverID", anchor=W)
        self.driver_booking_table.heading("FullName", text="FullName", anchor=W)
        self.driver_booking_table.heading("Contact", text="Contact", anchor=W)
        self.driver_booking_table.heading("Email", text="Email", anchor=W)
        self.driver_booking_table.heading("Address", text="Address", anchor=W)
        self.driver_booking_table.heading("VehicleNo", text="VehicleNo", anchor=W)
        self.driver_booking_table.heading("VehicleModel", text="VehicleModel", anchor=W)
        self.driver_booking_table.heading("LiscenceN0", text="LiscenceN0", anchor=W)
        self.driver_booking_table.heading("DriverStatus", text="DriverStatus", anchor=W)

        self.booking = self.admincontrol()

        records = self.booking.alldriverDetails()
        # print(records)

        for data in records:
            self.driver_booking_table.insert(
                "",
                index="end",
                values=(
                    data[0],
                    (data[1] + " " + data[2]),
                    data[3],
                    data[5],
                    data[4],
                    data[6],
                    data[7],
                    data[8],
                    data[10],
                ),
            )

    def assign(self):
        try:
            selectedbooking = self.user_booking_table.focus()
            selected_booking_row = self.user_booking_table.item(
                selectedbooking,
                "values",
            )
            selected_booking_id = selected_booking_row[0]
            selected_booking_status = selected_booking_row[8]

        except Exception as e:
            messagebox.showerror("Invalid", "Booking Id not selected")
        try:

            selecteddriver = self.driver_booking_table.focus()
            selected_driver_row = self.driver_booking_table.item(
                selecteddriver,
                "values",
            )
            selected_driver_id = selected_driver_row[0]
            selected_driver_status = selected_driver_row[8]
        except Exception as e:
            messagebox.showerror("Invalid", "Driver Id not selected")
        try:
            if selected_booking_status == "confirmed":
                messagebox.showerror("Invalid", "Booking is already Assigned")
            else:
                if selected_driver_status == "booked":
                    messagebox.showerror("Invalid", "Driver is already Booked")
                else:
                    assignControll = self.admincontrol()
                    assignControll.bookingAssignControll(
                        selected_driver_id, selected_booking_id
                    )

                    messagebox.showinfo(
                        "SUCCESS",
                        "Driver Id "
                        + selected_driver_id
                        + " is assigned to booking Id "
                        + selected_booking_id,
                    )
                self.bookingTable()
                self.driverTable()
        except Exception as e:
            pass

    def logout(self):
        response = messagebox.askquestion(
            title="Log Out !",
            message="Are You Sure?",
            icon="warning",
        )

        if response == "yes":
            self.adminDashboardFrame.destroy()
    
    
           
