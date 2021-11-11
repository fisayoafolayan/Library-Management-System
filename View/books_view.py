import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import utilities
from Model.Books import Books
from Model.book_list import BookList


class BooksView:
    def __init__(self):
        self.title_field = Entry()
        self.author_field = Entry()
        self.year_field = Entry()
        self.publisher_field = Entry()
        self.copies_available_field = Entry()
        self.publication_date_field = Entry()
        self.search_box_field = Entry()
        self.validator = utilities.InputValidator()

    # Method to build view book frame and return all books in book list
    def view_books(self, book_list: BookList):
        new_window = Tk()
        new_window.title("Library System - BookList")

        headings = ["Book Id", "Title", "Author", "Year", "Publisher", "Copies Available", "Publication Date"]
        self.create_table(new_window, headings, book_list.book_list)

    # Function to take data from GUI
    # Also serves as method to edit book.
    def insert_book(self, root, book_list: BookList, book_id=''):

        # check for empty input
        if (
                self.title_field.get() == "" or
                self.author_field.get() == "" or
                self.year_field.get() == "" or
                self.publisher_field.get() == "" or
                self.copies_available_field.get() == "" or
                self.publication_date_field.get() == ""
        ):
            messagebox.showinfo("Information", "Invalid Input, Please Provide a valid input")
        else:
            if book_id != '':
                for book in book_list.book_list:
                    if book.get_book_id() == book_id:
                        book.edit_title(self.title_field.get())
                        book.edit_author(self.author_field.get())
                        book.edit_year(self.year_field.get())
                        book.edit_publisher(self.publisher_field.get())
                        book.edit_copies_available(int(self.copies_available_field.get()))
                        book.edit_publication_date(self.publication_date_field.get())
                        messagebox.showinfo("Information", "Edit Successful")
                        root.destroy()
            else:
                new_book = Books(
                    self.title_field.get(),
                    self.author_field.get(),
                    int(self.year_field.get()),
                    self.publisher_field.get(),
                    int(self.copies_available_field.get()),
                    self.publication_date_field.get()
                )
                book_list.add(new_book)
                messagebox.showinfo("Information", "Success, Book Added to Library")
                root.destroy()

    def add_book(self, book_list):
        new_window = Tk()
        new_window.title("Library System - Add Book")

        # set the configuration of GUI window
        new_window.geometry("550x500")

        # create a Title label
        title = Label(new_window, text="Title")

        # create a Author label
        author = Label(new_window, text="Author")

        # create a Year label
        year = Label(new_window, text="Year")

        # create a Publisher table
        publisher = Label(new_window, text="Publisher")

        # create a Copies Available label
        copies_available = Label(new_window, text="Copies Available")

        # create a Publication Date label
        publication_date = Label(new_window, text="Publication Date")

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        title.grid(row=1, column=0)
        author.grid(row=2, column=0)
        year.grid(row=3, column=0)
        publisher.grid(row=4, column=0)
        copies_available.grid(row=5, column=0)
        publication_date.grid(row=6, column=0)

        # create a text entry box
        # for typing the information
        self.title_field = Entry(new_window)
        self.author_field = Entry(new_window)
        self.year_field = Entry(new_window)
        self.publisher_field = Entry(new_window)
        self.copies_available_field = Entry(new_window)
        self.publication_date_field = Entry(new_window)

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        self.title_field.grid(row=1, column=1, padx=40, pady=20, ipadx="100")
        self.author_field.grid(row=2, column=1, padx=40, pady=20, ipadx="100")
        self.year_field.grid(row=3, column=1, padx=40, pady=20, ipadx="100")
        self.publisher_field.grid(row=4, column=1, padx=40, pady=20, ipadx="100")
        self.copies_available_field.grid(row=5, column=1, padx=40, pady=20, ipadx="100")
        self.publication_date_field.grid(row=6, column=1, padx=40, pady=20, ipadx="100")

        # create a Submit Button and place into the root window
        submit = Button(new_window, text="Submit", command=lambda: self.insert_book(new_window, book_list))
        submit.grid(row=7, column=1)

    def create_table(self, windows, headings, data_list):
        frame = Frame(windows)
        tk.Button(frame)
        frame.pack(side=tk.LEFT, padx=30)
        no_of_columns = self.validator.get_column_count(len(headings))
        table = ttk.Treeview(frame, columns=no_of_columns, show="headings", height="5000")
        table.pack()

        for i in range(len(headings)):
            table.heading(i + 1, text=headings[i])

        for i in data_list:
            print(i)
            table.insert('', 'end', values=i)

    def get_book(self, root, book_list):

        if self.search_box_field.get() == "":
            messagebox.showinfo("Information", "Empty input")
        else:
            print(self.search_box_field.get())
            found = False
            for book in book_list.book_list:
                if book.get_book_id() == self.search_box_field.get():
                    found = True
                    root.destroy()
                    self.show_search_result(book, book_list)

            if not found:
                messagebox.showinfo("Information", "Book Not Found")

    # Method to edit a book from a book list
    def edit_book(self, book_list):
        new_window = Tk()
        new_window.title("Library System - Edit Book")

        # set the configuration of GUI window
        new_window.geometry("550x100")

        # create a Title label
        search_box = Label(new_window, text="Input Book ID")
        search_box.grid(row=1, column=0)
        self.search_box_field = Entry(new_window)
        # in table like structure .
        self.search_box_field.grid(row=1, column=1, padx=40, pady=20, ipadx="100")

        # create a Submit Button and place into the root window
        submit = Button(new_window, text="Submit", fg="Black", command=lambda: self.get_book(new_window, book_list))
        submit.grid(row=7, column=1)

    # Method to show search result and build search frame
    def show_search_result(self, book: Books, book_list: BookList):
        new_window = Tk()
        new_window.title("Library System - Edit Book: " + book.get_title())

        # set the configuration of GUI window
        new_window.geometry("550x500")

        # create a Title label
        book_id = Label(new_window, text="Book Id")

        # create a Title label
        title = Label(new_window, text="Title")

        # create a Author label
        author = Label(new_window, text="Author")

        # create a Year label
        year = Label(new_window, text="Year")

        # create a Publisher table
        publisher = Label(new_window, text="Publisher")

        # create a Copies Available label
        copies_available = Label(new_window, text="Copies Available")

        # create a Publication Date label
        publication_date = Label(new_window, text="Publication Date")

        book_id_value = Label(new_window, text=book.get_book_id())

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        book_id.grid(row=1, column=0)
        book_id_value.grid(row=1, column=1)
        title.grid(row=2, column=0)
        author.grid(row=3, column=0)
        year.grid(row=4, column=0)
        publisher.grid(row=5, column=0)
        copies_available.grid(row=6, column=0)
        publication_date.grid(row=7, column=0)

        # create a text entry box
        # for typing the information
        self.title_field = Entry(new_window)
        self.author_field = Entry(new_window)
        self.year_field = Entry(new_window)
        self.publisher_field = Entry(new_window)
        self.copies_available_field = Entry(new_window)
        self.publication_date_field = Entry(new_window)

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        # create a Title label

        self.title_field.grid(row=2, column=1, padx=40, pady=20, ipadx="100")
        self.author_field.grid(row=3, column=1, padx=40, pady=20, ipadx="100")
        self.year_field.grid(row=4, column=1, padx=40, pady=20, ipadx="100")
        self.publisher_field.grid(row=5, column=1, padx=40, pady=20, ipadx="100")
        self.copies_available_field.grid(row=6, column=1, padx=40, pady=20, ipadx="100")
        self.publication_date_field.grid(row=7, column=1, padx=40, pady=20, ipadx="100")

        self.title_field.insert(1, book.get_title())
        self.author_field.insert(1, book.get_author())
        self.year_field.insert(1, book.get_year())
        self.publisher_field.insert(1, book.get_publisher())
        self.copies_available_field.insert(1, book.get_copies_available())
        self.publication_date_field.insert(1, book.get_publication_date())

        # create a Submit Button and place into the root window
        submit = Button(new_window, text="Submit",
                        command=lambda: self.insert_book(new_window, book_list, book.get_book_id()))
        submit.grid(row=8, column=1)
        return
