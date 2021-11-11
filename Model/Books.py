import uuid
import utilities


class Books:

    def __init__(
            self,
            title,
            author,
            year: int,
            publisher,
            copies_available: int,
            publication_date
    ):
        self.book_id = uuid.uuid4().hex[:6]
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.copies_available = copies_available
        self.publication_date = publication_date
        self.validator = utilities.InputValidator()

    # Method to get a book id
    def get_book_id(self):
        return self.book_id

    # Method to get book title
    def get_title(self):
        return self.title

    # Method to set book title
    def set_title(self, title):
        self.set_prop(title, 'title', 'str')

    # Method to get book author
    def get_author(self):
        return self.author

    # Method to set book author
    def set_author(self, author):
        self.set_prop(author, 'author', 'str')

    # Method to get book year
    def get_year(self):
        return self.year

    # Method to set book title
    def set_year(self, year):
        self.set_prop(year, 'year', 'int')

    # Method to get book publisher
    def get_publisher(self):
        return self.publisher

    # Method to set book publisher
    def set_publisher(self, publisher):
        self.set_prop(publisher, 'publisher', 'str')

    # Method to get copies available
    def get_copies_available(self):
        return self.copies_available

    # Method to set copies available
    def set_copies_available(self, copies_available):
        self.set_prop(copies_available, 'copies_available', 'int')

    # Method to get publication date
    def get_publication_date(self):
        return self.publication_date

    # Method to set publication date
    def set_publication_date(self, publication_date):
        self.set_prop(publication_date, 'publication_date', 'str')

    # Method to edit title
    def edit_title(self, title):
        self.title = title

    # Method to edit author
    def edit_author(self, author):
        self.author = author

    # Method to edit year
    def edit_year(self, year):
        self.year = year

    # Method to edit publisher
    def edit_publisher(self, publisher):
        self.publisher = publisher

    # Method to edit copies available
    def edit_copies_available(self, copies_available):
        self.copies_available = copies_available

    # Method to edit publication date
    def edit_publication_date(self, publication_date):
        self.publication_date = publication_date

    '''
    Method sets property for attributes provided. 
    Returns ValueError if type provided does not match expected data type
    '''
    def set_prop(self, data, attribute, data_type):
        try:
            self.validator.validate_data_type(attribute, data_type)
            setattr(self, attribute, data)
        except ValueError as message:
            print(message)

    def __repr__(self):
        return f'"{self.book_id}" "{self.title}" "{self.author}" "{self.year}" "{self.publisher}" ' \
               f'"{self.copies_available}" "{self.publication_date}" '
