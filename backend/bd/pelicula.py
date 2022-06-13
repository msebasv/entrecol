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
        q_title = "AND LOWER(PEL.titulo) LIKE LOWER('%" + title + "%')"
    if quiantity != -1 and pagination != -1:
        pag = f'LIMIT {pagination*quiantity},{quiantity}'


    sql = ('''
            SELECT  P.cod_pelicula, PEL.titulo, G.NOMBRE, PG.cod_genero
        FROM (
            SELECT DISTINCT cod_pelicula
        FROM PELICULA
        {pag}
        ) P, PELICULA_GENERO PG, PELICULA PEL, GENERO G
        WHERE P.cod_pelicula = PG.cod_pelicula
        and P.cod_pelicula = PEL.codigo
        and PG.cod_genero = G.codigo
        {q_title}
    '''.format(q_title=q_title, pag=pag))

    cursor.execute(sql)


    return cursor.fetchall()
