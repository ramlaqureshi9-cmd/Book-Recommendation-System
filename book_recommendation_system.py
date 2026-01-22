# =========================
# BOOK RECOMMENDATION SYSTEM
# =========================

import pickle

# -------------------------
# Book Class
# -------------------------
class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author} ({self.genre})"


# -------------------------
# BST Node
# -------------------------
class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


# -------------------------
# Binary Search Tree
# -------------------------
class BookBST:
    def insert(self, root, book):
        if root is None:
            return BSTNode(book)
        if book.title.lower() < root.book.title.lower():
            root.left = self.insert(root.left, book)
        else:
            root.right = self.insert(root.right, book)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.book)
            self.inorder(root.right)


# -------------------------
# Stack (Recently Viewed)
# -------------------------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, book):
        self.items.append(book)

    def display(self):
        if not self.items:
            print("No recently viewed books.")
        else:
            print("\nRecently Viewed Books:")
            for book in reversed(self.items):
                print(book)


# -------------------------
# Main System
# -------------------------
class BookSystem:
    def __init__(self):
        self.book_table = {}      # Hash Table
        self.bst = BookBST()
        self.bst_root = None
        self.recent_stack = Stack()

    def insert_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")

        book = Book(book_id, title, author, genre)
        self.book_table[book_id] = book
        self.bst_root = self.bst.insert(self.bst_root, book)

        print("Book inserted successfully!")

    def search_book(self):
        book_id = input("Enter Book ID to search: ")
        book = self.book_table.get(book_id)

        if book:
            print("Book Found:", book)
            self.recent_stack.push(book)
        else:
            print("Book not found.")

    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")
        if book_id in self.book_table:
            del self.book_table[book_id]
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    def display_books(self):
        if self.bst_root is None:
            print("No books available.")
        else:
            print("\nBooks (Sorted by Title):")
            self.bst.inorder(self.bst_root)

    def save_to_file(self):
        with open("books.dat", "wb") as file:
            pickle.dump(self.book_table, file)
        print("Data saved to file.")

    def load_from_file(self):
        try:
            with open("books.dat", "rb") as file:
                self.book_table = pickle.load(file)

            self.bst_root = None
            for book in self.book_table.values():
                self.bst_root = self.bst.insert(self.bst_root, book)

            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved file found.")

    def show_recent(self):
        self.recent_stack.display()


# -------------------------
# Menu Interface
# -------------------------
def menu():
    system = BookSystem()
    system.load_from_file()

    while True:
        print("\n===== BOOK RECOMMENDATION SYSTEM =====")
        print("1. Insert Book")
        print("2. Search Book")
        print("3. Delete Book")
        print("4. Display All Books")
        print("5. Recently Viewed Books")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.insert_book()
        elif choice == "2":
            system.search_book()
        elif choice == "3":
            system.delete_book()
        elif choice == "4":
            system.display_books()
        elif choice == "5":
            system.show_recent()
        elif choice == "6":
            system.save_to_file()
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


# -------------------------
# Run Program
# -------------------------
menu()
