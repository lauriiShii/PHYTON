
alumnos = {}
alumnos["Carlos"] = ["Matematicas", "Lenguaje"]
alumnos["Carmen"] = ["Matematicas"]
alumnos["Julio"] = ["Conocimiento del medio", "Educacion Fisica"]
alumnos["Samuel"] = ["Quimica","Fisica","Matematicas", "Conocimiento del medio"]
alumnos["Tamzota"] = ["Quimica"]

def menu():

    print (""" Menu
            1) Recorrer Alumnos
            2) Modificar una asignatura
            3) Agregar una asignatura
            4) Eliminar una asignatura
            5) Salir""")

    opc = int(input("Elija una opción\n"))

    while (opc >0 and opc <5):
        if opc == 1:
            recorrerAlumnos()
            opc = int(input("Elija una opción\n"))
        elif opc == 2:
            alumno = input("Alumno: \n")
            asignatura = input("Asignatura: \n")
            modificarAsignatura(alumno,asignatura)
            opc = int(input("Elija una opción\n"))
        elif opc == 3:
            alumno = input("Alumno: \n")
            aniadirAsignatura(alumno)
            opc = int(input("Elija una opción\n"))
        elif opc == 4:
            alumno = input("Alumno: \n")
            asignatura = input("Asignatura: \n")
            eliminarAsignatura(alumno,asignatura)
            opc = int(input("Elija una opción\n"))

def recorrerAlumnos():
    print("Los alumnos disponibles son:")
    print(alumnos);

def modificarAsignatura(alumno,asignatura):
    for x in range(len(alumnos[alumno])):
        if(alumnos[alumno][x] == asignatura):
            dato = input("¿Que asignatura desea incluir?")
            alumnos[alumno][x] = dato;

def eliminarAsignatura(alumno,asignatura):
    for x in range(len(alumnos[alumno])):
        if(alumnos[alumno][x] == asignatura):
            del alumnos[alumno][x];

def aniadirAsignatura(alumno):
    dato = input("¿Que asignatura desea incluir?")
    alumnos[alumno] = dato;

menu()