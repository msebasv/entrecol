from typing import Tuple

from models.pelicula import Genero


def tuple_to_genero(genero:Tuple) -> Genero:
    return Genero(genero[0], genero[1])