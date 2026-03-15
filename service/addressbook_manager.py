from models.address_book import AddressBook


class AddressBookManager:
    def __init__(self):
        self.books = {}

    def add_book(self, book_name):
        if book_name not in self.books:
            self.books[book_name] = AddressBook()
            print("Address book '{}' created.".format(book_name))
        else:
            print("Book already exists.")

    def get_book(self, book_name):
        book = self.books.get(book_name)
        if book is None:
            print("Book not found.")
        return book

