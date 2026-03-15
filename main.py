from addressbookManager import AddressBookManager
from contact import Contact
class AddressBookMain:


    @staticmethod
    def main():
        manager = AddressBookManager()

        while True:

            print("1 Create Address Book")
            print("2 Add Contact")
            print("3 Display Contacts")
            print("4 Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:

                name = input("Enter AddressBook name: ")
                manager.add_book(name)

            elif choice == 2:

                book = manager.get_book(input("Enter AddressBook name: "))

                if book:

                    contact = Contact(
                        input("First Name: "),
                        input("Last Name: "),
                        input("Address: "),
                        input("City: "),
                        input("State: "),
                        input("Zip: "),
                        input("Phone: "),
                        input("Email: ")
                    )

                    book.add_contact(contact)

            elif choice == 3:

                book = manager.get_book(input("Enter AddressBook name: "))

                if book:
                    book.display_contacts()

            elif choice == 4:
                break

    if __name__ == "__main__":
        main()