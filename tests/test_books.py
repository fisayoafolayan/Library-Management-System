import unittest

from Model.Books import Books


class TestBooks(unittest.TestCase):

    # initial setup to test books class
    def setUp(self) -> None:
        self.first_book = {
            'title': 'Test book',
            'author': 'testAuthor',
            'year': 2010,
            'publisher': 'dfsfdf sdfd',
            'copies_available': 4,
            'publication_date': '02-05-97',
        }
        self.books = Books(**self.first_book)

    # Test method to get title
    def test_get_title(self):
        self.assertEqual(self.books.get_title(), self.first_book['title'])

    # Test method to set title
    def test_set_title(self):
        new_data = 'new book'
        self.books.set_title(new_data)
        self.assertNotEqual(self.books.get_title(), self.first_book['title'])
        self.assertEqual(self.books.get_title(), new_data)

    # Test method to get author
    def test_get_author(self):
        self.assertEqual(self.books.get_author(), self.first_book['author'])

    # Test method to set title
    def test_set_author(self):
        new_data = 'new author'
        self.books.set_author(new_data)
        self.assertNotEqual(self.books.get_author(), self.first_book['author'])
        self.assertEqual(self.books.get_author(), new_data)

    # Test method to add year
    def test_get_year(self):
        self.assertEqual(self.books.get_year(), self.first_book['year'])

    # Test method to set year
    def test_set_year(self):
        new_data = 1990
        self.books.set_year(new_data)
        self.assertNotEqual(self.books.get_year(), self.first_book['year'])
        self.assertEqual(self.books.get_year(), new_data)

    # Test method to get publisher
    def test_get_publisher(self):
        self.assertEqual(self.books.get_publisher(), self.first_book['publisher'])

    # Test method to set publisher
    def test_set_publisher(self):
        new_data = 'new publisher'
        self.books.set_publisher(new_data)
        self.assertNotEqual(self.books.get_publisher(), self.first_book['publisher'])
        self.assertEqual(self.books.get_publisher(), new_data)

    # Test method to get available copies
    def test_get_copies_available(self):
        self.assertEqual(self.books.get_copies_available(), self.first_book['copies_available'])

    # Test method to set available copies
    def test_set_copies_available(self):
        new_data = 5
        self.books.set_copies_available(new_data)
        self.assertNotEqual(self.books.get_copies_available(), self.first_book['copies_available'])
        self.assertEqual(self.books.get_copies_available(), new_data)

    # Test method to get publication date
    def test_get_publication_date(self):
        self.assertEqual(self.books.get_publication_date(), self.first_book['publication_date'])

    # Test method to set publication date
    def test_set_publication_date(self):
        new_data = '25-02-1956'
        self.books.set_publication_date(new_data)
        self.assertNotEqual(self.books.get_publication_date(), self.first_book['publication_date'])
        self.assertEqual(self.books.get_publication_date(), new_data)


