# Define a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone Number: {info['phone_number']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")
        print("-" * 20)

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term in (name, info['phone_number']):
            print(f"Name: {name}")
            print(f"Phone Number: {info['phone_number']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Enter new contact information:")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main loop
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
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please select a valid option.")
