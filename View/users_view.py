import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import utilities
from Model.user_list import UserList
from Model.users import Users


class UsersView:

    def __init__(self):

        self.username_field = Entry()
        self.firstname_field = Entry()
        self.surname_field = Entry()
        self.house_number_field = Entry()
        self.street_name_field = Entry()
        self.postcode_field = Entry()
        self.email_address_field = Entry()
        self.date_of_birth_field = Entry()
        self.search_box_field = Entry()
        self.users_list = UserList
        self.validator = utilities.InputValidator()

    def view_users(self, user_list: UserList):
        new_window = Tk()
        new_window.title("Library System - Users")
        headings = [
            "User ID", "Username", "Firstname", "Surname", "House Number", "Street Name", "Postcode", "Email Address",
            "Date of Birth"
        ]
        self.create_table(new_window, headings, user_list.user_list)
        return

    def create_table(self, windows, headings, data):
        frame = Frame(windows)
        frame.pack(side=tk.LEFT, padx=20)
        no_of_columns = self.validator.get_column_count(len(headings))
        table = ttk.Treeview(frame, columns=no_of_columns, show="headings", height="5000")
        table.pack()

        for i in range(len(headings)):
            table.heading(i + 1, text=headings[i])

        for i in data:
            print(i)
            table.insert('', 'end', values=i)

        return

    # Function to take data from GUI
    def insert_user(self, root, user_list: UserList, user_id=''):
        # if user not fill any entry
        # then print "empty input"
        if (
                self.username_field.get() == "" or
                self.firstname_field.get() == "" or
                self.surname_field.get() == "" or
                self.house_number_field.get() == "" or
                self.street_name_field.get() == "" or
                self.postcode_field.get() == "" or
                self.email_address_field.get() == "" or
                self.date_of_birth_field.get() == ""
        ):
            messagebox.showinfo("Information", "Invalid Input")
            print("empty input")
        else:
            if user_id != '':
                for user in user_list.user_list:
                    if user.get_user_id() == user_id:
                        user.edit_username(self.username_field.get())
                        user.edit_firstname(self.firstname_field.get())
                        user.edit_surname(self.surname_field.get())
                        user.edit_house_number(self.house_number_field.get())
                        user.edit_street_name(self.street_name_field.get())
                        user.edit_postcode(self.postcode_field.get())
                        user.edit_email_address(self.email_address_field.get())
                        user.edit_date_of_birth(self.date_of_birth_field.get())
                        messagebox.showinfo("Information", "Edit Successful")
                        root.destroy()
            else:
                new_user = Users(
                    self.username_field.get(),
                    self.firstname_field.get(),
                    self.surname_field.get(),
                    self.house_number_field.get(),
                    self.street_name_field.get(),
                    self.postcode_field.get(),
                    self.email_address_field.get(),
                    self.date_of_birth_field.get()
                )
                user_list.add(new_user)
                print("User Added >")
                print(user_list.user_list)
                messagebox.showinfo("Information", "Success")
                root.destroy()

    def add_user(self, user_list):
        # self.book_list = book_list
        new_window = Tk()
        new_window.title("Library System - Add Book")

        # set the configuration of GUI window
        new_window.geometry("550x600")

        # create a Username label
        username = Label(new_window, text="Username")

        # create a Firstname label
        firstname = Label(new_window, text="Firstname")

        # create a Surname label
        surname = Label(new_window, text="Surname")

        # create a house number table
        house_number = Label(new_window, text="House Number")

        # create a Street name label
        street_name = Label(new_window, text="Street Name")

        # create a Postcode  label
        post_code = Label(new_window, text="Postcode")

        # create an Email Address  label
        email_address = Label(new_window, text="Email Address")

        # create a Date of birth  label
        date_of_birth = Label(new_window, text="Date of birth")

        # provide grid for table.
        username.grid(row=1, column=0)
        firstname.grid(row=2, column=0)
        surname.grid(row=3, column=0)
        house_number.grid(row=4, column=0)
        street_name.grid(row=5, column=0)
        post_code.grid(row=6, column=0)
        email_address.grid(row=7, column=0)
        date_of_birth.grid(row=8, column=0)

        # Provide input fields for the required fields
        self.username_field = Entry(new_window)
        self.firstname_field = Entry(new_window)
        self.surname_field = Entry(new_window)
        self.house_number_field = Entry(new_window)
        self.street_name_field = Entry(new_window)
        self.postcode_field = Entry(new_window)
        self.email_address_field = Entry(new_window)
        self.date_of_birth_field = Entry(new_window)

        self.username_field.grid(row=1, column=1, padx=40, pady=20, ipadx="100")
        self.firstname_field.grid(row=2, column=1, padx=40, pady=20, ipadx="100")
        self.surname_field.grid(row=3, column=1, padx=40, pady=20, ipadx="100")
        self.house_number_field.grid(row=4, column=1, padx=40, pady=20, ipadx="100")
        self.street_name_field.grid(row=5, column=1, padx=40, pady=20, ipadx="100")
        self.postcode_field.grid(row=6, column=1, padx=40, pady=20, ipadx="100")
        self.email_address_field.grid(row=7, column=1, padx=40, pady=20, ipadx="100")
        self.date_of_birth_field.grid(row=8, column=1, padx=40, pady=20, ipadx="100")

        # create a Submit Button and place into the root window
        submit = Button(new_window, text="Submit", fg="Black",
                        bg="Red", command=lambda: self.insert_user(new_window, user_list))
        submit.grid(row=9, column=1)

        return

    # Method to get a user from a user list
    def get_user(self, root, user_list):
        if self.search_box_field.get() == "":
            messagebox.showinfo("Information", "Empty Input, Please provide a username")
        else:
            found = False
            for user in user_list.user_list:
                if user.get_username() == self.search_box_field.get():
                    found = True
                    root.destroy()
                    self.show_search_result(user, user_list)
                    break

            if not found:
                messagebox.showinfo("Information", "User Not Found")

        pass

    # Method to edit a user
    def edit_user(self, user_list):
        new_window = Tk()
        new_window.title("Library System - Edit User")

        # set the configuration of GUI window
        new_window.geometry("550x100")

        # create a Input User Id label
        search_box = Label(new_window, text="Input Username")
        search_box.grid(row=1, column=0)
        self.search_box_field = Entry(new_window)
        # create search input field .
        self.search_box_field.grid(row=1, column=1, padx=40, pady=20, ipadx="100")

        # create a Submit Button and place into the root window
        submit = Button(new_window, text="Submit", fg="Black", command=lambda: self.get_user(new_window, user_list))
        submit.grid(row=7, column=1)

        return

    # Method to build and show search result
    def show_search_result(self, user: Users, user_list: UserList):
        new_window = Tk()
        new_window.title("Library System - Edit User: " + user.get_username())

        # set the configuration of GUI window
        new_window.geometry("550x600")

        # create a User Id label
        user_id_field = Label(new_window, text="User Id")

        # create a Username label
        username_field = Label(new_window, text="Username")

        # create a Firstname label
        firstname_field = Label(new_window, text="Firstname")

        # create a Surname label
        surname_field = Label(new_window, text="Surname")

        # create a House Number label
        house_number_field = Label(new_window, text="House Number")

        # create a Street Name label
        street_name_field = Label(new_window, text="Street Name")

        # create a Postcode table
        postcode_field = Label(new_window, text="Postcode")

        # create a Email Address label
        email_address_field = Label(new_window, text="Email Address")

        # create a Date of Birth Date label
        date_of_birth_field = Label(new_window, text="Date of Birth")

        user_id_value = Label(new_window, text=user.get_user_id())

        # grid method is used for placing input on frame

        user_id_field.grid(row=1, column=0)
        user_id_value.grid(row=1, column=1)
        username_field.grid(row=2, column=0)
        firstname_field.grid(row=3, column=0)
        surname_field.grid(row=4, column=0)
        house_number_field.grid(row=5, column=0)
        street_name_field.grid(row=6, column=0)
        postcode_field.grid(row=7, column=0)
        email_address_field.grid(row=8, column=0)
        date_of_birth_field.grid(row=9, column=0)

        # create input fields for al fields
        self.username_field = Entry(new_window)
        self.firstname_field = Entry(new_window)
        self.surname_field = Entry(new_window)
        self.house_number_field = Entry(new_window)
        self.street_name_field = Entry(new_window)
        self.postcode_field = Entry(new_window)
        self.email_address_field = Entry(new_window)
        self.date_of_birth_field = Entry(new_window)

        # grid method is used for placing input on frame
        self.username_field.grid(row=2, column=1, padx=40, pady=20, ipadx="100")
        self.firstname_field.grid(row=3, column=1, padx=40, pady=20, ipadx="100")
        self.surname_field.grid(row=4, column=1, padx=40, pady=20, ipadx="100")
        self.house_number_field.grid(row=5, column=1, padx=40, pady=20, ipadx="100")
        self.street_name_field.grid(row=6, column=1, padx=40, pady=20, ipadx="100")
        self.postcode_field.grid(row=7, column=1, padx=40, pady=20, ipadx="100")
        self.email_address_field.grid(row=8, column=1, padx=40, pady=20, ipadx="100")
        self.date_of_birth_field.grid(row=9, column=1, padx=40, pady=20, ipadx="100")

        self.username_field.insert(1, user.get_username())
        self.firstname_field.insert(1, user.get_firstname())
        self.surname_field.insert(1, user.get_surname())
        self.house_number_field.insert(1, user.get_house_number())
        self.street_name_field.insert(1, user.get_street_name())
        self.postcode_field.insert(1, user.get_postcode())
        self.email_address_field.insert(1, user.get_email_address())
        self.date_of_birth_field.insert(1, user.get_date_of_birth())

        # create a Submit Button and place into the root window
        submit = Button(
            new_window, text="Submit", fg="Black", command=lambda: self.insert_user(
                new_window, user_list, user.get_user_id())
        )
        submit.grid(row=10, column=1)
        return
