from helper.dbconnection import SysDb
from tkinter import messagebox
from view.home import home


class UserControl:
    def __init__(self) -> None:
        self._connection = SysDb.Connection()

    def signup_controll(self, user):
        try:
            cursor = self._connection.cursor()
            statement = """CREATE TABLE IF NOT EXISTS users(
                userID  SERIAL PRIMARY KEY,
                Firstname   VARCHAR(50) NOT NULL,
                lastname    VARCHAR(50) NOT NULL,
                contact VARCHAR(20) NOT NULL,
                creditcard VARCHAR(20) NOT NULL,
                address  VARCHAR(50) NOT NULL,
                email   VARCHAR(50) NOT NULL UNIQUE,
                password    VARCHAR(20) NOT NULL
                
            );"""
            data_insert = """INSERT INTO users(firstname, lastname, contact, creditcard,
            address, email, password) VALUES ( %s, %s, %s, %s, %s, %s,%s);
            """
            data_values = (
                user.getFirstname(),
                user.getLastname(),
                user.getContactNo(),
                user.getCreditcardNo(),
                user.getAddress(),
                user.getEmail(),
                user.getPassword()
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

    def login(self, user, root):
        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM users WHERE email=%s AND password = %s;"
            data = (user.getEmail(), user.getPassword())
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            if self.record:
                for info in self.record:
                    firstname = info[1]
                    lastname = info[2]

                messagebox.showinfo("Sucess", "welcome " + firstname + " " + lastname)
                home(root, self.record)

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
