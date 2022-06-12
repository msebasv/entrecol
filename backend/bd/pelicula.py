from typing import List, Tuple


def create_generos(generos:List[dict], mydb) -> tuple:
    
    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO GENERO (nombre) VALUES (%s)')

    val = [(genero['nombre'],) for genero in generos]

    cursor.executemany(sql, val)

    mydb.commit()

def get_generos(mydb) -> tuple:

    cursor = mydb.cursor()

    sql = ('SELECT * FROM GENERO')

    cursor.execute(sql)

    return cursor.fetchall()

def add_peliculas(peliculas:List[dict], mydb) -> int:

    cursor = mydb.cursor()

    sql = ('''INSERT IGNORE INTO PELICULA
    (codigo, titulo) VALUES (%s, %s)''')

    val = [(i['codigo'], i['nombre'],) for i in peliculas] 

    cursor.executemany(sql, val)

    mydb.commit()

    add_peliculas_genero(peliculas, mydb)

    return cursor.rowcount

def add_peliculas_genero(peliculas:List[dict], mydb) :



    cursor = mydb.cursor()

    sql = ('''INSERT IGNORE INTO PELICULA_GENERO (cod_pelicula, cod_genero)
    VALUES (%s, %s) ''')
    val = []
    for i in peliculas:
        if 'generos' in i: 
            for j in i['generos']:
                val.append((i['codigo'], j['codigo'],))
    
    cursor.executemany(sql, val)
    mydb.commit()


def get_peliculas(pagination:int, quiantity:int, title:str, mydb) -> Tuple:

    cursor = mydb.cursor()
    pag = ""
    q_title = ""
    if len(title) > 0:
        q_title = "AND LOWER(PELICULA.titulo) LIKE LOWER('%" + title + "%')"
    if quiantity != -1 and pagination != -1:
        pag = f'LIMIT {quiantity} OFFSET {quiantity*pagination}'

    cursor.execute('''
    SELECT PELICULA.codigo, PELICULA.titulo, GENERO.nombre, GENERO.codigo
    FROM PELICULA, GENERO, PELICULA_GENERO
    WHERE PELICULA.codigo = PELICULA_GENERO.cod_pelicula
    AND GENERO.codigo = PELICULA_GENERO.cod_genero
    {q_title}
    ORDER BY PELICULA.codigo
    {pag}  
    '''.format(q_title=q_title, pag=pag))


    return cursor.fetchall()
