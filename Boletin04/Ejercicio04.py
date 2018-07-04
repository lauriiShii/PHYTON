"4.	Dados dos ficheros de texto “f1.txt” y “f2.txt”, en los que cada línea es una serie de "
"números separados por “:”, y suponiendo que las líneas están ordenadas por el primer número "
"de menor a mayor en los dos ficheros, haz un programa que lea los dos ficheros línea por línea "
"y escriba en el fichero “f3.txt” las líneas que tengan un inicio común."

import Funciones

fichero1 = open("Ejercicio03/fichero1.txt", "rt")
fichero2 = open("Ejercicio03/fichero2.txt", "rt")
fichero3 = open("Ejercicio03/fichero3.txt", "w")

#nos posicionamos en el principio del primer fichero
#obtenemos todos los datos del primer fichero y comparamos uno a uno el de la primera columna
fichero1.seek(0)
datos1 = []
it = (linea1 for i, linea1 in enumerate(fichero1))
for linea1 in it:
    datos1.append(linea1.split(":", 1))

print(datos1)

#nos posicionamos en el inicio del fichero segundo y obtenemos sus datos
fichero1.seek(0)
datos2 = []
ite = (linea2 for i, linea2 in enumerate(fichero2))
for linea2 in ite:
    datos2.append(linea2.split(":", 1))

print(datos2)

#comparamos el primer dato de la primera columna del segundo fichero con el que tenemos del primer fichero
#si coincide lo añadimos al tercer fichero

for i in range(0,len(datos1)):
    for j in range(0,len(datos2)):
        if datos1[i][0] == datos2[j][0]:
            fichero3.writelines(datos1[i][0] + ":" + datos2[j][1])
            print(datos1[i][0], datos2[j][1])

print("fin")

fichero1.close()
fichero2.close()
fichero3.close()
