file = open('movies.dat.txt', 'r')
lines = file.readlines()
n_new_files = int(len(lines) / 20)

for i in range(n_new_files):
    file_name = 'movies/movies_' + str(i) + '.dat.txt'
    new_file = open(file_name, 'w')
    for j in range(20):
        new_file.write(lines[i * 20 + j])
    new_file.close()