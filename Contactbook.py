class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        """Add a new contact to the contact book."""
        if phone in self.contacts:
            print("Contact with this phone number already exists.")
        else:
            self.contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'address': address}
            print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """Display all contacts in the contact book."""
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for contact in self.contacts.values():
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, query):
        """Search for a contact by name or phone number."""
        found = False
        for contact in self.contacts.values():
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
                found = True
        if not found:
            print("No matching contact found.")

    def update_contact(self, phone, name=None, email=None, address=None):
        """Update details of an existing contact."""
        if phone in self.contacts:
            contact = self.contacts[phone]
            if name:
                contact['name'] = name
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, phone):
        """Delete a contact by phone number."""
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == '4':
            phone = input("Enter phone number of the contact to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(phone, name, email, address)

        elif choice == '5':
            phone = input("Enter phone number of the contact to delete: ")
            contact_book.delete_contact(phone)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
