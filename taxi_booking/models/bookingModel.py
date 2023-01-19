from dataclasses import dataclass
from mimetypes import init
from tkinter import messagebox
import re


class bookingModel:

    # getters

    def getFullname(self):
        return self.Fullname

    def getEmail(self):
        return self.Email

    def getContact(self):
        return self.Contact

    def getPickupDate(self):
        return self.PickupDate

    def getPickupTime(self):
        return self.PickupTime

    def getPickupLocation(self):
        return self.PickupLocation

    def getDropLocation(self):
        return self.DropLocation

    # setters

    def setFullname(self, details):
        self.Fullname = details

    def setEmail(self, details):
        self.Email = details

    def setContact(self, details):
        self.Contact = details

    def setPickupDate(self, details):
        self.PickupDate = details

    def setPickupTime(self, details):
        self.PickupTime = details

    def setPickupLocation(self, details):
        self.PickupLocation = details

    def setDropLocation(self, details):
        self.DropLocation = details

    def booking_validator(self):
        nameReg = re.compile("^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")  # name regex
        contactReg = re.compile("^[0-9]{10}$")  # contact regex
        timeReg = re.compile(
            "((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))"
        )  # time regex
        dateReg = re.compile(
            "^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$"
        )  # date rejex
        addressReg = re.compile(".+")  # address not null regex
        emailReg = re.compile("[a-z0-9]+@[a-z]+.[a-z]{2,3}")  # email address regex
        # usernameReg = re.compile(
        #         "[a-z][a-z0-9]*([._-][a-z0-9]+){0,3}$")

        if not nameReg.match(self.getFullname()):
            messagebox.showerror("Invalid", "Invalid Fullname  !!")
            return False

        if not emailReg.match(self.getEmail()):
            messagebox.showerror("Invalid", "Invalid E-Mail !!")
            return False

        if not contactReg.match(self.getContact()):
            messagebox.showerror("Invalid", "Invalid Contact Number !!")
            return False

        if not dateReg.match(self.getPickupDate()):
            messagebox.showerror("Invalid", "Invalid Date!!")
            return False

        if not timeReg.match(self.getPickupTime()):
            messagebox.showerror("Invalid", "Please select time in correct format !!")
            return False

        if not addressReg.match(self.getPickupLocation()):
            messagebox.showerror("Invalid", "Invalid Location !!")
            return False

        if not addressReg.match(self.getDropLocation()):
            messagebox.showerror("Invalid", "Invalid Drop-Location !!")
            return False

        return True
