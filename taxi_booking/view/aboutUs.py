from tkinter import *
from view import home


class aboutUs:
    def __init__(self, root):

        self.root = root
        self.signupPage()

    def signupPage(self):

        self.aboutUsFrame = Frame(self.root)
        self.aboutUsFrame.place(relx=0, rely=0, height=768, width=1366)
        # self.aboutUsFrame.geometry("1366x725+-13+-11")
        # self.aboutUsFrame.minsize(1, 1)
        # self.aboutUsFrame.maxsize(1351, 738)
        # self.aboutUsFrame.resizable(1, 1)
        # self.aboutUsFrame.title("Toplevel 0")
        self.aboutUsFrame.configure(background="#d5f4e6")

        self.Label1 = Label(self.aboutUsFrame)
        self.Label1.place(relx=0.256, rely=0.041, height=124, width=647)
        self.Label1.configure(anchor="w")
        self.Label1.configure(background="#d5f4e6")
        self.Label1.configure(compound="left")
        self.Label1.configure(font="-family {Purisa} -size 72 -slant italic")
        self.Label1.configure(text="""ABOUT US!!!""")

        self.Label2 = Label(self.aboutUsFrame)
        self.Label2.place(relx=0.073, rely=0.29, height=450, width=500)
        self.Label2.configure(anchor="w")
        self.Label2.configure(compound="left")
        self.background = PhotoImage(
            file="C:/Users/DELL-14/Desktop/taxi_booking/images/car.png"
        )
        self.Label2.configure(image=self.background)

        self.Label3 = Label(self.aboutUsFrame)
        self.Label3.place(relx=0.469, rely=0.428, height=42, width=718)
        self.Label3.configure(anchor="w")
        self.Label3.configure(background="#d5f4e6")
        self.Label3.configure(compound="left")
        self.Label3.configure(font="-family {Purisa} -size 12 -weight bold")
        self.Label3.configure(
            text="""RIDE  X is the large run taxi company from where you can book your"""
        )

        self.Label3_1 = Label(self.aboutUsFrame)
        self.Label3_1.place(relx=0.469, rely=0.483, height=42, width=688)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(anchor="w")
        self.Label3_1.configure(background="#d5f4e6")
        self.Label3_1.configure(compound="left")
        self.Label3_1.configure(font="-family {Purisa} -size 12 -weight bold")
        self.Label3_1.configure(
            text="""trips. You can directly book a trip once you are logined to the"""
        )

        self.Label3_1_1 = Label(self.aboutUsFrame)
        self.Label3_1_1.place(relx=0.469, rely=0.538, height=42, width=707)
        self.Label3_1_1.configure(activebackground="#f9f9f9")
        self.Label3_1_1.configure(anchor="w")
        self.Label3_1_1.configure(background="#d5f4e6")
        self.Label3_1_1.configure(compound="left")
        self.Label3_1_1.configure(font="-family {Purisa} -size 12 -weight bold")
        self.Label3_1_1.configure(
            text="""application.You can have amazing trip experience with the most"""
        )

        self.Label3_1_1_1 = Label(self.aboutUsFrame)
        self.Label3_1_1_1.place(relx=0.471, rely=0.593, height=42, width=728)
        self.Label3_1_1_1.configure(activebackground="#f9f9f9")
        self.Label3_1_1_1.configure(anchor="w")
        self.Label3_1_1_1.configure(background="#d5f4e6")
        self.Label3_1_1_1.configure(compound="left")
        self.Label3_1_1_1.configure(font="-family {Purisa} -size 12 -weight bold")
        self.Label3_1_1_1.configure(
            text="""comfortable vehicles.RIDE X provides you the best trip experience ever"""
        )

        # self.backonce.deiconify()

        self.Button1 = Button(self.aboutUsFrame)
        self.Button1.place(relx=0.908, rely=0.883, height=33, width=73)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound="left")
        self.Button1.configure(text="""BACK""", command=self.redirect)

        self.Label4 = Label(self.aboutUsFrame)
        self.Label4.place(relx=0.47, rely=0.65, height=32, width=370)
        self.Label4.configure(anchor="w")
        self.Label4.configure(background="#d5f4e6")
        self.Label4.configure(compound="left")
        self.Label4.configure(font="-family {Purisa} -size 12 -weight bold")
        self.Label4.configure(text="""Book your trip and have a nice trip.""")

        # self.root.withdraw()
        self.aboutUsFrame.mainloop()

    def redirect(self):
        self.aboutUsFrame.destroy()
