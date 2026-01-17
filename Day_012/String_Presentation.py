class Book:
    def __str__(self): return "Readable Title for Users"
    def __repr__(self): return "Book(id = 101, title = 'Code')"

book = Book()
print(book)
print(repr(book))