class Book:
    def show(self):
        print("This is a book")
class TextBook(Book):
    def show(self):
        print("This is a Text Book")
class ReferenceBook(Book):
    def show(self):
        print("This is a Reference Book")
b1 = TextBook()
b2 = ReferenceBook()
b1.show()
b2.show()