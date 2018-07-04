"3.	Diseña una función “finfichero” que reciba dos parámetros: el primero debe ser un número entero " \
"positivo n, y el segundo el nombre de un fichero de texto. La función debe mostrar por pantalla las n " \
"últimas líneas del fichero."

import Funciones

fichero = open("archivo.txt", "rt")

Funciones.finfichero(5,fichero)

fichero.close()