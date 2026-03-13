class AddressBook:

    def __init__(self):
        self.contacts = {}

    ##To add Contact to the book
    def add_contact(self, contact):

        if contact not in self.contacts:
            self.contacts[contact.first_name] = contact
            print("Contact added successfully.")
        else:
            print("Contact already exists.")
    ## to edit the contact
    def edit_contact(self,name):
        if name in self.contacts:
            contact = self.contacts[name]
            print("Editing contact:", contact)
            choice = input("Enter the field you want to edit (first_name, last_name, address, city, state, zip_code, phone_number, email): ")
            match choice:
                case "first_name":
                    contact.first_name = input("Enter new first name: ")
                case "last_name":
                    contact.last_name = input("Enter new last name: ")
                case "address":
                    contact.address = input("Enter new address: ")
                case "city":
                    contact.city = input("Enter new city: ")
                case "state":
                    contact.state = input("Enter new state: ")
                case "zip_code":
                    contact.zip_code = input("Enter new zip code: ")
                case "phone_number":
                    contact.phone_number = input("Enter new phone number: ")
                case "email":
                    contact.email = input("Enter new email: ")
                case _:
                    print("Invalid choice.")
            
        else:
            print("Contact not found.")

    ## Adding multiple user to the contact
    def add_multiple_contacts(self, *contacts):
        for contact in contacts:
            self.add_contact(contact)

    ## deleting the contact by name
    def delete_contact(self,name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    ##Searching contacts by state or city
    def search_by_city_or_state(self, location):
        results = []
        for contact in self.contacts.values():
            if contact.city == location or contact.state == location:
                results.append(contact)
        return results
    
    

            