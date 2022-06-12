from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Genero:
    codigo:int = -1
    nombre:str = None

    def __eq__(self, other)-> bool:
        return self.nombre == other.nombre


@dataclass
class Pelicula:
    codigo:int = -1
    nombre:str = None
    generos:List[Genero] = field(default_factory=list)

    def add_genero(self, genero:Genero) -> None:
        self.generos.append(genero)

