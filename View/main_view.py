from tkinter import *

from Model.Books import Books
from Model.book_list import BookList
from Model.loans import Loans
from Model.user_list import UserList
from Model.users import Users
import View

users_array = [
    Users('user1', 'Jim', 'Jones', 22, 'Borselstraß', 22765, 'fisayo@gmx.de', '02-05-97'),
    Users('user2', 'Tim', 'James', 21, 'kisselstraß', 21735, 'fgsayo@gmxx.de', '02-10-97'),
    Users('user3', 'Tom', 'Dreamer', 21, 'Nachbanshaftstraß', 22765, 'userThree@gmxx.de', '21-03-97'),
    Users('user4', 'Ken', 'Tester', 21, 'Morgenstraß', 22265, 'userFour@gmxx.de', '02-04-97'),
    Users('user5', 'Vas', 'Stewart', 21, 'Kimmelstraß', 21765, 'userFive@gmxx.de', '02-05-97'),
]

books_array = [
    Books(title='The quarterbacks the uncensored truth about the men in the pocket 1st ed.',
          author='Mickey Herskowitz',
          year=2010, publisher='Morrow', copies_available=4, publication_date='1990'),
    Books('Giants In Their Own Words', 'Richard Whittingham', 1990, 'McGraw-Hill', 3, '1993'),
    Books('Faces of Maine', 'Bob Niss', 1981, 'G. Gannett Books', 4, '1981'),
    Books('A Wolf At The Door A Jesse James Dawson Novel', 'Stephen King', 2012, 'Pocket Books', 3, '2012'),
    Books('The Shining', 'Stephen King', 2012, 'K. A. Stewart', 3, '2012'),
    Books('Salem', 'Stephen King', 1975, 'K. A. Stewart', 5, '2000'),
    Books('Motherless Child', 'Glen Hirshberg', 2015, 'Tor Books', 4, '2015'),
]


class MainView:
    def __init__(self):
        # Creates the initial data for the Library system
        self.book_list = BookList()
        for book in books_array:
            self.book_list.add(book)

        self.user_list = UserList()
        for user in users_array:
            self.user_list.add(user)

        self.loans = Loans()
        self.loans.borrow_book(users_array[1], books_array[1], 2)
        self.loans.borrow_book(users_array[0], books_array[1], 1)
        self.loans.borrow_book(users_array[0], books_array[2], 2)
        self.loans.borrow_book(users_array[0], books_array[2], -4)
        self.loans.borrow_book(users_array[1], books_array[2], -3)

    def build_library(self):
        """
        Builds the Navigation point of the library system
        """
        root = Tk()
        root.title("Library System - Home")
        root.geometry("600x250")

        view_books = Button(root, text="View Books", padx=40, pady=20, command=self.view_books_frame)
        add_book = Button(root, text="Add Books", padx=40, pady=20, command=self.view_add_books_frame)
        view_all_users = Button(root, text="View Users", padx=40, pady=20, command=self.view_users_frame)
        add_user = Button(root, text="Add User", padx=40, pady=20, command=self.add_users_frame)
        view_edit_book = Button(root, text="Edit Book", padx=40, pady=20, command=self.view_edit_book_frame)
        view_edit_user = Button(root, text="Edit User", padx=40, pady=20, command=self.view_edit_user_frame)
        view_loan_list = Button(root, text="Loan List", padx=40, pady=20, command=self.view_loan_list_frame)
        view_loan_books = Button(root, text="Loan Book", padx=40, pady=20, command=self.view_loan_form_frame)
        view_overdue_books = Button(root, text="View Overdue", padx=40, pady=20, command=self.view_overdue_frame)

        # Positions the button grid
        add_book.grid(row=1, column=0)
        view_books.grid(row=1, column=1)
        view_edit_book.grid(row=1, column=2)
        add_user.grid(row=2, column=0)
        view_all_users.grid(row=2, column=1)
        view_edit_user.grid(row=2, column=2)
        view_loan_list.grid(row=3, column=0)
        view_loan_books.grid(row=3, column=1)
        view_overdue_books.grid(row=3, column=2)

        root.mainloop()

    def view_books_frame(self):
        """
        Calls the view that builds the frame for book list
        """
        return View.books_view.BooksView().view_books(self.book_list)

    def view_add_books_frame(self):
        """
        Calls the view that builds the frame to add a new book
        """
        return View.books_view.BooksView().add_book(self.book_list)

    def view_edit_book_frame(self):
        """
        Calls the view that builds the frame to edit a book
        """
        return View.books_view.BooksView().edit_book(self.book_list)

    def view_users_frame(self):
        """
        Calls the view that builds the view user frame
        """
        return View.users_view.UsersView().view_users(self.user_list)

    def add_users_frame(self):
        """
        Calls the view that builds the frame for adding a new user
        """
        return View.users_view.UsersView().add_user(self.user_list)

    def view_edit_user_frame(self):
        """
        Calls the view that builds the frame for editing a new user
        """
        return View.users_view.UsersView().edit_user(self.user_list)

    def view_overdue_frame(self):
        """
        Calls the view that builds the frame for viewing overdue books
        """
        return View.loans_view.LoansView().view_overdue_books(self.loans)

    def view_loan_form_frame(self):
        """
        Calls the view that builds the frame for creating a loan
        """
        return View.loans_view.LoansView().load_loan_form(self.loans, self.user_list, self.book_list)

    def view_loan_list_frame(self):
        """
        Calls the view that builds the frame for viewing the loan list
        """
        return View.loans_view.LoansView().view_loan_list(self.loans)
