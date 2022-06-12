from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from models.empleado import Empleado

@dataclass
class Publicador:
    codigo: int = -1
    nombre: str = None

    def __eq__(self, obj) -> bool:
        return self.nombre == obj.nombre

@dataclass
class Autor:
    codigo: int = -1
    nombre: str = None

    def __eq__(self, obj) -> bool:
        return self.nombre == obj.nombre

@dataclass
class Idioma:
    codigo: int = -1
    nombre: str = None

    def __eq__(self, obj) -> bool:
        return self.nombre == obj.nombre

@dataclass
class Libro:
    book_id: str = None
    num_pages: int = -1
    average_rating: float = -1
    title: str = None
    publication_date: datetime|str = datetime.now()
    ratings_count: int = -1
    text_reviews_count: int = -1
    isbn:int = -1
    isbn_13:int = -1
    idioma: Idioma=None
    publicador: Publicador = None
    autores: List[Autor] = field(default_factory=list)

    def __eq__(self, other):
        return self.book_id == other.book_id
    
    def update_autores(self, autores: List[Autor]):
        lista_autores: List[Autor] = []
        for autor in autores:
            if autor in self.autores:
                lista_autores.append(autor)
        self.autores = lista_autores
    
    def add_autor(self, autor: Autor):
        if autor not in self.autores:
            self.autores.append(autor)
    

