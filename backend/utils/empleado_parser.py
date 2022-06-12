from datetime import datetime
from bd.empleado import get_cargo_by_id, get_dependencia_by_id, get_eps_by_id, get_pension_by_id, get_rol, get_rol_by_id
from models.empleado import Cargo, Dependencia, Pension, Rol, Eps, Empleado
from dataclasses import asdict

def tuple_to_rol(rol:tuple)->Rol:
    el_rol = rol[0]
    new_eps = Eps()
    new_eps.codigo = el_rol[0]
    new_eps.nombre = el_rol[1]

    return new_eps

def tuple_to_cargo(cargo:tuple)->Cargo:
    el_cargo = cargo[0]
    new_eps = Eps()
    new_eps.codigo = el_cargo[0]
    new_eps.nombre = el_cargo[1]

    return new_eps

def tuple_to_pension(pension:tuple)->Pension:
    el_pension = pension[0]
    new_eps = Eps()
    new_eps.codigo = el_pension[0]
    new_eps.nombre = el_pension[1]

    return new_eps

def tuple_to_dependencia(dep:tuple)->Dependencia:
    el_dep = dep[0]
    new_eps = Eps()
    new_eps.codigo = el_dep[0]
    new_eps.nombre = el_dep[1]

    return new_eps

def tuple_to_eps(eps:tuple)->Eps:
    el_eps = eps[0]
    new_eps = Eps()
    new_eps.codigo = el_eps[0]
    new_eps.nombre = el_eps[1]

    return new_eps

def tuple_to_empleado(emp:tuple, mydb) -> Empleado:
    new_empleado = Empleado()
    new_empleado.codigo = int(emp[0])
    new_empleado.sueldo = float(emp[1])
    new_empleado.arl = bool(emp[2])
    if type(emp[3]) != str : new_empleado.fecha_ingreso = emp[3]
    else: new_empleado.fecha_ingreso = datetime.strptime(emp[3],"%Y-%m-%d")
    new_empleado.nombre = emp[4]
    new_empleado.contraseña = emp[5]
    new_empleado.rol = tuple_to_rol(get_rol_by_id(asdict(Rol(codigo=int(emp[6]))), mydb))
    new_empleado.cargo = tuple_to_cargo(get_cargo_by_id(asdict(Cargo(codigo=int(emp[7]))), mydb))
    new_empleado.pension = tuple_to_pension(get_pension_by_id(asdict(Pension(codigo=int(emp[8]))), mydb))
    new_empleado.dependencia = tuple_to_dependencia(get_dependencia_by_id(asdict(Dependencia(codigo=int(emp[9]))), mydb))
    new_empleado.eps = tuple_to_dependencia(get_eps_by_id(asdict(Eps(codigo=int(emp[10]))), mydb))
    return new_empleado