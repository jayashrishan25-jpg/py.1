class Book:
    def __init__(self, title):
        self.title = title
class User:
    def __init__(self, name):
        self.name = name
    def issue_book(self, book):
        print(self.name, "issued", book.title)
book = Book("Data Structures")
user = User("Jayashri")
user.issue_book(book)