from typing import Dict, List, Tuple


def insertar_idiomas(idioma:List[Dict], mydb):

    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO IDIOMA (nombre) VALUES (%s)')

    val:List[Tuple] = []
    for i in idioma:
        val.append((i['nombre'],))

    cursor.executemany(sql, val)

    mydb.commit()

def insertar_publicadores(publicadores:List[Dict], mydb):

    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO PUBLICADOR (nombre) VALUES (%s)')

    val:List[Tuple] = []
    for i in publicadores:
        val.append((i['nombre'],))

    cursor.executemany(sql, val)

    mydb.commit()

def insertar_autores(autores:List[Dict], mydb):

    cursor = mydb.cursor()

    sql = ('INSERT IGNORE INTO AUTOR (nombre) VALUES (%s)')

    val:List[Tuple] = []
    for i in autores:
        val.append((i['nombre'],))

    cursor.executemany(sql, val)
    mydb.commit()
