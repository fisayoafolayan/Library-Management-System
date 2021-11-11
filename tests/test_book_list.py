import unittest

from Model.Books import Books
from Model.book_list import BookList


class TestBookList(unittest.TestCase):

    # Initial setup to test book list
    def setUp(self) -> None:
        book_list = BookList()
        first_book_list = [
            {
                'title': 'Test book',
                'author': 'test author',
                'year': 2010,
                'publisher': 'dfsfdf sdfd',
                'copies_available': 4,
                'publication_date': '02-05-97',
            },
            {
                'title': 'Test book two',
                'author': 'test author two',
                'year': 2010,
                'publisher': 'dfsfdf sdfd',
                'copies_available': 4,
                'publication_date': '02-05-97',
            },
        ]
        for book in first_book_list:
            book_list.book_list.append(Books(**book))
        self.book_list = book_list

    # Test method to add new book
    def test_add(self):
        self.book_list.add(
            Books(**{
                'title': 'Test book three ',
                'author': 'test author three',
                'year': 2010,
                'publisher': 'dfsfdf sdfd',
                'copies_available': 4,
                'publication_date': '02-05-97',
            })
        )
        self.assertEqual(3, len(self.book_list.book_list))

    # Test method to remove a book
    def test_remove(self):
        self.book_list.remove('Test book')
        self.assertEqual(1, len(self.book_list.book_list))
