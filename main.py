from service.addressbook_manager import AddressBookManager
from models.contact import Contact


def main():
    manager = AddressBookManager()

    while True:
        print("\n=== Address Book Application ===")
        print("1. Create Address Book")
        print("2. Add Contact")
        print("3. Display Contacts")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter AddressBook name: ").strip()
            if not name:
                print("Book name cannot be empty.")
                continue
            manager.add_book(name)

        elif choice == 2:
            book_name = input("Enter AddressBook name: ").strip()
            book = manager.get_book(book_name)
            if not book:
                continue

            contact = Contact(
                input("First Name: ").strip(),
                input("Last Name: ").strip(),
                input("Address: ").strip(),
                input("City: ").strip(),
                input("State: ").strip(),
                input("Zip: ").strip(),
                input("Phone: ").strip(),
                input("Email: ").strip(),
            )
            book.add_contact(contact)

        elif choice == 3:
            book_name = input("Enter AddressBook name: ").strip()
            book = manager.get_book(book_name)
            if book:
                book.display_contacts()

        elif choice == 4:
            print("Exiting Address Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()