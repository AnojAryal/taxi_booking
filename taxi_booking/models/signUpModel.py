from dataclasses import dataclass
from mimetypes import init
from tkinter import messagebox
import re


class signUpModel:

    # getter

    def getFirstname(self):
        return self.Firstname

    def getLastname(self):
        return self.Lastname

    def getContactNo(self):
        return self.ContactNo

    def getAddress(self):
        return self.Address

    def getCreditcardNo(self):
        return self.CreditcardNo

    def getEmail(self):
        return self.Email

    def getPassword(self):
        return self.Password

    def getConfirmPassword(self):
        return self.ConfirmPassword

    # setters

    def setFirstname(self, details):
        self.Firstname = details

    def setLastname(self, details):
        self.Lastname = details

    def setContactNo(self, details):
        self.ContactNo = details

    def setAddress(self, details):
        self.Address = details

    def setCreditcardNo(self, details):
        self.CreditcardNo = details

    def setEmail(self, details):
        self.Email = details

    def setPassword(self, details):
        self.Password = details

    def setConfirmPassword(self, details):
        self.ConfirmPassword = details

    def signUp_validator(self):
        nameReg = re.compile("^[A-Z][a-z]+$")  # firstname, lastname regex
        contactReg = re.compile("^[0-9]{10}$")  # contact regex
        creditcardReg = re.compile("^[0-9]{16}$")  # credit regex
        addressReg = re.compile(".+")  # address not null regex
        emailReg = re.compile("[a-z0-9]+@[a-z]+.[a-z]{2,3}")  # email address regex
        # usernameReg = re.compile(
        #         "[a-z][a-z0-9]*([._-][a-z0-9]+){0,3}$")

        if not nameReg.match(self.getFirstname()):
            messagebox.showerror("Invalid", "Invalid Firstname  !!")
            return False

        if not nameReg.match(self.getLastname()):
            messagebox.showerror("Invalid", "Invalid Lastname  !!")
            return False

        if not contactReg.match(self.getContactNo()):
            messagebox.showerror("Invalid", "Invalid ContactNo !!")
            return False

        if not addressReg.match(self.getAddress()):
            messagebox.showerror("Invalid", "Invalid Address !!")
            return False

        if not creditcardReg.match(self.getCreditcardNo()):
            messagebox.showerror("Invalid", "Invalid Credit Card No !!")
            return False

        if not emailReg.match(self.getEmail()):
            messagebox.showerror("Invalid", "Invalid E-Mail  !!")
            return False

        if not addressReg.match(self.getPassword()):
            messagebox.showerror("Invalid", "Invalid Password !!")
            return False

        return True
