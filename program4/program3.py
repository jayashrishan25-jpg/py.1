contacts = [
    {"name": "Arun", "phone": "9876543210"},
    {"name": "Priya", "phone": "9876501234"},
    {"name": "Kavi", "phone": "9876512345"}
]
name = input("Enter name to delete: ")
for c in contacts:
    if c["name"].lower() == name.lower():
        contacts.remove(c)
        print("Contact deleted")
        break
else:
    print("Contact not found")
print("\nContacts:")
for c in contacts:
    print(c)