class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(self.title, "has been borrowed successfully")
        else:
             print(self.title, "is already borrowed")

    def return_book(self):
            if self.is_borrowed:
                self.is_borrowed = False
                print(self.title, "has been returned successfully")
            else:
                 print(self.title, "is already returned")

#CREATINGGGG OBJECTTTTTTTT
book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("The Odyssey", "Homer")
book3 = Book("Frankenstein ", "Mary Shelley")

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book()
book3.return_book()
