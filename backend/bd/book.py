from datetime import datetime
from typing import Dict, List, Tuple

from models.libro import Publicador


def insertar_idiomas(idioma:List[Dict], mydb):

    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO IDIOMA (nombre) VALUES (%s)')

    val:List[Tuple] = []
    for i in idioma:
        val.append((i['nombre'],))

    cursor.executemany(sql, val)

    mydb.commit()

def insertar_publicadores(publicadores:List[Dict], mydb):

    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO PUBLICADOR (nombre) VALUES (%s)')

    val:List[Tuple] = []
    for i in publicadores:
        val.append((i['nombre'],))

    cursor.executemany(sql, val)

    mydb.commit()

def insertar_autores(autores:List[Dict], mydb):

    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO AUTOR (nombre) VALUES (%s)')

    val:List[Tuple] = []
    for i in autores:
        val.append((i['nombre'],))

    cursor.executemany(sql, val)
    mydb.commit()

def get_autores(mydb) -> tuple:
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM AUTOR")

    return cursor.fetchall()

def get_idiomas(mydb) -> tuple:
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM IDIOMA")

    return cursor.fetchall()

def get_publicadores(mydb) -> tuple:
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM PUBLICADOR")

    return cursor.fetchall()


def insertar_libros(libros:List[dict], mydb) -> tuple:

    cursor = mydb.cursor()

    sql = ('''
        INSERT IGNORE INTO LIBRO (
            book_id,
            num_pages,
            average_rating,
            title,
            isbn,
            isbn13,
            publication_date,
            ratings_count,
            text_reviews_count,
            cod_publicador,
            cod_idioma)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''')
    val:List[Tuple] = []
    for i in libros:
        publicador = i['publicador']
        idioma = i['idioma']
        publication_date = datetime.strftime(i['publication_date'], '%Y-%m-%d')

        row = (
            i['book_id'],
            i['num_pages'],
            i['average_rating'],
            i['title'],
            i['isbn'],
            i['isbn_13'],
            publication_date,
            i['ratings_count'],
            i['text_reviews_count'],
            publicador['codigo'],
            idioma['codigo'],
        )
        val.append(row)
    
    cursor.executemany(sql, val)

    mydb.commit()

    insertar_libros_autores(libros, mydb)

def insertar_libros_autores(libros:List[dict], mydb) -> tuple:

    cursor = mydb.cursor()
    sql = ('''
        INSERT IGNORE INTO LIBRO_AUTOR (
            cod_libro,
            cod_autor)
        VALUES (%s, %s)
    ''')

    val = []
    for i in libros:
        for j in i['autores']:
            row = (i['book_id'], j['codigo'])
            val.append(row)
    
    cursor.executemany(sql, val)

    mydb.commit()

def get_libros(pagination:int, quiantity:int, tittle:str, fecha_inicio:str, fecha_fin:str, mydb) -> tuple:
    cursor = mydb.cursor()
    pag = ""
    q_tit = ""
    query_fecha = ""

    if fecha_inicio != "" and fecha_fin != "":
        query_fecha = f' AND publication_date BETWEEN \'{fecha_inicio}\' AND \'{fecha_fin}\''
    elif fecha_inicio != "" and fecha_fin == "":
        query_fecha = f' AND publication_date >= \'{fecha_inicio}\''
    elif fecha_inicio == "" and fecha_fin != "":
        query_fecha = f' AND publication_date <= \'{fecha_fin}\''

    if len(tittle) > 0:
        q_tit = "AND LOWER(LIBRO.title) LIKE LOWER('%" + tittle + "%')"
        
    if quiantity != -1 and pagination != -1:
        pag = f'LIMIT {quiantity} OFFSET {quiantity*pagination}'
    cursor.execute('''
        SELECT LIBRO.book_id,
                LIBRO.num_pages,
                LIBRO.average_rating,
                LIBRO.title,
                LIBRO.isbn,
                LIBRO.isbn13,
                LIBRO.publication_date,
                LIBRO.ratings_count,
                LIBRO.text_reviews_count,
                AUTOR.codigo,
                AUTOR.nombre,
                IDIOMA.codigo,
                IDIOMA.nombre,
                PUBLICADOR.codigo,
                PUBLICADOR.nombre
        FROM LIBRO, LIBRO_AUTOR, AUTOR, IDIOMA, PUBLICADOR
        WHERE LIBRO.book_id = LIBRO_AUTOR.cod_libro
        AND LIBRO_AUTOR.cod_autor = AUTOR.codigo
        AND LIBRO.cod_idioma = IDIOMA.codigo
        AND LIBRO.cod_publicador = PUBLICADOR.codigo
        {q_tit}
        {query_fecha}
        ORDER BY LIBRO.title
        {pag}   
        '''.format(q_tit=q_tit, pag=pag, query_fecha=query_fecha))


    return cursor.fetchall()