"2.	Un programa que pregunte un nombre de fichero y muestre en pantalla el contenido de ese fichero, "\
"haciendo una pausa después de cada 25 líneas, para que dé tiempo a leerlo. Cuando el usuario pulse " \
"intro, se mostrarán las siguientes 25 líneas, y así hasta que termine el fichero. "

import Funciones

#pedimos archivo
archivo = input("¿Que archivo desea leer?")

#comprobamos si el nombre se refiere a un txt
# #esTxt = Funciones.esTxt(archivo)

#si es txt comprobamos si existe y si existe lo leememos en bloques de 25 lineas
existe = Funciones.existeFichero(archivo)

if existe == True:
    fichero = open(archivo, "rt")

    #contamos lineas
    lineas = len(fichero.readlines())
    print("El total de lineas es", lineas)

    #mostramos de 25 en 25 lineas
    max = 0
    Funciones.mostrarLineas(fichero, lineas, 0, 0, 5)

    fichero.close();
