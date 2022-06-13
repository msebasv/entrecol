import json

f = open('books.json', 'r')
data = json.load(f)

n_books = len(data)
n_book_lines = 40
n_books_per_file = n_books // n_book_lines


for i in range(n_books_per_file):
    file_name = 'books/books_' + str(i) + '.json'
    if (i +1) * n_book_lines < n_books:
        books_file = data[i * n_book_lines : (i + 1) * n_book_lines]
    else:
        books_file = data[i * n_book_lines :]
    with open(file_name, 'w') as outfile:
        json.dump(books_file, outfile)
    outfile.close()