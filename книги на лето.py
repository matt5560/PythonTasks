total_books = int(input())
books_to_read = int(input())
set_books = set()
set_books_to_read = set()


for i in range (total_books):
    book = input()
    set_books.add(book)


for i in range (books_to_read):
    book_to_read = input()
    set_books_to_read.add(book_to_read)
    
    if book_to_read in set_books:
        print("YES")
    else:
        print("NO")
