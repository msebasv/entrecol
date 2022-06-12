from models.libro import Idioma, Autor, Libro, Publicador

def tuple_to_idioma(idioma:tuple) -> Idioma:
    return Idioma(idioma[0], idioma[1])

def tuple_to_publicador(publicador:tuple) -> Publicador:
    return Publicador(publicador[0], publicador[1])

def tuple_to_autor(autor:tuple) -> Autor:
    return Autor(autor[0], autor[1])

