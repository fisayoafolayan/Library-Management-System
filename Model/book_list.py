class BookList:

    def __init__(self):
        self.book_list = []

    # Method to search for a book from a book list by  book title
    def search(self, title):
        return [books for books in self.book_list if books.get_title() == title][0]

    # Method to add a book to a book list
    def add(self, book):
        self.book_list.append(book)

    # Method to remove a book to a book list
    def remove(self, name):
        for i in range(len(self.book_list)):
            books = self.book_list[i]
            if books.get_title() == name:
                self.book_list.pop(i)
                break

    # Method to count the total number of books in a book list
    def count(self):
        return len(self.book_list)

    # Method to view all books in a book list
    def view(self):
        for books in self.book_list:
            print(books)
