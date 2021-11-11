import unittest

from Model.Books import Books
from Model.loans import Loans
from Model.users import Users


class TestLoans(unittest.TestCase):

    # initial setup to test loans class
    def setUp(self) -> None:
        self.book_data = {
            'title': 'Test book',
            'author': 'Fisayo',
            'year': 2010,
            'publisher': 'dfsfdf sdfd',
            'copies_available': 4,
            'publication_date': '02-05-97',
        }
        self.books = Books(**self.book_data)

        self.users_data = {
            'username': 'Test User',
            'firstname': 'user1',
            'surname': 'Test',
            'street_name': 'Yaba',
            'house_number': 25,
            'postcode': 2554,
            'email_address': 'fisayo@gmx.de',
            'date_of_birth': '02-05-97',
        }
        self.users = Users(**self.users_data)
        self.loans = Loans()

    # Test method to borrow book
    def test_borrow_book(self):
        self.loans.borrow_book(self.users, self.books, 2)
        self.assertEqual(3, self.books.get_copies_available())

    # Test method to return book
    def test_return_book(self):
        self.loans.return_book(self.users, self.books)
        self.assertEqual(4, self.books.get_copies_available())

