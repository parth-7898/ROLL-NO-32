class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = True

    def show_book(self):
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"

        print(f"Book ID : {self.id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-" * 30)


class Member:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name
        self.books = []

    def show_member(self):
        print(f"Member ID : {self.id}")
        print(f"Name      : {self.name}")
        if self.books:
            print("Borrowed Books :", ", ".join(self.books))
        else:
            print("Borrowed Books : None")
        print("-" * 30)


class Library:
    def __init__(self):
        self.book_list = []
        self.member_list = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        self.book_list.append(Book(book_id, title, author))
        print("Book Added Successfully.\n")

    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        self.member_list.append(Member(member_id, name))
        print("Member Registered Successfully.\n")

    def borrow_book(self):
        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")

        member = None
        book = None

        for m in self.member_list:
            if m.id == member_id:
                member = m
                break

        for b in self.book_list:
            if b.id == book_id:
                book = b
                break

        if member is None:
            print("Member not found.\n")
            return

        if book is None:
            print("Book not found.\n")
            return

        if not book.available:
            print("Book already borrowed.\n")
            return

        book.available = False
        member.books.append(book.title)
        print(f"{member.name} borrowed '{book.title}'.\n")

    def return_book(self):
        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")

        member = None
        book = None

        for m in self.member_list:
            if m.id == member_id:
                member = m
                break

        for b in self.book_list:
            if b.id == book_id:
                book = b
                break

        if member is None or book is None:
            print("Invalid ID.\n")
            return

        if book.title in member.books:
            member.books.remove(book.title)
            book.available = True
            print("Book Returned Successfully.\n")
        else:
            print("This member did not borrow this book.\n")

    def show_books(self):
        if not self.book_list:
            print("No Books Available.\n")
            return

        print("\nLibrary Books")
        print("=" * 30)

        for b in self.book_list:
            b.show_book()

    def show_members(self):
        if not self.member_list:
            print("No Members Registered.\n")
            return

        print("\nLibrary Members")
        print("=" * 30)

        for m in self.member_list:
            m.show_member()


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Books")
    print("6. Show Members")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.add_member()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.show_books()

    elif choice == "6":
        library.show_members()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")