print("Welcome to your personal Library Manager!")

# List to store all the books as dictionaries
items = []

# Start of the infinite loop that presents the menu to the user
while True:
    # Menu options for the user
    print("1. Add a Book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

    # Taking input from the user, handling invalid input with try-except block
    try:
        choice = int(input("\nEnter your choice (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        continue  # If input is invalid, we prompt the user again

    # Matching user's choice with the appropriate action using 'match' statement
    match choice:
        case 1:
            print("Adding a book...")
            
            # Taking inputs for book details
            Book_title = input("Enter the book title: ")
            Book_author = input("Enter the author: ")
            Book_year = input("Enter the publication year: ")
            Book_genre = input("Enter the genre: ")
            read = input("Have you read this book? (yes/no): ")

            # Creating a dictionary to represent a book
            book = {
                "title": Book_title,
                "author": Book_author,
                "year": Book_year,
                "genre": Book_genre,
                "read": read
            }
            
            # Appending the book dictionary to the 'items' list
            items.append(book)
            print("Book added successfully!")

        case 2:
            print("Removing a book...")

            # Asking user to input the title of the book they want to remove
            remove_book = input("Enter the title of the book to remove: ")

            # Filtering the books list to find the book that matches the input title (case insensitive)
            filtered_books = list(filter(lambda book: book["title"].lower() == remove_book.lower(), items))

            # If the book is found, it will be removed from the 'items' list
            if filtered_books:
                book_to_remove = filtered_books[0]  # Getting the first matching book
                items.remove(book_to_remove)  # Removing the book from the list
                print(f"The Book '{remove_book}' has been removed")
            else:
                # If no book is found, show an error message
                print("Book not found!")

        case 3:
            print("Searching for a book...")
            
            while True:
                print("1. Title")
                print("2. Author")

                try:
                    choice = int(input("\nEnter your choice (1 or 2): "))
                except ValueError:
                    print("Invalid input! Please enter a number 1 or 2.")
                    continue

                # Search by title
                if choice == 1:
                    search_term = input("Enter the title to search for: ").lower()
                    # Using filter to find books that contain the search term in the title
                    filtered_books = list(filter(lambda book: search_term in book["title"].lower(), items))
                    
                    # If matching books are found, display them
                    if filtered_books:
                        for book in filtered_books:
                            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")
                    else:
                        print("No books found with that title.")
                    break  # Exit the search loop after searching by title

                # Search by author
                elif choice == 2:
                    search_term = input("Enter the author to search for: ").lower()
                    # Using filter to find books by the given author
                    filtered_books = list(filter(lambda book: search_term in book["author"].lower(), items))
                    
                    # If matching books are found, display them
                    if filtered_books:
                        for book in filtered_books:
                            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")
                    else:
                        print("No books found by that author.")
                    break  # Exit the search loop after searching by author

                else:
                    print("Invalid choice! Please select 1 or 2.")

        case 4:
            print("Displaying all books...\n")

            # If there are any books in the list, display them
            if items:
                # Looping through each book in the 'items' list
                for index, book in enumerate(items, start=1):
                    print(f"Book {index}:")
                    print(f"  Title: {book['title']}")
                    print(f"  Author: {book['author']}")
                    print(f"  Year: {book['year']}")
                    print(f"  Genre: {book['genre']}")
                    print(f"  Read: {book['read']}\n")
            else:
                print("No books available.")

        case 5:
            print("Displaying statistics...")

            # Calculate the total number of books
            total_Books = len(items)
            # Calculate how many books have been read by checking if 'read' equals 'yes'
            books_read = len([book for book in items if book["read"].lower() == "yes"])

            # If there are books, calculate the percentage of books that have been read
            if total_Books > 0:
                percentage_read = (books_read / total_Books) * 100
                print(f"Total books: {total_Books}")
                print(f"Percentage read: {percentage_read:.2f}%")
            else:
                print("No books in the library.")

        case 6:
            print("Thank you for using the Library Manager!")
            break  # Exit the program when the user chooses to exit

        case _:
            print("Invalid choice! Please enter a number between 1 and 6.")
