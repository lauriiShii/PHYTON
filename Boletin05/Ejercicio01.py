#construye el fichero alumnos
def contruirAlumnos():
    fichero = open("alumnos.txt", "w")

    alumnos = []
    alumno = ["Calvente", "Dominguez", "Laura", "77200128f", "23", "c/Padre Pandero n18", "lauracalventedominguez@gmail.com"]
    alumnos.append(alumno)
    alumno = ["Marquez", "Rodriguez", "Julio", "7737128f", "25", "c/Escolares n6 1ºA", "juliomarquez@gmail.com"]
    alumnos.append(alumno)
    alumno = ["Ordoñez", "Cintrano", "Antonio Carlos", "66200138r", "27", "c/San Jose n18", "antonio@gmail.com"]
    alumnos.append(alumno)

    for i in range(0, len(alumnos)):
        fichero.write(alumnos[i][0] + ":" + alumnos[i][1] + ":" + alumnos[i][2] + ":" + alumnos[i][3]+ ":" + alumnos[i][4]+ ":" + alumnos[i][5]+ ":" + alumnos[i][6]+"\n")

    fichero.close()

def dameDatos():
    fichero = open("alumnos.txt", "rt")
    fichero.seek(0)
    alumnos = []

    #sacamos los datos del fichero alumnos
    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        alumnos.append(linea.split(":"))

    #los mapeamos y mostramos solo los que tienen el turno indicado
    print("\nLISTADO DE ALUMNOS\n")
    for i in range(0, len(alumnos)):
        print("-- Primer apellido:", alumnos[i][0], "Segundo apellido:", alumnos[i][1], "Nmombre:", alumnos[i][2], "DNI:", alumnos[i][3], "Edad:",  alumnos[i][4], "Direccion:", alumnos[i][5], "Correo:", alumnos[i][6])

    fichero.close()

def numAltas ():

    fichero = open("alumnos.txt", "rt")
    fichero.seek(0)
    alumnos = []

    #sacamos los datos del fichero alumnos
    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        alumnos.append(linea.split(":"))

    fichero.close()

    print("-- hay ", len(alumnos), " alumnos dados de alta")

def listarNombresDirecciones():
    fichero = open("alumnos.txt", "rt")
    fichero.seek(0)
    alumnos = []

    #sacamos los datos del fichero alumnos
    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        alumnos.append(linea.split(":"))

    #los mapeamos y mostramos solo los que tienen el turno indicado
    print("\nLISTADO DE NOMBRES Y DIRECCIONES\n")
    for i in range(0, len(alumnos)):
        print("-- Nombre:", alumnos[i][0]," ", alumnos[i][1], ", ",alumnos[i][2], " Direccion:", alumnos[i][5])

    fichero.close()

def agregarAlumno():
    fichero = open("alumnos.txt", "a+")

    print("\nNUEVO ALUMNO\n")
    fichero.write(input("Primer Apellido: ")
                  +":"+ input("Segundo Apellido: ")
                  +":"+ input("Nombre: ")
                  +":"+ input("DNI: ")
                  +":"+ input("Edad: ")
                  +":"+ input("Direccion: ")
                  +":"+ input("Correo: "))
    fichero.close()
    dameDatos()

def borrarAlumno():

    dni = input("DNI del alumno que desea eliminar")

    fichero = open("alumnos.txt", "rt")
    fichero.seek(0)
    alumnos = []

    #sacamos los datos del fichero alumnos
    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        alumnos.append(linea.split(":"))

    fichero.close()
    fichero = open("alumnos.txt", "w")
    for i in range(0, len(alumnos)):
        if alumnos[i][3] != dni:
            fichero.write(alumnos[i][0] + ":" + alumnos[i][1] + ":" + alumnos[i][2] + ":" + alumnos[i][3]+ ":" + alumnos[i][4]+ ":" + alumnos[i][5]+ ":" + alumnos[i][6])
    fichero.close()

    print("\nSE HA BORRADO UN ALUMNO\n")
    dameDatos()

contruirAlumnos()
dameDatos()
numAltas()
listarNombresDirecciones()
agregarAlumno()
borrarAlumno()