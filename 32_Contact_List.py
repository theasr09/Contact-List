
contacts = {}

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"{name} has been added to your contacts.")

def view_contact(name):
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"{name} not found in contacts.")

def edit_contact(name):
    if name in contacts:
        contact = contacts[name]
        print("Current Details:")
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        
        phone = input("Enter new phone number (press Enter to keep current): ")
        email = input("Enter new email address (press Enter to keep current): ")
        
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        
        print(f"{name}'s contact information has been updated.")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from contacts.")
    else:
        print(f"{name} not found in contacts.")

def list_contacts():
    print("Contacts:")
    for name in contacts:
        print(name)

def main():
    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Quit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            name = input("Enter the name to view: ")
            view_contact(name)
        elif choice == '3':
            name = input("Enter the name to edit: ")
            edit_contact(name)
        elif choice == '4':
            name = input("Enter the name to delete: ")
            delete_contact(name)
        elif choice == '5':
            list_contacts()
        elif choice == '6':
            print("Exiting the contact list.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()
