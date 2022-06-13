import requests

n_mov_last = 216
n_mov_files = 533
endopint = 'http://127.0.0.1:8000/movieFile'

for i in range(n_mov_last, n_mov_files+1):
    file_name = 'movies/movies_' + str(i) + '.dat.txt'
    with open(file_name, 'r') as f:
        documento_peliculas = f.read()
        r = requests.post(endopint, files={'documento_peliculas': documento_peliculas})
        print(file_name, "successfully inserted")
        print(r.status_code)
