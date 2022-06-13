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
        q_tit = " AND LOWER(LIBRO.title) LIKE LOWER('%" + tittle + "%')"
        
    if quiantity != -1 and pagination != -1:
        pag = f'LIMIT {quiantity*pagination}, {quiantity}'


    sql = ('''
        SELECT  P.cod_libro, l.num_pages, l.average_rating, l.title, l.isbn, l.isbn13, l.publication_date,
        l.ratings_count, l.text_reviews_count, a.codigo, a.nombre, i.codigo, i.nombre, p.codigo, p.nombre
        FROM (
            SELECT DISTINCT cod_libro
        FROM LIBRO, LIBRO_AUTOR, AUTOR
        {pag}
        ) P, LIBRO l, LIBRO_AUTOR la, AUTOR a , IDIOMA i , PUBLICADOR p 
        WHERE l.book_id = la.cod_libro
        AND la.cod_autor = a.codigo
        AND l.cod_idioma = i.codigo
        AND l.cod_publicador = p.codigo
        AND P.cod_libro = la.cod_libro
        {q_tit}
        {query_fecha}
        ORDER BY l.title
    '''.format(pag=pag, q_tit=q_tit, query_fecha=query_fecha))
    cursor.execute(sql)

    return cursor.fetchall()