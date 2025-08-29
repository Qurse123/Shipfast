#!/usr/bin/env python3
"""
Personal Library Manager
Build your own book tracking system!
"""

library = {}

def main():
    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add book")
        print("2. Search book")
        print("3. Update book")
        print("4. Rate book")
        print("5. Remove book")
        print("6. List all books")
        print("0. Exit")
        
        try:
            choice = input("\nChoose an option: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        
        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            rate_book()
        elif choice == "5":
            remove_book()
        elif choice == "6":
            list_all_books()
        elif choice == "0":
            print("Thanks for using Personal Library Manager!")
            break
        else:
            print("Invalid option. Please choose 0-6.")

def add_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        update = input("Read or Not Read: ")
        rate = input("Rate from 1 to 5: ")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")
        return
   
    
    library[title] = {
        'author': author,
        'year': year,
        'update': update,
        'rate': rate,
    }
    print(f"{title} added to library")


def remove_book():
    try:
        title = input("Enter book you want to delete: ")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")
        return

    # verify that book title is in the library
    if title in library:
        del library[title]
        print("You have deleted this book")
    else:
        print("Book not found!")

def update_book():
    try:
        title = input("Enter book title: ")
        update = input("Read or not Read? ")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")
        return
    
    if title in library:
        print("This book exists! Do you want to update it? (yes or no)")
        try:
            answer = input("yes or no: ")
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return

        if answer == "yes":
            library[title]['update'] = update
            print("Book has been updated")
        else:
            print("Ok have a good day!")
    else:
        print("This book does not exist!")


def rate_book():
    try:
        title = input("Enter book title: ")
        rate = input("Rate from 1 to 5: ")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")
        return

    if title in library:
        print("This book exists! Do you want to update your rating?")
        try:
            answer = input("yes or no: ")
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return
        
        if answer == "yes":
            while True:
                try: 
                    change_rate = int(input("Rate book from 1 to 5: "))
                    if 1 <= change_rate <= 5:
                        library[title]['rate'] = str(change_rate)
                        print("Book has been updated")
                        break
                    else:
                        print("Please enter a number between 1 and 5")
                except ValueError:
                    print("This is not a number")
                except (EOFError, KeyboardInterrupt):
                    print("\nOperation cancelled.")
                    return
        else:
            print("Ok have a good day!")
    else:
        print("Book does not exist")

def search_book():
    try:
        title = input("Enter book title: ")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")
        return

    if title in library:
        book_info = library[title]
        print(f"\nBook found:")
        print(f"Title: {title}")
        print(f"Author: {book_info['author']}")
        print(f"Year: {book_info['year']}")
        print(f"Status: {book_info['update']}")
        print(f"Rating: {book_info['rate']}")
    else:
        print("This book does not exist, would you like to add it?")
        try:
            answer = input("yes or no? ")
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return
            
        if answer == "yes":
            add_book()
        else:
            print("Ok, no problem!")

def list_all_books():
    if len(library) == 0:
        print("Your Library is empty!")
    else:
        print("\nYour Library:")
        print("-" * 50)
        for title in library:
            book_info = library[title]
            print(f"Title: {title}")
            print(f"Author: {book_info['author']}")
            print(f"Year: {book_info['year']}")
            print(f"Status: {book_info['update']}")
            print(f"Rating: {book_info['rate']}")
            print("-" * 50)

def filter_books():
    try:
        title = input("Enter book title: ")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")
        return
        
    if title not in library:
        print("This book does not exist, would you like to add it?")
        try:
            answer = input("yes or no? ")
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return
            
        if answer == "yes":
            add_book()
    else:
        print("What would you like to filter by?")
        try:
            filter_type = input("rating or author: ")
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return
            
        if filter_type == "rating":
            try:
                desired_rating = input("What rating do you want to filter by (1-5): ")
            except (EOFError, KeyboardInterrupt):
                print("\nOperation cancelled.")
                return
                
            print(f"\nBooks with {desired_rating} star rating:")
            found_books = False

            for title in library:
                if library[title]['rate'] == desired_rating:
                    print(f"- {title}")
                    found_books = True
            
            if not found_books:
                print("No books found with that rating.")

if __name__ == "__main__":
    print("Welcome to Personal Library Manager!")
    main()