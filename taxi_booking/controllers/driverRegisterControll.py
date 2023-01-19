from helper.dbconnection import SysDb
from tkinter import messagebox

from view.driverDashboard import driverDashboard


class driverRegistercontroll:
    def __init__(self) -> None:
        self._connection = SysDb.Connection()

    def driverDetails(self, driverID):

        try:
            statement = "SELECT * FROM driver where driverID = %s;"
            id = str(driverID)
            data = id
            cursor = self._connection.cursor()
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def driverRegister_controll(self, user):
        try:
            cursor = self._connection.cursor()
            statement = """CREATE TABLE IF NOT EXISTS driver(
                driverID  SERIAL PRIMARY KEY,
                Firstname   VARCHAR(50) NOT NULL,
                lastname    VARCHAR(50) NOT NULL,
                contact VARCHAR(20) NOT NULL,
                address VARCHAR(20) NOT NULL,
                email VARCHAR(50) NOT NULL UNIQUE,
                vehicleno   VARCHAR(50) NOT NULL ,
                vehiclemod VARCHAR(50) NOT NULL,
                liscenceno VARCHAR(50) NOT NULL,
                password    VARCHAR(20) NOT NULL,
                Driverstatus Varchar(20)
                
            );"""

            data_insert = """INSERT INTO driver(firstname, lastname, contact,
            address, email, vehicleno, vehiclemod,liscenceno,password,Driverstatus) VALUES ( %s, %s, %s, %s, %s, %s,%s,%s,%s,%s);
            """
            data_values = (
                user.getFirstname(),
                user.getLastname(),
                user.getContactNo(),
                user.getAddress(),
                user.getEmail(),
                user.getVehicleno(),
                user.getVehiclemod(),
                user.getLiscenceno(),
                user.getPassword(),
                "Available",
            )
            cursor.execute(statement)
            cursor.execute(data_insert, data_values)
            self._connection.commit()
            return True

        except Exception as error:
            print(error)

        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()

    def driverlogin(self, user, root):
        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM driver WHERE email=%s AND password = %s;"
            data = (user.getEmail(), user.getPassword())
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            if self.record:
                for info in self.record:
                    firstname = info[1]
                    lastname = info[2]

                messagebox.showinfo("Sucess", "welcome " + firstname + " " + lastname)
                driverDashboard(root, self.record, driverRegistercontroll)

                return True

            else:
                messagebox.showerror("Invalid", "Invalid E-Mail or Password !!")

                return False

        except Exception as error:
            print(error)

        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()

    def assignedDetails(self, driverID):

        try:
            statement = "SELECT * FROM users as u JOIN booking as b ON u.userid = b.userid where driverId =%s ;"
            id = str(driverID)
            data = id
            cursor = self._connection.cursor()
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)
