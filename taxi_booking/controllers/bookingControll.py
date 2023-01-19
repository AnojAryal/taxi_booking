from helper.dbconnection import SysDb
from tkinter import messagebox

# from view import home


# from view.viewBooking import viewBooking


class bookingControl:
    def __init__(self) -> None:
        self._connection = SysDb.Connection()

    def bookingDetails(self, userID):

        try:
            statement = "SELECT * FROM booking where userID = %s;"
            id = str(userID)
            data = id
            cursor = self._connection.cursor()
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def booking_controll(self, user, userID):
        try:
            cursor = self._connection.cursor()
            statement = """CREATE TABLE IF NOT EXISTS booking(

                bookingID  SERIAL PRIMARY KEY,
                userID     INT,    
                Fullname   VARCHAR(50) NOT NULL,
                email    VARCHAR(50) NOT NULL,
                contactno VARCHAR(20) NOT NULL,
                pickupdate VARCHAR(20) NOT NULL,
                pickuptime VARCHAR(50) NOT NULL,
                pickuplocation  VARCHAR(50) NOT NULL UNIQUE,
                droplocation    VARCHAR(20) NOT NULL,
                Status          VARCHAR(20),
                DriverID        INT


                
            );"""

            data_insert = """INSERT INTO booking(userID,Fullname, email, contactno, pickupdate,
            pickuptime, pickuplocation, droplocation,Status) VALUES ( %s,%s, %s, %s, %s, %s, %s,%s,%s);
            """
            data_values = (
                userID,
                user.getFullname(),
                user.getEmail(),
                user.getContact(),
                user.getPickupDate(),
                user.getPickupTime(),
                user.getPickupLocation(),
                user.getDropLocation(),
                "Pending",
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


    def Cancelbooking(self,bookingId):
        try:
            statement = "UPDATE booking SET status = 'Cancelled' where bookingID = %s"
            booking_ID = str(bookingId)
            data = booking_ID
            cursor = self._connection.cursor()
            cursor.execute(statement,data)
            self._connection.commit()
        except Exception as error:
            print(error)