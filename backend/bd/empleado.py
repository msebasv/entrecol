from datetime import datetime
from typing import Dict, List, Tuple

def get_or_create_eps(eps:dict, mydb)->tuple|None:
    new_eps = get_eps(eps, mydb)
    if (new_eps != None): return new_eps

    # if not found create a new on database
    cursor = mydb.cursor()
    sql = ('INSERT IGNORE INTO EPS (nombre) VALUES (%s)')
    val = (eps['nombre'],)
    cursor.execute(sql, val)
    mydb.commit()
    return get_eps(eps, mydb)
    

def get_eps(eps:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()
    nombre = eps['nombre']
    sql = (f'SELECT * FROM EPS WHERE nombre=\'{nombre}\'')

    cursor.execute(sql)
    tuple_eps = cursor.fetchall()

    if len(tuple_eps) == 0: return None
    return tuple_eps

def get_eps_by_id(eps:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()

    codigo = eps['codigo']

    sql = (f'SELECT * FROM EPS WHERE codigo=\'{codigo}\'')

    cursor.execute(sql)
    tuple_eps = cursor.fetchall()

    if len(tuple_eps) == 0: return None
    return tuple_eps

def get_or_create_cargo(cargo:dict, mydb)->tuple|None:
    new_cargo = get_cargo(cargo, mydb)
    if (new_cargo != None): return new_cargo

    # if not found create a new on database
    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO CARGO (nombre) VALUES (%s)')
    val = (cargo['nombre'],)
    cursor.execute(sql, val)
    mydb.commit()
    return get_cargo(cargo, mydb)
    

def get_cargo(cargo:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()

    nombre = cargo['nombre']
    sql = (f'SELECT * FROM CARGO WHERE nombre=\'{nombre}\'')

    cursor.execute(sql)
    tuple_eps = cursor.fetchall()

    if len(tuple_eps) == 0: return None
    return tuple_eps

def get_cargo_by_id(cargo:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()

    codigo = cargo['codigo']
    sql = (f'SELECT * FROM CARGO WHERE codigo=\'{codigo}\'')

    cursor.execute(sql)
    tuple_eps = cursor.fetchall()

    if len(tuple_eps) == 0: return None
    return tuple_eps

def get_or_create_rol(rol:dict, mydb)->tuple|None:
    new_rol = get_rol(rol, mydb)
    if (new_rol != None): return new_rol

    # if not found create a new on database
    cursor = mydb.cursor()


    sql = ('INSERT IGNORE INTO ROL (nombre) VALUES (%s)')
    val = (rol['nombre'],)
    cursor.execute(sql, val)
    mydb.commit()
    return get_rol(rol, mydb)
    

def get_rol(rol:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()

    nombre = rol['nombre']
    sql = (f'SELECT * FROM ROL WHERE nombre=\'{nombre}\'')

    cursor.execute(sql)
    tuple_rol = cursor.fetchall()

    if len(tuple_rol) == 0: return None
    return tuple_rol

def get_rol_by_id(rol:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()

    codigo = rol['codigo']
    sql = (f'SELECT * FROM ROL WHERE codigo=\'{codigo}\'')

    cursor.execute(sql)
    tuple_rol = cursor.fetchall()

    if len(tuple_rol) == 0: return None
    return tuple_rol


def get_or_create_pension(pension:dict, mydb)->tuple|None:
    new_pension = get_pension(pension, mydb)
    if (new_pension != None): return new_pension

    # if not found create a new on database
    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO PENSION (nombre) VALUES (%s)')
    val = (pension['nombre'],)
    cursor.execute(sql, val)
    mydb.commit()
    return get_pension(pension, mydb)
    

def get_pension(pension:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()
    nombre = pension['nombre']
    sql = (f'SELECT * FROM PENSION WHERE nombre=\'{nombre}\'')

    cursor.execute(sql)
    tuple_pension = cursor.fetchall()

    if len(tuple_pension) == 0: return None
    return tuple_pension

def get_pension_by_id(pension:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()

    codigo = pension['codigo']
    sql = (f'SELECT * FROM PENSION WHERE codigo=\'{codigo}\'')

    cursor.execute(sql)
    tuple_pension = cursor.fetchall()

    if len(tuple_pension) == 0: return None
    return tuple_pension

def get_or_create_dependencia(dep:dict, mydb)->tuple:
    new_dep = get_dependencia(dep, mydb)
    if (new_dep != None): return new_dep

    # if not found create a new on database
    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO DEPENDENCIA (nombre) VALUES (%s)')
    val = (dep['nombre'],)
    cursor.execute(sql, val)
    mydb.commit()
    return get_dependencia(dep, mydb)
    

def get_dependencia(dep:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()

    nombre = dep['nombre']
    sql = (f'SELECT * FROM DEPENDENCIA WHERE nombre=\'{nombre}\'')

    cursor.execute(sql)
    tuple_dep = cursor.fetchall()

    if len(tuple_dep) == 0: return None
    return tuple_dep

def get_dependencia_by_id(dep:dict, mydb)-> tuple|None:

    cursor = mydb.cursor()

    codigo = dep['codigo']
    sql = (f'SELECT * FROM DEPENDENCIA WHERE codigo=\'{codigo}\'')

    cursor.execute(sql)
    tuple_dep = cursor.fetchall()

    if len(tuple_dep) == 0: return None
    return tuple_dep


def get_or_create_empleado(emp:dict, mydb)-> tuple|None:

    new_emp = get_empleado_by_id(emp, mydb)
    if (new_emp != None): return new_emp

    # if not found create a new on database
    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO EMPLEADO (codigo, sueldo, arl, '+
    'fecha_ingreso, nombre, contraseña, cod_rol,'+
    'cod_cargo, cod_pension, '+
    'cod_dependencia, cod_eps) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')

    codigo = emp['codigo']
    sueldo = emp['sueldo']
    arl = 0
    if emp['arl'] == "Positiva": arl = 1
    fecha_ingreso = datetime.strftime(emp['fecha_ingreso'], "%Y,%m,%d")
    nombre:str = emp['nombre']
    constraseña = emp['contraseña']
    cod_rol = emp['rol']
    cargo = emp['cargo']
    pension = emp['pension']
    dep = emp['dependencia']
    eps = emp['eps']

    val = (codigo, sueldo, arl,
    fecha_ingreso, nombre.replace('\xa0', ''),
    constraseña, cod_rol, cargo['codigo'],
    pension['codigo'], dep['codigo'],
    eps['codigo'])

    print(val)
    cursor.execute(sql, val)
    mydb.commit()
    return get_dependencia(emp, mydb)


def get_empleado_by_id(emp:dict, mydb) -> tuple|None:

    cursor = mydb.cursor()

    codigo = emp['codigo']
    sql = (f'SELECT * FROM EMPLEADO WHERE codigo=\'{codigo}\'')

    cursor.execute(sql)
    tuple_emp = cursor.fetchall()

    if len(tuple_emp) == 0: return None
    return tuple_emp

def insertar_novedades(novedad:List[Dict], mydb):

    cursor = mydb.cursor()

    sql = ('INSERT IGNORE IGNORE INTO NOVEDAD (fecha_inicio, fecha_fin, dias_trabajados, '+
    'dias_no_trabajados, bonificacion, transporte, cod_empleado, '+
    'cod_tipo_novedad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)')

    val:List[Tuple] = []
    for i in novedad:
        fecha_inicio = None
        fecha_fin = None
        if (i['fecha_inicio'] != None): fecha_inicio = datetime.strftime(i['fecha_inicio'], "%Y-%m-%d")
        if (i['fecha_fin'] != None): fecha_fin = datetime.strftime(i['fecha_fin'], "%Y-%m-%d")

        row = (
            fecha_inicio,
            fecha_fin,
            i['dias_trabajados'],
            i['dias_no_trabajados'],
            i['bonificacion'],
            i['transporte'],
            i['cod_empleado'],
            i['cod_tipo_novedad'],
        )
        val.append(row)

    cursor.executemany(sql, val)

    mydb.commit()

    return cursor.fetchall()


def get_empleados(quantity:int, page:int, fecha_inicio:str, fecha_fin:str, name:str, mydb):

    cursor = mydb.cursor()

    query_dates = ''
    query_page = ''
    query_name = ''

    if name != '':
        query_name = " and LOWER(nombre) LIKE LOWER('%"+name+"%')"
    if (fecha_inicio != "" and fecha_fin != ""):
        query_dates = f' AND fecha_ingreso BETWEEN \'{fecha_inicio}\' AND \'{fecha_fin}\''
    elif (fecha_inicio != ""):
        query_dates = f' AND fecha_ingreso >= \'{fecha_inicio}\''
    elif (fecha_fin != ""):
        query_dates = f' AND fecha_ingreso <= \'{fecha_fin}\''
    
    if quantity != -1 and page != -1:
        query_page = f' LIMIT {quantity} OFFSET {page * quantity}'

    sql = (f'SELECT * FROM EMPLEADO WHERE 1=1 {query_dates} {query_name} {query_page}')

    cursor.execute(sql)

    return cursor.fetchall()

def get_empleado_by_name(name, mydb):

    cursor = mydb.cursor()

    cursor.execute(f'SELECT * FROM EMPLEADO WHERE LOWER(nombre) LIKE LOWER(\'%{name}%\')')

    return cursor.fetchall()


    
def fetch_login(codigo:str, password:str, mydb):

    cursor = mydb.cursor()

    cursor.execute(f'SELECT * FROM EMPLEADO WHERE codigo=\'{codigo}\' AND contraseña=\'{password}\'')

    return cursor.fetchall()