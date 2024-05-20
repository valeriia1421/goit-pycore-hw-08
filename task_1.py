# task_1

import pickle

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, address, phone):
        contact = {
            "name": name,
            "address": address,
            "phone": phone
        }
        self.contacts.append(contact)

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Address: {contact['address']}, Phone: {contact['phone']}")

    def save_data(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load_data(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

def main():
    address_book = AddressBook.load_data()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            address_book.add_contact(name, address, phone)
        elif choice == "2":
            address_book.list_contacts()
        elif choice == "3":
            address_book.save_data()
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()