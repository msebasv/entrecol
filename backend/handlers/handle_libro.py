from cmath import log
from datetime import datetime
from typing import List, Tuple
from models.libro import Autor, Libro, Publicador, Idioma
from bd.book import get_autores, get_idiomas, get_publicadores, insertar_idiomas, insertar_publicadores, insertar_autores, insertar_libros
import utils.libro_parser as lb
from dataclasses import asdict

def handle_libros(libros:List, mydb) -> List:
    authors_collected:List[Autor] = []
    publishers_collected:List[Publicador] = []
    books_collected:List[Libro] = []
    lenguage_collected:List[Idioma] = []
    for i in libros:
        autores_name = i['authors'].split('/')
        autores:List[Autor] = []
        for aut in autores_name:
            autor = Autor(nombre=aut)
            autores.append(autor)
            if (not autor in authors_collected): authors_collected.append(autor)
        publisher = Publicador(nombre=i['publisher'])
        if (not publisher in publishers_collected): publishers_collected.append(publisher)
        idioma = Idioma(nombre=i['language_code'])
        if (not idioma in lenguage_collected): lenguage_collected.append(idioma)
        book_id = int(i['bookID'])
        title = i['title']
        average_rating = float(i['average_rating'])
        isbn = i['isbn']
        isbn_13 = i['isbn13']
        num_pages = int(i['num_pages'])
        ratings_count = int(i['ratings_count'])
        text_reviews_count = int(i['text_reviews_count'])
        date = i['publication_date'].split('/')
        day = date[1]
        month = date[0]
        year = date[2]
        if len(day) != 2: day = '0' + day
        if len(month) !=2: month = '0' + month
        publication_date = datetime.strptime(month+day+year, '%m%d%Y')
        book = Libro(book_id,
                num_pages,
                average_rating,
                title,
                publication_date,
                ratings_count,
                text_reviews_count,
                isbn,
                isbn_13,
                idioma,
                publisher,
                autores)
        books_collected.append(book)

    
    insertar_autores([asdict(i) for i in authors_collected], mydb)
    insertar_idiomas([asdict(i) for i in lenguage_collected], mydb)

    insertar_publicadores([asdict(i) for i in publishers_collected], mydb)

    new_idiomas = [lb.tuple_to_idioma(i) for i in get_idiomas(mydb)]
    new_publicadores = [lb.tuple_to_publicador(i) for i in get_publicadores(mydb)]
    new_autores = [lb.tuple_to_autor(i) for i in get_autores(mydb)]
    
    for i in books_collected:
        i.publicador = get_new_publicador(i.publicador, new_publicadores)
        i.idioma = get_new_idioma(i.idioma, new_idiomas)
        i.update_autores(new_autores)
    
    insertar_libros([asdict(i) for i in books_collected], mydb)

        

def handle_peliculas(peliculas:List, mydb) -> List:
    pass


def get_new_idioma(idioma:Idioma, idiomas:List[Idioma]) -> Idioma:
    for j in idiomas:
        if (idioma == j):
            return j
    return None

def get_new_publicador(publicador:Publicador, publicadores:List[Publicador]) -> Publicador:
    
    for j in publicadores:
        if publicador == j:
            return j
    return None
