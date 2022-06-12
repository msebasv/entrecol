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
    
    def update_generos(self, generos:List[Genero]) -> None:
        liste_generos:List[Genero]= []
        for i in generos:
            for j in self.generos:
                if (i == j):
                    liste_generos.append(i)
                    break
        
        self.generos = liste_generos