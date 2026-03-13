class AddressBookMain:

    @staticmethod
    def main():
        print("Welcome to the Address Book Application!")
        address_book_manager = AddressBookManager()
        address_book_manager.add_book("Personal")
        personal_book = address_book_manager.get_book("Personal")
        contact1 = Contact("John", "Doe", "123 Main St", "Anytown", "Anystate", "12345", "555-1234", "ff")
        personal_book.add_contact(contact1)
        print("Current contacts in Personal Address Book:")

    if __name__ == "__main__":
        main()