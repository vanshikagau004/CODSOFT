import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact."""
    contacts = load_contacts()
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    """View all contacts."""
    contacts = load_contacts()
    if contacts:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
    else:
        print("No contacts found.")

def search_contacts():
    """Search for a contact by name or phone number."""
    contacts = load_contacts()
    query = input("Enter name or phone number to search: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("No matching contacts found.")

def update_contact():
    """Update an existing contact."""
    contacts = load_contacts()
    name = input("Enter the name of the contact to update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Leave a field blank to keep it unchanged.")
            new_name = input(f"New name [{contact['name']}]: ").strip()
            new_phone = input(f"New phone [{contact['phone']}]: ").strip()
            new_email = input(f"New email [{contact['email']}]: ").strip()
            new_address = input(f"New address [{contact['address']}]: ").strip()
            contact['name'] = new_name or contact['name']
            contact['phone'] = new_phone or contact['phone']
            contact['email'] = new_email or contact['email']
            contact['address'] = new_address or contact['address']
            save_contacts(contacts)
            print(f"Contact '{contact['name']}' updated successfully.")
            return
    print(f"Contact '{name}' not found.")

def delete_contact():
    """Delete a contact."""
    contacts = load_contacts()
    name = input("Enter the name of the contact to delete: ").strip()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            confirm = input(f"Are you sure you want to delete '{contact['name']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                contacts.pop(i)
                save_contacts(contacts)
                print(f"Contact '{contact['name']}' deleted successfully.")
            else:
                print("Deletion canceled.")
            return
    print(f"Contact '{name}' not found.")

def main():
    """Main function to run the contact management system."""
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
