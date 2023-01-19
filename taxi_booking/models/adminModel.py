from dataclasses import dataclass
from mimetypes import init
from tkinter import messagebox
import re


class adminModel:

    # getters

    def getEmail(self):
        return self.Email

    def getPassword(self):
        return self.Password

    # setters

    def setEmail(self, details):
        self.Email = details

    def setPassword(self, details):
        self.Password = details


# def admin_validator(self):
#     passReg = re.compile(".+")  # password  regex
#     emailReg = re.compile("[a-z0-9]+@[a-z]+.[a-z]{2,3}")  # email address regex

#     if not emailReg.match(self.getEmail()):
#         messagebox.showerror("Invalid", "Invalid E-Mail  !!")
#         return False

#     if not passReg.match(self.getPassword()):
#         messagebox.showerror("Invalid", "Invalid Password !!")
#         return False

#     return True
