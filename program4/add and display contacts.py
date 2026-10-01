contacts = []
name = input("Enter name: ")
phone = input("Enter phone: ")
contact = {"name": name, "phone": phone}
contacts.append(contact)
print("\nContact Details:")
for c in contacts:
    print(c["name"], "-", c["phone"])