contacts = []
n = int(input("Enter number of contacts: "))
for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts.append({"name": name, "phone": phone})
with open("contacts.txt", "w") as file:
    for c in contacts:
        file.write(c["name"] + "," + c["phone"] + "\n")
print("Contacts saved successfully")
with open("contacts.txt", "r") as file:
    print("\nSaved Contacts:")
    print(file.read())