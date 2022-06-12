import mysql.connector

mydb = mysql.connector.connect(
    host="proyegod-do-user-8625564-0.b.db.ondigitalocean.com",
    port="25060",
    user="doadmin",
    password="AVNS_3KuXnnoONrgRMbF2o55",
    database="defaultdb"
)
"""sql = '''
CREATE TABLE IDIOMA (
	codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)	
);

CREATE TABLE TIPO_NOVEDAD (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);
CREATE TABLE CARGO (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);
CREATE TABLE PENSION (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);
CREATE TABLE DEPENDENCIA (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);
CREATE TABLE ROL (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);
CREATE TABLE EPS (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);
CREATE TABLE AUTOR (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);
CREATE TABLE PUBLICADOR (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);
CREATE TABLE GENERO (
    codigo int auto_increment UNIQUE,
    nombre varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (codigo)
);

CREATE TABLE EMPLEADO(
    codigo int auto_increment,
    sueldo double,
    arl boolean,
    fecha_ingreso date,
    nombre varchar(255),
    contraseña varchar(255),
    cod_rol int,
    cod_cargo int,
    cod_pension int,
    cod_dependencia int,
    cod_eps int,
    PRIMARY KEY (codigo),
    FOREIGN KEY (cod_rol) REFERENCES ROL(codigo),
    FOREIGN KEY (cod_cargo) REFERENCES CARGO(codigo),
    FOREIGN KEY (cod_pension) REFERENCES PENSION(codigo),
    FOREIGN KEY (cod_dependencia) REFERENCES DEPENDENCIA(codigo),
    FOREIGN KEY (cod_eps) REFERENCES EPS(codigo)
);

CREATE TABLE NOVEDAD (
    codigo int auto_increment,
    cod_tipo_novedad int,
    dias_trabajados int,
    dias_no_trabajados int,
    dias_novedad int,
    fecha_inicio date,
    fecha_fin date,
    cod_empleado int,
    bonificacion double,
    transporte double,
    PRIMARY KEY (codigo),
    FOREIGN KEY (cod_tipo_novedad) REFERENCES TIPO_NOVEDAD(codigo),
    FOREIGN KEY (cod_empleado) REFERENCES EMPLEADO(codigo)
);

CREATE TABLE LIBRO(
    book_id int,
    num_pages int,
    average_rating double,
    title varchar(255),
    isbn varchar(10),
    isbn13 varchar(13),
    publication_date date,
    ratings_count int,
    text_reviews_count int,
    cod_empleado int,
    cod_publicador int,
    cod_idioma int,
    PRIMARY KEY (book_id),
    FOREIGN KEY (cod_empleado) REFERENCES EMPLEADO(codigo),
    FOREIGN KEY (cod_publicador) REFERENCES PUBLICADOR(codigo),
    FOREIGN KEY (cod_idioma) REFERENCES IDIOMA(codigo)
);

CREATE TABLE LIBRO_AUTOR(
	cod_autor int,
	cod_libro int,
	PRIMARY KEY (cod_autor, cod_libro),
    FOREIGN KEY (cod_autor) REFERENCES AUTOR(codigo),
    FOREIGN KEY (cod_libro) REFERENCES LIBRO(book_id)
);

CREATE TABLE PELICULA(
    codigo int auto_increment,
    titulo varchar(255),
    PRIMARY KEY (codigo)
);

CREATE TABLE PELICULA_GENERO(
    cod_pelicula int not null,
    cod_genero int not null,
    PRIMARY KEY (cod_pelicula, cod_genero),
    FOREIGN KEY (cod_pelicula) REFERENCES PELICULA(codigo),
    FOREIGN KEY (cod_genero) REFERENCES GENERO(codigo)
);
'''
mycursor = mydb.cursor()

mycursor.execute(sql)


cursor = mydb.cursor()

sql = "INSERT INTO ROL (codigo, nombre) VALUES (%s, %s)"
val = [(1, "admin"), (2, "empleado")]

cursor.executemany(sql, val)
mydb.commit()


sql = "INSERT INTO TIPO_NOVEDAD (codigo, nombre) VALUES (%s, %s)"
val = [(1, "incapacidad"), (2, "vacaciones")]

cursor.executemany(sql, val)
mydb.commit()"""