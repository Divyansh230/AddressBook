import csv
import json

from models.contact import Contact


class FileIO:
    
    @staticmethod
    def write_to_txt(contacts, filename="contacts.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for contact in contacts.values():
                line = (
                    f"{contact.first_name},{contact.last_name},"
                    f"{contact.address},{contact.city},{contact.state},"
                    f"{contact.zip_code},{contact.phone_number},{contact.email}\n"
                )
                file.write(line)
        print("Contacts written to txt file successfully")

    @staticmethod
    def read_from_txt(filename="contacts.txt"):
        contacts = []
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")
                contacts.append(data)
        return contacts

    @staticmethod
    def write_to_csv(contacts, filename="contacts.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "First Name",
                    "Last Name",
                    "Address",
                    "City",
                    "State",
                    "Zip",
                    "Phone",
                    "Email",
                ]
            )
            for contact in contacts.values():
                writer.writerow(
                    [
                        contact.first_name,
                        contact.last_name,
                        contact.address,
                        contact.city,
                        contact.state,
                        contact.zip_code,
                        contact.phone_number,
                        contact.email,
                    ]
                )
        print("Contacts written to csv file successfully")

    @staticmethod
    def read_from_csv(filename="contacts.csv"):
        contacts = []
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            # Skip header
            next(reader, None)
            for row in reader:
                contacts.append(row)
        return contacts

    @staticmethod
    def write_to_json(contacts, filename="contacts.json"):
        data = []
        for contact in contacts.values():
            data.append(
                {
                    "first_name": contact.first_name,
                    "last_name": contact.last_name,
                    "address": contact.address,
                    "city": contact.city,
                    "state": contact.state,
                    "zip_code": contact.zip_code,
                    "phone_number": contact.phone_number,
                    "email": contact.email,
                }
            )
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Contacts written to json file successfully")

    @staticmethod
    def read_from_json(filename="contacts.json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

