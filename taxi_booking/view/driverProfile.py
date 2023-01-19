from tkinter import *


class driverProfile:
    def __init__(self, root, record):
        self.record = record
        # self.root = root

        self.display = Toplevel(root, background="#c9c9c9")
        self.display.geometry("600x600+213+75")
        self.display.resizable(False, False)
        self.display.title("Taxi booking System")
        self.display.minsize(1, 1)
        self.display.maxsize(1351, 738)

        for data in self.record:
            Firstname = data[1]
            lastname = data[2]
            contact = data[3]
            address = data[4]
            vehicleno = data[6]
            liscenceno = data[8]
            email = data[5]

        self.label_fullname = Label(self.display)
        self.label_fullname.place(relx=0.033, rely=0.433, height=31, width=159)
        self.label_fullname.configure(anchor="w")
        self.label_fullname.configure(background="#c9c9c9")
        self.label_fullname.configure(compound="left")
        self.label_fullname.configure(
            font="-family {DejaVu Sans} -size 18 -weight bold"
        )
        self.label_fullname.configure(text="""FullName  :""")

        self.Label_image = Label(self.display)
        self.Label_image.place(relx=0.05, rely=0.033, height=201, width=259)
        self.Label_image.configure(anchor="w")
        self.Label_image.configure(compound="left")
        self.Label_image.configure(cursor="fleur")
        self.Label_image.configure(background="#c9c9c9")
        self.photo3e = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/profiles.png"
        )
        self.Label_image.configure(image=self.photo3e)

        self.label_address = Label(self.display)
        self.label_address.place(relx=0.033, rely=0.517, height=31, width=159)
        self.label_address.configure(activebackground="#f9f9f9")
        self.label_address.configure(anchor="w")
        self.label_address.configure(background="#c9c9c9")
        self.label_address.configure(compound="left")
        self.label_address.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.label_address.configure(text="""Address    :""")

        self.Label_liscence = Label(self.display)
        self.Label_liscence.place(relx=0.033, rely=0.6, height=31, width=159)
        self.Label_liscence.configure(activebackground="#f9f9f9")
        self.Label_liscence.configure(background="#c9c9c9")
        self.Label_liscence.configure(anchor="w")
        self.Label_liscence.configure(compound="left")
        self.Label_liscence.configure(
            font="-family {DejaVu Sans} -size 18 -weight bold"
        )
        self.Label_liscence.configure(text="""Liscence   :""")

        self.label_email = Label(self.display)
        self.label_email.place(relx=0.033, rely=0.687, height=31, width=159)
        self.label_email.configure(activebackground="#f9f9f9")
        self.label_email.configure(background="#c9c9c9")
        self.label_email.configure(anchor="w")
        self.label_email.configure(compound="left")
        self.label_email.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.label_email.configure(text="""E-Mail       :""")

        self.Label_contactno = Label(self.display)
        self.Label_contactno.place(relx=0.033, rely=0.783, height=31, width=159)
        self.Label_contactno.configure(activebackground="#f9f9f9")
        self.Label_contactno.configure(background="#c9c9c9")
        self.Label_contactno.configure(anchor="w")
        self.Label_contactno.configure(compound="left")
        self.Label_contactno.configure(
            font="-family {DejaVu Sans} -size 18 -weight bold"
        )
        self.Label_contactno.configure(text="""Contact    :""")

        self.Button_back = Button(self.display)
        self.Button_back.place(relx=0.833, rely=0.9, height=33, width=66)
        self.Button_back.configure(activebackground="beige")
        self.Button_back.configure(borderwidth="2")
        self.Button_back.configure(compound="left")
        self.Button_back.configure(background="#d5f4e6")
        self.Button_back.configure(text="""BACK""", command=self.redirect11)

        self.Fullname_ent = Label(self.display)
        self.Fullname_ent.place(relx=0.367, rely=0.435, height=31, width=280)
        self.Fullname_ent.configure(activebackground="#f9f9f9")
        self.Fullname_ent.configure(background="#c9c9c9")
        self.Fullname_ent.configure(anchor="w")
        self.Fullname_ent.configure(compound="left")
        self.Fullname_ent.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.Fullname_ent.configure(text=Firstname + " " + lastname)

        self.Address_ent = Label(self.display)
        self.Address_ent.place(relx=0.367, rely=0.522, height=31, width=280)
        self.Address_ent.configure(activebackground="#f9f9f9")
        self.Address_ent.configure(background="#c9c9c9")
        self.Address_ent.configure(anchor="w")
        self.Address_ent.configure(compound="left")
        self.Address_ent.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.Address_ent.configure(text=address)

        self.liscence_ent = Label(self.display)
        self.liscence_ent.place(relx=0.367, rely=0.603, height=31, width=280)
        self.liscence_ent.configure(activebackground="#f9f9f9")
        self.liscence_ent.configure(background="#c9c9c9")
        self.liscence_ent.configure(anchor="w")
        self.liscence_ent.configure(compound="left")
        self.liscence_ent.configure(text=liscenceno)
        self.liscence_ent.configure(font="-family {DejaVu Sans} -size 18 -weight bold")

        self.email_ent = Label(self.display)
        self.email_ent.place(relx=0.367, rely=0.688, height=31, width=280)
        self.email_ent.configure(activebackground="#f9f9f9")
        self.email_ent.configure(background="#c9c9c9")
        self.email_ent.configure(anchor="w")
        self.email_ent.configure(compound="left")
        self.email_ent.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.email_ent.configure(text=email)

        self.contact_ent = Label(self.display)
        self.contact_ent.place(relx=0.367, rely=0.783, height=31, width=280)
        self.contact_ent.configure(activebackground="#f9f9f9")
        self.contact_ent.configure(background="#c9c9c9")
        self.contact_ent.configure(anchor="w")
        self.contact_ent.configure(compound="left")
        self.contact_ent.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.contact_ent.configure(text=contact)

        self.label_fullname_1 = Label(self.display)
        self.label_fullname_1.place(relx=0.343, rely=0.170, height=35, width=220)

        self.label_fullname_1.configure(activebackground="#f9f9f9")
        self.label_fullname_1.configure(background="#c9c9c9")
        self.label_fullname_1.configure(anchor="w")
        self.label_fullname_1.configure(compound="left")
        self.label_fullname_1.configure(
            font="-family {DejaVu Sans} -size 18 -weight bold"
        )
        self.label_fullname_1.configure(text="""-----Profile""")
        self.display.grab_set()
        self.display.mainloop()

    def redirect11(self):
        self.display.destroy()
