from dataclasses import dataclass
from mimetypes import init
from tkinter import messagebox
import re


class driverRegisterModel:

    # getter

    def getFirstname(self):
        return self.Firstname

    def getLastname(self):
        return self.Lastname

    def getContactNo(self):
        return self.ContactNo

    def getEmail(self):
        return self.Email

    def getAddress(self):
        return self.Address

    def getVehicleno(self):
        return self.Vehicleno

    def getVehiclemod(self):
        return self.Vehiclemod

    def getLiscenceno(self):
        return self.Liscenceno

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

    def setEmail(self, details):
        self.Email = details

    def setAddress(self, details):
        self.Address = details

    def setVehicleno(self, details):
        self.Vehicleno = details

    def setVehiclemod(self, details):
        self.Vehiclemod = details

    def setLiscenceno(self, details):
        self.Liscenceno = details

    def setPassword(self, details):
        self.Password = details

    def setConfirmPassword(self, details):
        self.ConfirmPassword = details

    def driverRegister_validator(self):
        nameReg = re.compile("^[A-Z][a-z]+$")  # firstname, lastname regex
        contactReg = re.compile("^[0-9]{10}$")  # contact regex
        vehicleReg = re.compile("^[0-9]{4}$")
        liscenceReg = re.compile("^[A-Z][0-9]+$")
        modelReg = re.compile(".+")

        addressReg = re.compile(".+")  # address not null regex
        emailReg = re.compile("[a-z0-9]+@[a-z]+.[a-z]{2,3}")  # email address regex

        if not nameReg.match(self.getFirstname()):
            messagebox.showerror("Invalid", "Invalid Firstname  !!")
            return False

        if not nameReg.match(self.getLastname()):
            messagebox.showerror("Invalid", "Invalid Lastname  !!")
            return False

        if not contactReg.match(self.getContactNo()):
            messagebox.showerror("Invalid", "Invalid ContactNo !!")
            return False

        if not emailReg.match(self.getEmail()):
            messagebox.showerror("Invalid", "Invalid E-Mail  !!")
            return False

        if not addressReg.match(self.getAddress()):
            messagebox.showerror("Invalid", "Invalid Address !!")
            return False

        if not vehicleReg.match(self.getVehicleno()):
            messagebox.showerror("Invalid", "Invalid Vehicle Number !!")
            return False

        if not modelReg.match(self.getVehiclemod()):
            messagebox.showerror("Invalid", "Invalid Vehicle Model !!")
            return False

        if not liscenceReg.match(self.getLiscenceno()):
            messagebox.showerror("Invalid", "Invalid liscence Number !!")
            return False

        if not addressReg.match(self.getPassword()):
            messagebox.showerror("Invalid", "Invalid Password !!")
            return False

        return True
