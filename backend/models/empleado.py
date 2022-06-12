from datetime import datetime
from dataclasses import dataclass

@dataclass
class Rol:
    codigo: int = -1
    nombre: str = None

@dataclass
class Cargo:
    codigo: int = -1
    nombre: str = None

@dataclass
class Pension:
    codigo: int = -1
    nombre: str = None

@dataclass
class Dependencia:
    codigo: int = -1
    nombre: str = None

@dataclass
class Eps:
    codigo: int = -1
    nombre: str = None

@dataclass
class Empleado:
    codigo: int = -1
    sueldo: float = -1
    arl: bool = False
    fecha_ingreso: datetime.date = datetime.now()
    nombre: str = None
    contraseña: str = None
    rol: Rol = -1
    cargo: Cargo = None
    pension: Pension = None
    dependencia: Dependencia = None
    eps: Eps = None
    
@dataclass
class Novedad:
    codigo: int = -1
    cod_empleado: int = -1
    cod_tipo_novedad: int = -1
    dias_trabajados: int = -1
    dias_no_trabajados: int = -1
    fecha_inicio: datetime= datetime.now()
    fecha_fin: datetime = datetime.now()
    bonificacion:float = -1
    transporte:float = -1
