import pickle  # to convert objects to byte stream
from sys import getsizeof  # for hash function

class Book:
    book_code = 0  # integer
    title = ''  # string
    author = ''  # string
    publication_year = 0  # integer

# TASK 1.2
def input_books(n):
    books = [Book() for i in range(n)]  # list of Book of length n
    for i in range(n):
        while True:
            try:
                books[i].book_code = int(input("Enter book code: "))
                if not 100 <= int(books[i].book_code) <= 999:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid book code\n")
        books[i].title = input("Enter book title: ")  # string
        books[i].author = input("Enter book author: ")  # string
        while True:
            try:
                books[i].publication_year = int(input("Enter year of publication: "))
                break
            except ValueError:
                print("Please enter a valid year")

        print("\nBook code: " + str(books[i].book_code))
        print("Title: " + books[i].title)
        print("Author: " + books[i].author)
        print("Publication Year: " + str(books[i].publication_year) + '\n')
    return books

# TASK 1.3
def store_books_to_file(books):
    with open('books.dat', 'wb') as f:
        for book in books:
            pickle.dump(book, f)

# TASK 1.4
def read_all_books_from_file():
    with open('books.dat', 'rb') as f:
        while True:
            try:
                book = pickle.load(f)
                print("\nBook code: " + str(book.book_code))
                print("Title: " + book.title)
                print("Author: " + book.author)
                print("Publication Year: " + str(book.publication_year) + '\n')
            except EOFError:
                break


my_books = input_books(10)
store_books_to_file(my_books)
read_all_books_from_file()

# TASK 1.5
record_size = getsizeof(Book())  # 48 bytes
max_no_records = 15

def h(id):
    global record_size, max_no_records
    return (id % max_no_records) * record_size + 1

# TASK 1.6

# h(100) -> 481
# h(134) -> 673
# h(277) -> 337
# h(422) -> 97
# h(999) -> 433
