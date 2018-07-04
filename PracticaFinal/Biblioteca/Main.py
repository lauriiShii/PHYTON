"""Realiza en Python un SG para mantener información de una biblioteca.
 Nos interesa mantener información acerca de los materiales, los trabajadores de la biblioteca y los usuarios que realizan un préstamo.
 En cuanto a los materiales se necesita almacenar su título, su descripción, número de ejemplares y su código. Este código será auto-numérico.

Hay 3 tipos de materiales:

    * Libros: de los que nos interesará almacenar también su editorial, y disponen de 1 semana de préstamo.
    * Películas: de las que nos interesará también el director, actor principal, año de publicación y género. El préstamo para una película será de 3 días.
    * Revistas: almacenaremos su temática y el mes y año de publicación. El préstamo para revistas será de 10 días.

El programa deberá permitir las siguientes operaciones:

    1. Dar de alta/eliminar usuarios de la biblioteca
    2. Dar de alta/eliminar materiales de la biblioteca. Debe quedar constancia de si está disponible para su préstamo.
    3. Dar de alta/eliminar usuarios de la biblioteca.
    4. Realización de préstamo. Este préstamo deberá quedar registrado por un empleado de la biblioteca y se asignará un material a un usuario durante su periodo de préstamo establecido.

        a. Deberá controlarse que el material esté disponible.
        b. Un usuario no podrá tener en préstamo dos materiales diferentes.
        c. Cada vez que se preste/devuelva un material deberá quedar constancia en los ejemplares disponibles.

Cada clase deberá almacenarse en un fichero diferente.
Deberá generarse una interfaz que permita el manejo de estas clases y funciones."""

import Funciones
from Biblioteca.Persona import Trabajador
from Biblioteca.Persona import Usuario
from Biblioteca.Material import Libro
from Biblioteca.Material import Revista
from Biblioteca.Material import Pelicula

trabajadores = []
usuarios = []
materiales = []
trabajadorActual = Trabajador(0,"","")

def mayorId (busqueda):
    id = 0
    for b in busqueda:
        if b.identificador > id:
            id = b.identificador
    return id

def existeIdentificador(id, busqueda):
    for b in busqueda:
        if b.identificador == id:
            return True
    return False

def altaTrabajador ():
    nombre = Funciones.escribeCadena("Nombre del trabajador: ")
    apellidos = Funciones.escribeCadena("Apellidos: ")
    trabajador = Trabajador(mayorId(trabajadores)+1,nombre,apellidos)
    trabajadores.append(trabajador)

def altaUsuario ():
    nombre = Funciones.escribeCadena("Nombre del usuario: ")
    apellidos = Funciones.escribeCadena("Apellidos: ")
    usuario = Usuario(mayorId(usuarios)+1,nombre,apellidos)
    usuarios.append(usuario)

def altaMaterial ():
    print("Que tipo de material quieres añadir: ")
    opcion = Funciones.lee_opcion("L - libro \nP - Pelicula\nR - Revista\n", ["L","P","R"])

    if opcion == "L":
        titulo = Funciones.escribeCadena("Titulo: ")
        descripcion = Funciones.escribeCadena("Descripcion: ")
        numEjemplares = Funciones.escribeEntero("Numero de ejemplares: ")
        editorial = Funciones.escribeCadena("Editorial: ")
        libro = Libro(mayorId(materiales)+1, titulo, descripcion, numEjemplares, editorial)
        materiales.append(libro)
    if opcion == "P":
        titulo = Funciones.escribeCadena("Titulo: ")
        descripcion = Funciones.escribeCadena("Descripcion: ")
        numEjemplares = Funciones.escribeEntero("Numero de ejemplares: ")
        director = Funciones.escribeCadena("Director: ")
        actorPrincipal = Funciones.escribeCadena("Actor principal: ")
        anioPublicacion = Funciones.escribeEntero("Año de publicacion: ")
        genero = Funciones.escribeCadena("Genero: ")
        pelicula = Pelicula(mayorId(materiales)+1, titulo, descripcion, numEjemplares, director, actorPrincipal, anioPublicacion, genero)
        materiales.append(pelicula)
    if opcion == "R":
        titulo = Funciones.escribeCadena("Titulo: ")
        descripcion = Funciones.escribeCadena("Descripcion: ")
        numEjemplares = Funciones.escribeEntero("Numero de ejemplares: ")
        tematica = Funciones.escribeCadena("Tematica: ")
        mes= Funciones.escribeCadena("Mes: ")
        anio = Funciones.escribeEntero("Año: ")
        revista  = Revista(mayorId(materiales)+1, titulo, descripcion, numEjemplares,tematica, mes, anio)
        materiales.append(revista)

def baja ():
    opcion = Funciones.lee_opcion("¿Que desea dar de baja?\nT - Trabajador\nU - usuario\nM - Material\n", ["T","U","M"])
    id = Funciones.escribeEntero("Id que deseas dar de baja: ")

    if existeIdentificador(id, trabajadores) and opcion == "T":
        for trabajador in trabajadores:
            if trabajador.identificador == id:
                del trabajador

    if existeIdentificador(id, usuarios) and opcion == "U":
        for usuario in usuarios:
            if usuario.identificador == id:
                del usuario

    if existeIdentificador(id, materiales) and opcion == "U":
        for material in materiales:
            if material.identificador == id:
                del material

def identificate():
    id = Funciones.escribeEntero("¿Cual es tu identificador?: ")
    if existeIdentificador(id, trabajadores):
        for trabajador in trabajadores:
            trabajadorActual = trabajador
        subMenu()
        return True
    else:
        print("No se ha podido cotejar su id con la bdd")
        return False

def prestamo():
    import time
    idTrabajador = trabajadorActual.identificador
    idUsuario = Funciones.escribeEntero("Introduce el id del uduario: ")
    if existeIdentificador(idUsuario, usuarios):
        idMaterial = Funciones.escribeEntero("Introduce el id del material a prestar: ")
        if existeIdentificador(idMaterial, materiales):
            for material in materiales:
                material.noDisponible()
            for usuario in usuarios:
                usuario.noPrestamo()
            fichero = open ("registro.txt", "a+")
            fichero.write("\n"+str(idTrabajador)+":"+str(idUsuario)+":"+str(idMaterial)+":"+str(time.strftime("%d/%m/%y")))
            fichero.close()


def menu():
    salir = False
    while (not salir):

        print("BIBLIOTECA - MENU PRINCIPAL")
        print("1. Dar de alta trabajador")
        print("2. Identificar trabajador")
        print("3. Salir")

        opcion = int(input("Introduce una opcion (1 - 3): "))

        if (opcion == 1):
            altaTrabajador()
        if (opcion == 2):
            identificate()
        if (opcion == 3):
            salir = True
            print("Fin del programa.")

def subMenu():
    salir = False
    while (not salir):

        print("SUB-MENU - MENU PRINCIPAL")
        print("1. Dar de alta trabajador")
        print("2. Dar de alta usuario")
        print("3. Dar de alta material")
        print("4. Realizar una baja")
        print("5. Realizar prestamo")
        print("6. Salir")

        opcion = int(input("Introduce una opcion (1 - 6): "))

        if (opcion == 1):
            altaTrabajador()
        if (opcion == 2):
            altaUsuario()
        if (opcion == 3):
            altaMaterial()
        if (opcion == 4):
            baja()
        if (opcion == 5):
            prestamo()
        if (opcion == 6):
            salir = True
            print("Fin del programa.")

def main():
    menu()

if __name__ == '__main__':
    main();