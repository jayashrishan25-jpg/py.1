class Book:
    def __init__(self, title):
        self.title = title
        self.available = True
    def issue(self):
        if self.available:
            self.available = False
            print(self.title, "issued")
        else:
            print("Book not available")
    def return_book(self):
        self.available = True
        print(self.title, "returned")
book = Book("Python Programming")
book.issue()
book.return_book()