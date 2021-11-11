import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

import utilities
from Model.book_list import BookList
from Model.loans import Loans
from Model.user_list import UserList


class LoansView:

    def __init__(self):
        self.validator = utilities.InputValidator()
        self.user_list_combobox = ttk.Combobox()
        self.book_list_combobox = ttk.Combobox()

    """
    A method to return over due books.
    Receives the loan list as a parameter, and calls teh loans model to get overdue books
    """

    def view_overdue_books(self, loan_list: Loans):
        new_window = Tk()
        new_window.title("Library System - JK")

        overdue_list = loan_list.get_overdue_books()

        headings = ["Book Id", "Title", "Username", "Firstname", "Surname", "Date Borrowed", "Due Date"]

        self.create_table(new_window, headings, overdue_list)

    """
        A method to return over due books.
        Receives the loan list as a parameter, and calls teh loans model to get overdue books
    """

    def load_loan_form(self, loan_list: Loans, user_list: UserList, book_list: BookList):
        new_window = Tk()
        new_window.title("Library System - Loan Books")

        # set the configuration of GUI window
        new_window.geometry("420x500")

        # create a User dropdown label
        user = Label(new_window, text="Select User", padx=40, pady=20)

        book = Label(new_window, text="Select Book", padx=40, pady=20)

        # create a Submit Button and place into the root window
        add_loan_button = Button(new_window, text="Loan", command=lambda: self.create_loan(
            new_window,
            user_list,
            book_list,
            loan_list
        ))

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        user.grid(row=1, column=0)
        book.grid(row=1, column=1)
        add_loan_button.grid(row=4, column=1)

        user_list_for_display = []
        for user in user_list.user_list:
            user_list_for_display.append(f'{user.get_firstname()} {user.get_surname()}')

        book_list_for_display = []
        for book in book_list.book_list:
            # Only display books that are available to be borrowed
            if book.get_copies_available() > 0:
                book_list_for_display.append(book.get_title())

        self.user_list_combobox = ttk.Combobox(new_window, values=user_list_for_display)
        self.user_list_combobox.grid(row=2, column=0)

        self.book_list_combobox = ttk.Combobox(new_window, values=book_list_for_display)
        self.book_list_combobox.grid(row=2, column=1)

    def view_loan_list(self, loan_list: Loans):
        new_window = Tk()
        new_window.title("Library System - LoanList")

        loan_list = loan_list.view()

        headings = ["Book Id", "Title", "Username", "Firstname", "Surname", "Date Borrowed", "Due Date"]

        self.create_table(new_window, headings, loan_list)

    """
    A method to build the views table for loans
    It passes in headers, the frame of view and data to be displayed
    """

    def create_table(self, windows, headings, data):
        frame = Frame(windows)
        tk.Button(frame)
        frame.pack(side=tk.LEFT, padx=30)
        no_of_columns = self.validator.get_column_count(len(headings))
        table = ttk.Treeview(frame, columns=no_of_columns, show="headings", height="5000")
        table.pack()

        for i in range(len(headings)):
            table.heading(i + 1, text=headings[i])

        for i in data:
            print(i)
            table.insert('', 'end', values=i)

    def create_loan(self, root, user_list, book_list, loan_list):

        if self.user_list_combobox.get() == '' or self.book_list_combobox.get() == '':
            messagebox.showinfo("Information", "Empty Input")
        else:
            user = self.user_list_combobox.get()
            firstname = user.split(' ')[0]
            get_user = user_list.search(firstname)

            book = self.book_list_combobox.get()
            get_book = book_list.search(book)

            loan_list.borrow_book(get_user[0], get_book, 3)
            messagebox.showinfo("Information", "Book borrowed")
            root.destroy()


