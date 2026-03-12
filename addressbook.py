class AddressBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):

        if contact not in self.contacts:
            self.contacts.append(contact)
            print("Contact added successfully.")
        else:
            print("Contact already exists.")
            