# Contact book dictionary
contact_book = {}

# Function to validate email
def is_valid_email(email):
    return "@" in email and "." in email

# Function to add a new contact
def add_contact(name, phone, email):
    name = name.title()
    if name in contact_book:
        print(" Contact already exists.")
        return
    if not is_valid_email(email):
        print(" Invalid email format.")
        return
    contact_book[name] = {"phone": phone, "email": email}
    print(f" Contact '{name}' added.")

# Function to update existing contact
def update_contact(name, phone, email):
    name = name.title()
    if name not in contact_book:
        print(" Contact does not exist.")
        return
    if not is_valid_email(email):
        print(" Invalid email format.")
        return
    contact_book[name] = {"phone": phone, "email": email}
    print(f" Contact '{name}' updated.")

# Function to retrieve a contact
def get_contact(name):
    name = name.title()
    if name in contact_book:
        print(f"{name} - Phone: {contact_book[name]['phone']}, Email: {contact_book[name]['email']}")
    else:
        print(" Contact not found.")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("📭 No contacts available.")
    else:
        print("\nContact List:")
        for name, info in contact_book.items():
            print(f"- {name}: Phone: {info['phone']}, Email: {info['email']}")

# Main loop
while True:
    print("\n Contact Book Menu:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Retrieve Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)

    elif choice == "2":
        name = input("Enter name to update: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        update_contact(name, phone, email)

    elif choice == "3":
        name = input("Enter name to search: ")
        get_contact(name)

    elif choice == "4":
        view_contacts()

    elif choice == "5":
        print(" Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
