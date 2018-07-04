"""En una aplicación dedicada a la gestión del almacenamiento en una empresa aparecen dos conceptos: Contenedor y Mercancía. Los contenedores son recipientes de gran tamaño que son utilizados para el almacenamiento de mercancías. Un contenedor se caracteriza por su capacidad
(volumen total del contenedor, valor entero), las mercancías que contiene, número de mercancías y si está abierto o cerrado para recibir mercancías.
Por su parte, una mercancía se caracteriza por ocupar un volumen y puede estar contenida en un contenedor.

a) Identifica las propiedades de los objetos de la clase Contenedor. Para cada propiedad indica el atributo que almacena su
información o si es una propiedad calculada el cálculo necesario para implementarla. Escribe el código de un único constructor para la clase.
b) Entre las clases Contenedor y Mercancía existe la siguiente relación: Un contenedor puede contener varias mercancías y una mercancía puede estar contenida como máximo en un contenedor.
    b.1) el método addMercancia en la clase Contenedor sabiendo que un contenedor podrá alojar mercancías siempre que esté abierto y que el volumen de la nueva mercancía
    y el del resto de mercancías que contiene no sobrepase la capacidad del contenedor, y
    b.2) la clase Mercancía
c) La clase Caja que es un tipo de Mercancía que se caracteriza por tener las propiedades de ancho, alto y fondo. El volumen se calcula como el ancho x alto x fondo. Un Cubo es un tipo de Caja que tiene el mismo valor para alto, ancho y fondo. Escribe el código de las clases Caja y Cubo.
d) Debes incluir la interfaz necesaria, que te permita dar de alta contenedores y mercancías (cajas y cubos) y asignarlas de un elemento al otro."""

import Funciones
from ContenedoresMercancia.Contenedor import Contenedor
from ContenedoresMercancia.Mercancia import Cubo
from ContenedoresMercancia.Mercancia import Caja

contenedores = []

def dameIdMasGrande ():
    id = 0
    for contenedor in contenedores:
        if contenedor.identificador > id:
            id = contenedor.identificador
    return id

def addContenedor():
    id = dameIdMasGrande()
    capacidad = Funciones.escribeEntero("Capacidad total del contenedor: ")
    contenedor = Contenedor(id+1, capacidad)
    contenedores.append(contenedor)

def existeContenedor(id):
    for contenedor in contenedores:
        if contenedor.identificador == id:
            return True
    return False

def addCubo():
    id = Funciones.escribeEntero("¿A que contenedor deseas añadir el cubo?: ")
    if existeContenedor(id):
        lado = Funciones.escribeEntero("Lado del cubo: ")
        cubo = Cubo(lado)
        for contenedor in contenedores:
            if contenedor.identificador == id:
                contenedor.abrirContenedor()
                contenedor.addMercancia(cubo)
                contenedor.cerrarContenedor()
    else:
        print("El contenedor introducido no existe")

def addCaja():
    id = Funciones.escribeEntero("¿A que contenedor deseas añadir el cubo?: ")
    if existeContenedor(id):
        ancho = Funciones.escribeEntero("Ancho de la Caja: ")
        alto = Funciones.escribeEntero("Alto de la Caja: ")
        fondo = Funciones.escribeEntero("Fono  de la Caja: ")
        caja = Caja(ancho, alto, fondo)
        for contenedor in contenedores:
            if contenedor.identificador == id:
                contenedor.abrirContenedor()
                contenedor.addMercancia(caja)
                contenedor.cerrarContenedor()
    else:
        print("El contenedor introducido no existe")

def menu():
    salir = False
    while (not salir):

        print("CONTENEDORES Y MERCANCIAS - MENU PRINCIPAL")
        print("1. Agregar contenedor")
        print("2. Agregar cubo")
        print("3. Agregar caja")
        print("4. Salir")

        opcion = int(input("Introduce una opcion (1 - 4): "))

        if (opcion == 1):
            addContenedor()

        if (opcion == 2):
            addCubo()

        if (opcion == 3):
            addCaja()

        if (opcion == 4):
            salir = True
            print("Fin del programa.")

def main():
    menu()

if __name__ == '__main__':
    main();