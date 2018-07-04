"1.	Haz un programa que lea un fichero “fichero.txt” y escriba en otro fichero “FICHERO2.TXT” "
"el contenido del fichero de entrada con todas las letras en mayúsculas."
"a.	Deberá avisar si el fichero de inicio está vacío."
"b.	Deberá avisar si el fichero de inicio no existe."

import Funciones

#compribamos si existe el fichero de inicio sino lo creamos
existe = Funciones.existeFichero("Ejercicio01/fichero1.txt")

#creamos ficheros
if existe == False:
    fichero1 = open("Ejercicio01/fichero1.txt", "w")
else:
    fichero1 = open("Ejercicio01/fichero1.txt", "r")

fichero2 = open("Ejercicio01/fichero2.txt", "a+")

#comprobamos si el fichero de inicio esta vacio
vacio = Funciones.ficheroVacio("Ejercicio01/fichero1.txt")

#si no esta vacio entonces copiamos el contenido del fichero de inicio al de destino
if vacio == False:
    contenido = fichero1.read()
    fichero2.seek(0)
    fichero2.write(contenido)
    fichero2.seek(0)
    contenido = fichero2.read()
    print(contenido)

#cerramos ficheros
fichero1.close()
fichero2.close()