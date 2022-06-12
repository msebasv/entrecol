from datetime import datetime
from io import BytesIO
from typing import List, Union
from openpyxl import load_workbook
import json
from fastapi import FastAPI, UploadFile, File
from bd import pelicula
from bd.empleado import get_or_create_cargo, get_or_create_dependencia, get_or_create_empleado, get_or_create_eps, get_or_create_pension, insertar_novedades, get_empleados
from handlers.handle_libro import handle_libros
from models.empleado import Cargo, Dependencia, Empleado, Eps, Pension, Novedad
from models.libro import Libro
from models.pelicula import Pelicula, Genero
from utils.empleado_parser import tuple_to_cargo, tuple_to_dependencia, tuple_to_empleado, tuple_to_eps, tuple_to_pension
from dataclasses import asdict
from utils.sqlconnector import mydb
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/bookFile")
async def read_book_doc(libros: UploadFile):
    json_data = json.load(libros.file)
    handle_libros(json_data, mydb)

    return {'data': len(json_data)}

@app.post("/userFile")
async def read_employees_doc(documento_empleados: bytes = File()):
    wb = load_workbook(BytesIO(documento_empleados))
    for sheet in wb:
        if sheet.title == 'MAESTRO NÓMINA':
            for row in sheet.iter_rows(min_row=3, values_only=True):
                ## Creation of employee and dependencies

                dep = tuple_to_dependencia(get_or_create_dependencia(asdict(Dependencia(nombre=row[2])), mydb))
                cargo = tuple_to_cargo(get_or_create_cargo(asdict(Cargo(nombre=row[3])), mydb))
                eps = tuple_to_eps(get_or_create_eps(asdict(Eps(nombre=row[5])), mydb))
                pension = tuple_to_pension(get_or_create_pension(asdict(Pension(nombre=row[7])), mydb))
                
                get_or_create_empleado(asdict(Empleado(row[0], row[8], row[6], datetime.strptime(str(row[4]), '%Y%m%d'), row[1],"admin", 2, cargo, pension, dep, eps)),mydb)
        else:
            lista_novedades: List[Novedad] = []
            for row in sheet.iter_rows(min_row=3, values_only=True):
                codigo_empleado = row[0]
                cod_novedad = 3
                if row[2] != None:
                    cod_novedad = 2
                elif row[3] != None:
                    cod_novedad = 1

                dias_trabajados = row[3]
                dias_no_trabajados = 0
                if row[4] != None:
                    dias_no_trabajados = row[4]
                else: 
                    dias_no_trabajados = row[5]
                
                # fecha inicio
                fecha_inicio= None
                if (row[6] != None): fecha_inicio = datetime.strptime(row[6], '%Y.%m.%d')
                elif (row[8] != None): fecha_inicio = datetime.strptime(row[8], '%Y.%m.%d')
                else: fecha_inicio = None

                # fecha fin
                fecha_fin= None
                if (row[6] != None): fecha_fin = datetime.strptime(row[7], '%Y.%m.%d')
                elif (row[8] != None): fecha_fin = datetime.strptime(row[9], '%Y.%m.%d')
                else: fecha_fin = None

                bonificacion = float(row[10])
                transporte = float(row[11])

                novedad = Novedad(
                    cod_tipo_novedad=cod_novedad,
                    dias_trabajados=dias_trabajados,
                    dias_no_trabajados= dias_no_trabajados,
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin,
                    bonificacion=float(bonificacion),
                    transporte=float(transporte),
                    cod_empleado=codigo_empleado,
                )
                lista_novedades.append(novedad)
            insertar_novedades([asdict(i) for i in lista_novedades], mydb)

@app.post("/movieFile")
async def read_movies_dec(documento_peliculas:bytes= File()):
    list_doc = documento_peliculas.decode().split("\n")
    list_generos: List[Genero] = []
    list_libros: List[Libro] = []
    for i in list_doc:
        datos = i.split("::")
        if len(datos) <= 1: break
        n_pelicula = Pelicula(codigo=int(datos[0]),nombre=datos[1])
        for gen in datos[2].split("|"):
            new_gen = Genero(nombre=gen)
            n_pelicula.add_genero(new_gen)
            if (not new_gen in list_generos): list_generos.append(new_gen)
        list_libros.append(pelicula)
    


        

            




@app.get("/empleado")
async def retrieve_empleados(pagination:int = 1, quantity:int = 10):
    empleados:List[Empleado] = [tuple_to_empleado(i, mydb) for i in get_empleados(quantity, pagination, mydb)]
    for i in empleados:
        i.fecha_ingreso = i.fecha_ingreso.strftime("%Y-%m-%d")
    return empleados
