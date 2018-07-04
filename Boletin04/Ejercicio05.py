"5.	Dado un fichero “alumnos.txt” que tiene registros de alumnos, con la siguiente información por cada alumno: "
"a.	dni "
"b.	apellidos "
"c.	nombre"
"d.	turno – los turnos van del 1 al 10"
"Diseña un programa que te permita seleccionar la información a mostrar dependiendo del turno."
"Deberá permitir calcular el número de alumnos almacenados en el fichero."
"Diseña un programa que intercambie los alumnos de dos turnos que el usuario deberá incluir por teclado."

import Funciones

#da la info de los alumnos indicados para un turno
def infoAlumnos(turno):
    fichero = open("alumnos.txt", "rt")
    fichero.seek(0)
    alumnos = []

    #sacamos los datos del fichero alumnos
    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        alumnos.append(linea.split(":"))

    #los mapeamos y mostramos solo los que tienen el turno indicado
    for i in range(0, len(alumnos)):
        if int(alumnos[i][3]) == int(turno):
            print("DNI: ", alumnos[i][0], "\nApellidos: ", alumnos[i][1], "\nNombre: ", alumnos[i][2], "\nTurno: ", alumnos[i][3])

    fichero.close()

#numero de alumnos registrados
def numAlumnos():
    fichero = open("alumnos.txt", "rt")
    fichero.seek(0)
    alumnos = []

    #sacamos los datos del fichero alumnos
    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        alumnos.append(linea.split(":"))

    #contamos los datos
    print(len(alumnos))

    fichero.close()

#cambiar turno
def cambiarTurno():
    fichero = open("alumnos.txt", "rt")
    fichero.seek(0)
    ok = False
    alumnos = []

    #primero guardamos todos los datos de los alumnos
    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        alumnos.append(linea.split(":"))

    #pedimos turno a cambiar y pot cual
    turno = input("¿Que turno deseas cambiar?")
    nuevoTurno = input("¿Por cual lo cambias?")

    #buscamos todos los alumnos con el turno concreto y lo modificamos por el nuevo
    for i in range(0, len(alumnos)):
        if int(alumnos[i][3]) == int(turno):
            alumnos[i][3] = nuevoTurno

    fichero.close()

    #sobreescribimos el fichero con todos los datos actualizados
    fichero = open("alumnos.txt", "w")

    for i in range(0, len(alumnos)):
        fichero.write(alumnos[i][0]+ ":"+ alumnos[i][1]+ ":"+ alumnos[i][2]+ ":"+ alumnos[i][3])

    fichero.close()


salir = False
opcion = 0

while (not salir):

    print("ALUMNOS - MENU PRINCIPAL")
    print("1. Mostrar informacion de los alumnos de un turno")
    print("2. ¿Cuantos alumnos hay?")
    print("3. Intercambiar turno")
    print("4. Salir")

    opcion = int(input("Introduce una opcion (1 - 4): "))

    if (opcion == 1):
        turno = input("De que turno deseas obtener información: ")
        infoAlumnos(turno)

    if (opcion == 2):
        numAlumnos()

    if (opcion == 3):
        cambiarTurno()

    if (opcion == 4):
        salir = True
        print("Fin del programa.")
