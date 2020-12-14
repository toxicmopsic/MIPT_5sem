class Library:
    @classmethod
    def __init__(self, name):
        self.name = name
        self.books = {}

    def __str__(self):
        result = []
        for book in self.books.values():
            result.append(f'Book: {str(book[0])}, Quantity: {str(book[1])}')
        return str(self.name) + ':\n' + str(result)

    def info(self, name=None, ISBN=None):
        if ISBN:
            book = self.books.get(ISBN)
            if book:
                return book[0]
            return None
        elif name:
            for book in self.books.items():
                if name == book[1][0].name:
                    return book[1][0]
            return None
        return None

    def add(self, book):
        ISBN = book.ISBN
        if ISBN in self.books:
            self.books[ISBN][1] += 1
        else:
            self.books[ISBN] = [book, 1]

    def pop(self, ISBN):
        book = self.books.get(ISBN)
        if book:
            book[1] -= 1
            if not book[1]:
                self.books.pop(ISBN)
            return book[0]

    def find(self, author):
        result = []
        for item in self.books.values():
            book = item[0]
            if author == book.author:
                result.append(book.name)
        return result


class Book:
    def __init__(self, name, author, publisher, release_date, ISBN):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.release_date = release_date
        self.ISBN = ISBN

    def __str__(self):
         return f'{self.name}, {self.author}, {self.publisher}, {self.release_date}, {self.ISBN}'


def test_library():
    library = Library('LENIN')
    assert library.name == 'LENIN'

    book1 = Book('Война и мир', 'Толстой Л.', 'АСТ', 2000, 11111)
    book2 = Book('Анна Каренина', 'Толстой Л.', 'АСТ', 2010, 22222)
    book3 = Book('Севастопольские рассказы', 'Толстой Л.', 'АСТ', 2020, 33333)

    library.add(book1)
    library.add(book2)
    library.add(book3)

    info1 = library.info(ISBN=11111)
    info2 = library.info(name='Анна Каренина')
    info3 = library.info(name='Севастопольские рассказы')
    print(info1)
    print(info2)
    print(info3, '\n')

    print(library.find('Толстой Л.'), '\n')

    print(library)
    library.pop(info1.ISBN)
    library.pop(info2.ISBN)
    library.pop(info3.ISBN)
    print(library)
    assert len(library.books) == 0

if name == '__main__':
    test_library()
