password = input("Enter password: ")
while len(password) < 8:
    print("Password must contain at least 8 characters")
    password = input("Enter password again: ")
encrypted = ""
for c in password:
    encrypted += chr(ord(c) + 3)
with open("password.txt", "w") as file:
    file.write(encrypted)
print("Password is valid")
print("Encrypted Password:", encrypted)
print("Saved in password.txt")