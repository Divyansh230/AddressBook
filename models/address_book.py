from models.contact import Contact


class AddressBook:
    def __init__(self):
        # Use first_name as the key as in the original implementation
        self.contacts = {}

    # Add a single contact
    def add_contact(self, contact):
        if contact.first_name not in self.contacts:
            self.contacts[contact.first_name] = contact
            print("Contact added successfully.")
        else:
            print("Contact with this first name already exists.")

    # Edit an existing contact by first name
    def edit_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print("Editing contact:", contact)
            choice = input(
                "Enter the field you want to edit "
                "(first_name, last_name, address, city, state, zip_code, "
                "phone_number, email): "
            )
            if choice == "first_name":
                new_name = input("Enter new first name: ")
                # Update key in dictionary if first_name changes
                del self.contacts[name]
                contact.first_name = new_name
                self.contacts[new_name] = contact
            elif choice == "last_name":
                contact.last_name = input("Enter new last name: ")
            elif choice == "address":
                contact.address = input("Enter new address: ")
            elif choice == "city":
                contact.city = input("Enter new city: ")
            elif choice == "state":
                contact.state = input("Enter new state: ")
            elif choice == "zip_code":
                contact.zip_code = input("Enter new zip code: ")
            elif choice == "phone_number":
                contact.phone_number = input("Enter new phone number: ")
            elif choice == "email":
                contact.email = input("Enter new email: ")
            else:
                print("Invalid choice.")
        else:
            print("Contact not found.")

    # Add multiple contacts
    def add_multiple_contacts(self, *contacts):
        for contact in contacts:
            self.add_contact(contact)

    # Delete a contact by first name
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # Search contacts by state or city
    def search_by_city_or_state(self, location):
        results = []
        for contact in self.contacts.values():
            if contact.city == location or contact.state == location:
                results.append(contact)
        return results

    # Sort helpers
    def sort_by_name(self):
        return sorted(self.contacts.values(), key=lambda x: x.first_name)

    def sort_by_city(self):
        return sorted(self.contacts.values(), key=lambda x: x.city)

    def sort_by_state(self):
        return sorted(self.contacts.values(), key=lambda x: x.state)

    def sort_by_zip(self):
        return sorted(self.contacts.values(), key=lambda x: x.zip_code)

    # Show contacts in a city or state
    def show_by_city_or_state(self, location):
        results = self.search_by_city_or_state(location)
        if results:
            print(f"Contacts in {location}:")
            for contact in results:
                print(f"{contact.first_name} {contact.last_name}")
        else:
            print(f"No contacts found in {location}.")

    # Count contacts in a city or state
    def count_by_city_or_state(self, location):
        results = self.search_by_city_or_state(location)
        return len(results)

    # Display all contacts
    def display_contacts(self):
        if not self.contacts:
            print("No contacts in this address book.")
            return

        print("Contacts:")
        for contact in self.sort_by_name():
            print(contact)

