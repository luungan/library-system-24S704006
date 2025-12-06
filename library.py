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
        print("3. Exit")

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

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()