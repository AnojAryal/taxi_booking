from helper.dbconnection import SysDb
from tkinter import messagebox
from view.adminDashboard import adminDashboard


class adminControl:
    def __init__(self) -> None:
        self._connection = SysDb.Connection()

    def adminlogin(self, user, root):
        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM admin WHERE Email=%s AND Password = %s;"
            data = (user.getEmail(), user.getPassword())
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            if self.record:

                messagebox.showinfo("Sucess", "welcome Admin")
                adminDashboard(root, self.record, adminControl)

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

    def allbookingDetails(self):

        try:
            statement = "SELECT * FROM booking ;"

            cursor = self._connection.cursor()
            cursor.execute(statement)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def alldriverDetails(self):

        try:
            statement = "SELECT * FROM driver ;"

            cursor = self._connection.cursor()
            cursor.execute(statement)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def bookingAssignControll(self, selected_driver_id, selected_booking_id):
        try:
            bookingstatement = "update booking set status='confirmed' , DriverID= %s where bookingID=%s  ;"
            bookingID = str(selected_booking_id)
            driverID = str(selected_driver_id)

            bookingdata = (driverID, bookingID)

            cursor = self._connection.cursor()
            cursor.execute(bookingstatement, bookingdata)
            driverstatement = (
                "update driver set Driverstatus='booked'  where driverID=%s  ;"
            )

            driverdata = driverID
            cursor.execute(driverstatement, driverdata)

            self._connection.commit()

        except Exception as error:
            print(error)
