class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True


class Member:

    def __init__(self, name):
        self.name = name
        self.issued_books = []


class Library:

    def __init__(self):
        self.book_list = []
        self.member_list = []

    def add_book(self, book):
        self.book_list.append(book)
        print("Book Added:", book.title)

    def add_member(self, member):
        self.member_list.append(member)
        print("Member Registered:", member.name)

    def issue_book(self, member, book):

        if book.is_available:
            book.is_available = False
            member.issued_books.append(book)
            print(book.title, "issued to", member.name)
        else:
            print(book.title, "is already issued.")

    def submit_book(self, member, book):

        if book in member.issued_books:
            member.issued_books.remove(book)
            book.is_available = True
            print(book.title, "returned by", member.name)
        else:
            print(member.name, "has not borrowed this book.")


library = Library()

book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("Java Programming", "James Gosling")
book3 = Book("C Programming", "Dennis Ritchie")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print()

member1 = Member("Rahul")
member2 = Member("Priya")

library.add_member(member1)
library.add_member(member2)

print()

library.issue_book(member1, book1)
library.issue_book(member2, book2)

print()

library.issue_book(member2, book1)

print()

library.submit_book(member1, book1)

print()

library.issue_book(member2, book1)

print("\n===== Library Report =====")

print("\nBook Status:")
for book in library.book_list:
    print(book.title, ":", book.is_available)

print("\nMember Records:")
for member in library.member_list:
    print("\n", member.name)

    if member.issued_books:
        for book in member.issued_books:
            print("-", book.title)
    else:
        print("No books issued.")