from Model.Books import Books
from Model.users import Users

from datetime import timedelta, date


class Loans:

    def __init__(self):
        self.loan_list = []

    # Method to borrow book
    def borrow_book(self, user: Users, book: Books, duration_in_days):
        if book.get_copies_available() > 0:
            # Reduces the count of books available
            book.set_copies_available(book.get_copies_available() - 1)

            # Adds book and user object to loan list
            self.loan_list.append({
                'user': user,
                'book': book,
                'date_borrowed': date.today() + timedelta(days=-3),
                'due_date': date.today() + timedelta(days=duration_in_days)
            })

    # Method to return book
    def return_book(self, user: Users, book: Books):
        for i, loan in enumerate(self.loan_list):
            # Verify username  in loan list is the same as username in user object provided
            if user.get_username() == loan['user'].get_username() \
                    and book.get_book_id() == loan['book'].get_book_id():
                # Increment copies_available attribute by one
                book.set_copies_available(loan['book'].get_copies_available() + 1)
                # Remove loan list object of returned book
                self.loan_list.pop(i)

    # Count total loans by username
    def count_loans_by_username(self, username):
        return len(self.search('user', 'username', username))

    # Check due date of loan items and return loan list of over due list
    def get_overdue_books(self):
        date_today = date.today() + timedelta(days=-2)
        # creates an empty array of over due loans
        loans = []
        for loan in self.loan_list:
            if date_today > loan['due_date']:
                loans.append(
                    f'"{loan["book"].get_book_id()}" "{loan["book"].get_title()}" "{loan["user"].get_username()}" '
                    f'"{loan["user"].get_firstname()}" "{loan["user"].get_surname()}" "{loan["date_borrowed"]}" '
                    f'"{loan["due_date"]}"')
        return loans

    # Accepts a book object, and returns users detail based on the loan list data
    def get_borrower_details(self, book: Books):
        loans = self.search('book', 'title', book.get_title())
        for loan in loans:
            print(
                f"'{loan['user'].get_username()}' '{loan['user'].get_surname()}' '{loan['user'].get_email_address()}'")

    # Searches for book title in loan list
    def search(self, criteria, key, value):
        return [loans for loans in self.loan_list if getattr(loans[criteria], key) == value]

    # Method to view all loans in a loan list
    def view(self):
        loans = []
        for loan in self.loan_list:
            loans.append(
                f'"{loan["book"].get_book_id()}" "{loan["book"].get_title()}" "{loan["user"].get_username()}" '
                f'"{loan["user"].get_firstname()}" "{loan["user"].get_surname()}" "{loan["date_borrowed"]}" '
                f'"{loan["due_date"]}"')
        return loans
