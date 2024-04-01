# Catalog of books
books = {
    1: ["Book 1", "Author 1", 3],
    2: ["Book 2", "Author 2", 2],
    3: ["Book 3", "Author 3", 1]
}

# User records
users = {}

# Book transactions
transactions = {}

def register_user():
    name = input("Enter your name: ")
    user_id = len(users) + 1
    users[user_id] = {"name": name, "books": []}
    print(f"Welcome, {name}! Your user ID is {user_id}.")
    return user_id

def display_catalog():
    print("Available Books:")
    for book_id, book_info in books.items():
        title, author, quantity = book_info
        print(f"ID: {book_id}, Title: {title}, Author: {author}, Quantity: {quantity}")

def checkout_book(user_id):
    book_id = int(input("Enter the book ID you want to check out: "))
    if book_id not in books:
        print("Invalid book ID.")
        return

    title, author, quantity = books[book_id]
    if quantity == 0:
        print("Sorry, this book is not available currently.")
        return

    if len(users[user_id]["books"]) >= 3:
        print("You have already checked out the maximum number of books allowed (3).")
        return

    books[book_id][2] -= 1  # Decrease the quantity
    users[user_id]["books"].append(book_id)
    transactions[book_id] = transactions.get(book_id, []) + [user_id]
    print(f"You have checked out '{title}' by {author}. It is due in 14 days.")

def return_book(user_id):
    book_id = int(input("Enter the book ID you want to return: "))
    if book_id not in books:
        print("Invalid book ID.")
        return

    if book_id not in users[user_id]["books"]:
        print("You haven't checked out this book.")
        return

    title, author, _ = books[book_id]
    books[book_id][2] += 1  # Increase the quantity
    users[user_id]["books"].remove(book_id)
    transactions[book_id].remove(user_id)
    print(f"You have returned '{title}' by {author}.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Register User")
        print("2. Display Catalog")
        print("3. Check Out Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            user_id = register_user()
        elif choice == "2":
            display_catalog()
        elif choice == "3":
            if not users:
                print("Please register a user first.")
            else:
                user_id = int(input("Enter your user ID: "))
                if user_id not in users:
                    print("Invalid user ID.")
                else:
                    checkout_book(user_id)
        elif choice == "4":
            if not users:
                print("Please register a user first.")
            else:
                user_id = int(input("Enter your user ID: "))
                if user_id not in users:
                    print("Invalid user ID.")
                else:
                    return_book(user_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()