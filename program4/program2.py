contacts = []
for i in range(3):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts.append({"name": name, "phone": phone})
search = input("Enter name to search: ")
for c in contacts:
    if c["name"].lower() == search.lower():
        print("Name:", c["name"])
        print("Phone:", c["phone"])
        break
else:
    print("Contact not found")