class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books {book_id: [title, author, status]}
        self.members = {}  # Dictionary to store members {member_id: [name, books_borrowed]}
        self.book_id_counter = 1
        self.member_id_counter = 1

    def add_book(self, title, author):
        """Add a new book to the library"""
        self.books[self.book_id_counter] = [title, author, "Available"]
        print(f"Book added successfully with ID: {self.book_id_counter}")
        self.book_id_counter += 1

    def add_member(self, name):
        """Add a new member to the library"""
        self.members[self.member_id_counter] = [name, []]
        print(f"Member added successfully with ID: {self.member_id_counter}")
        self.member_id_counter += 1
    def display_books(self):
        """Display all books in the library"""
        print("\nLibrary Books:")
        print("ID\tTitle\tAuthor\tStatus")
        print("-" * 40)
        for book_id, details in self.books.items():
            print(f"{book_id}\t{details[0]}\t{details[1]}\t{details[2]}")

    def display_members(self):
        """Display all library members"""
        print("\nLibrary Members:")
        print("ID\tName\tBooks Borrowed")
        print("-" * 40)
        for member_id, details in self.members.items():
            print(f"{member_id}\t{details[0]}\t{details[1]}")

    def borrow_book(self, member_id, book_id):
        """Allow member to borrow a book"""
        if book_id not in self.books or member_id not in self.members:
            print("Invalid book ID or member ID")
            return
        
        if self.books[book_id][2] != "Available":
            print("Book is not available for borrowing")
            return

        if len(self.members[member_id][1]) >= 3:
            print("Member has already borrowed maximum number of books")
            return

        self.books[book_id][2] = "Borrowed"
        self.members[member_id][1].append(book_id)
        print("Book borrowed successfully")

    def return_book(self, member_id, book_id):
        """Allow member to return a book"""
        if book_id not in self.books or member_id not in self.members:
            print("Invalid book ID or member ID")
            return

        if book_id not in self.members[member_id][1]:
            print("This book was not borrowed by this member")
            return

        self.books[book_id][2] = "Available"
        self.members[member_id][1].remove(book_id)
        print("Book returned successfully")


def main():
    lib = Library()
    
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Display Books")
        print("4. Display Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            lib.add_book(title, author)
            
        elif choice == '2':
            name = input("Enter member name: ")
            lib.add_member(name)
            
        elif choice == '3':
            lib.display_books()
            
        elif choice == '4':
            lib.display_members()
            
        elif choice == '5':
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            lib.borrow_book(member_id, book_id)
            
        elif choice == '6':
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            lib.return_book(member_id, book_id)
            
        elif choice == '7':
            print("Thank you for using the Library Management System!")
            break
            
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
