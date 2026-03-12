from addressbook import AddressBook
class AddressBookManager:
   
   def __init__(self):
      self.books={}

   def add_book(self,book_name):
        if book_name not in self.books:
            self.books[book_name]=AddressBook()
        else:   
            raise ValueError("Book already exists")
    
   def get_book(self,book_name):
        if book_name in self.books:
            return self.books[book_name]
        else:
            raise ValueError("Book not found")
    
        