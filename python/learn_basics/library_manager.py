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
        
        choice = input("\nChoose an option: ")
        
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
   title = input("Enter book title:")
   author = input ("Enter author name:")
   year = input("Enter publication year:")
   update = input("Read or Not Read")
   rate = input("Rate from 1 to 5")
   
   library[title] = {
    'author': author,
    'year': year,
    'update': update,
    'rate':rate,
}
   print(f"{title} added to library")


def remove_book():
    title = input("Enter book you want to delete")

    #verify that book title is in the library
    if title in library:
        del library[title]
        print("You have deleted this book")
    else:
        print("book not found!")
        main()

def update_book():
    title = input("Enter book title:")
    update = input("Read or not Read?")
    
    if title in library:
        print("This book exists! Do you want to update it? (yes or no)")
        answer = input("yes or no")

        if answer == "yes":
            library[title]['update'] = update
            print("book has been updated")
        else:
            print("Ok have a good day!")
            main()
    else:
        print("This book does not exist!")
        main()


def rate_book():
    title = input("Enter book title:")
    rate = input ("rate from 1 to 5")

    if title in library:
        print("This book exists! Do you want to update your rating")
        answer = input("yes or no")
        
        if answer == "yes":
            while True:
                try: 
                    change_rate = int(input("Rate book from 1 to 5"))
                    library[title]['rate'] = change_rate
                    print ("Book has been updated")
                    break
                except ValueError:
                    print ("This is not a number")

        else:
            print("Ok have a good day!")
            main()
    else:
        print ("book does not exist")
        main()

def search_book():
    title = input("Enter book title:")

    if title in library:
        print(library[title])

    elif title not in library:
        print("this book does not exist, would you like to add it?")
        answer = input("yes or no?")
        if answer == "yes":
            add_book()
        else:
            print("Ok, no problem!")
            main()

def list_all_books():
    if len(library) == 0:
        print("Your Library is empty!")
        main()
    
    for title in library:
            print(title)

if __name__ == "__main__":
    print("Welcome to Personal Library Manager!")
    main()