import csv

class FileIO:

    @staticmethod
    def write_to_txt(contacts,filename='contacts.txt'):

        with open(filename,'w') as file:
            for contact in contacts.values():

                line= f"{contact.first_name},{contact.last_name},{contact.address},{contact.city},{contact.state},{contact.zip_code},{contact.phone_number},{contact.email}\n"
                file.write(line)

        print('Contacts written to txt file successfully')

    @staticmethod
    def read_from_txt(filename='contacts.txt'):
        contact=[]

        with open(filename,'r') as file:
            for line in file:
                data=line.strip().split(",")
                contact.append(data)

        return contact
    

    ## writing to csv file 
    @staticmethod
    def write_to_csv(contacts,filename='contacts.txt'):
        
        with open(filename,'w') as file:
            writer=csv.writer(file)

            writer.writerow(
                ["First Name","Last Name","Address","City","State","Zip","Phone","Email"]
            )

            for contact in contacts.values():
                  writer.writerow([
                    contact.first_name,
                    contact.last_name,
                    contact.address,
                    contact.city,
                    contact.state,
                    contact.zip_code,
                    contact.phone_number,
                    contact.email
                ])
                  
        print('Contacts written to csv file successfully')

    @staticmethod
    def read_from_csv(filename="contacts.csv"):

        contacts = []

        with open(filename, "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:
                contacts.append(row)

        return contacts

    
    

