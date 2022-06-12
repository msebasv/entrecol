from dataclasses import dataclass
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
    publication_date: datetime = datetime.now()
    ratings_count: int = -1
    text_reviews_count: int = -1
    isbn:int = -1
    isbn_13:int = -1
    idioma: Idioma=None
    empleado: Empleado = None
    publicador: Publicador = None
    autores: List[Autor] = None

    def __eq__(self, other):
        return self.book_id == other.book_id
