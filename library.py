library = []
{
    'title': ... ,
    'author': ... ,
    'is_available': True
}

def main():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.append({"title": title, "author": author})
            print("Book added successfully!")

        elif choice == "2":
            if not library:
                print("Library is empty!")
            else:
                print("\n--- Book List ---")
                for i, book in enumerate(library, 1):
                    print(f"{i}. {book['title']} - {book['author']}")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")

def add_book():
    """Prompt user for book info and append to library list."""
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    new_book = {
        'title': title,
        'author': author,
        'is_available': True
    }

    library.append(new_book)
    print("Book added successfully!")
    

def main():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Exits")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            if not library:
                print("Library is empty!")
            else:
                print("\n--- Book List ---")
                for i, book in enumerate(library, 1):
                    print(f"{i}. {book['title']} - {book['author']} (Available: {book['is_available']})")

        elif choice == "4":
            print("Exiting...")
            break
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()

        else:
            print("Invalid option. Try again.")
def view_books():
    if not library:
        print("Library is empty!")
    else:
        print("\n--- Book List ---")
        for i, book in enumerate(library, 1):
            title = book['title']
            author = book['author']
            available = "Yes" if book['is_available'] else "No"
            print(f"{i}. Title: {title} | Author: {author} | Available: {available}")

def search_book():
    query = input("Enter keyword to search: ").lower()

    found = False
    print("\n--- Search Results ---")

    for book in library:
        if query in book['title'].lower():  # case-insensitive search
            found = True
            available = "Yes" if book["is_available"] else "No"
            print(f"Title: {book['title']} | Author: {book['author']} | Available: {available}")

    if not found:
        print("No matching books found.")
if __name__ == "__main__":
    main()