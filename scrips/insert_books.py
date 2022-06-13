import requests

n_mov_files = 277
endopint = 'http://127.0.0.1:8000/bookFile'

for i in range(n_mov_files+1):
    file_name = 'books/books_' + str(i) + '.json'
    with open(file_name, 'r') as f:
        documento_libros = f.read()
        r = requests.post(endopint, files={'libros': documento_libros})
        print(r.status_code)
        if r.status_code >= 200 and r.status_code < 300:
            print(file_name, "successfully inserted")
        else: print(file_name, "could not be inserted")
