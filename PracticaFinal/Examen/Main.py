from Examen.Trabajador import Trabajador
from Examen.Trabajador import Responsable
from Examen.Taller import Taller
import Funciones

talleres = []
trabajadores = []

def crearBdd():
    t1 = Taller(1,"Magenta","Desarrollo web", "La linea de la Concepción")
    t2 = Taller(2,"Creativos","Desarrollo android", "Algeciras")
    t3 = Taller(3,"Union Live","Desarrollo python", "Jimena")

    talleres.append(t1)
    talleres.append(t2)
    talleres.append(t3)

    r1 = Responsable(1, "Cristin", "Sanchez Moral", "77200128F",956125434, 100005)
    r1.activo = True
    t1.responsablre = r1
    trabajadores.append(r1)
    r2 = Responsable(2, "Carlos", "Ruz Moral", "77200222H",663420564, 100006 )
    r2.activo = True
    t2.responsablre = r2
    trabajadores.append(r2)
    r3 = Responsable(3, "Lidia", "Sanchez Jimena", "77233128G",956769079, 100009)
    r3.activo = True
    t3.responsablre = r3
    trabajadores.append(r3)

    crearFicheroResponsables()

def crearFicheroResponsables():
    fichero = open("Responsables.txt", "w+")
    fichero2 = open("Trabajadores.txt", "w+")
    for taller in talleres:
        if Funciones.ficheroVacio("Responsables.txt"):
            fichero.write("\n" + str(taller.identificador) + ":" + str(taller.responsablre.identificador))
        else:
            fichero.write(str(taller.identificador) + ":" + str(taller.responsablre.identificador))
        if Funciones.ficheroVacio("Trabajadores.txt"):
            fichero2.write("\n" + str(taller.responsablre.DNI) + ":" + str(
                taller.responsablre.identificador) + ":s:" + taller.localidad)
        else:
            fichero2.write(str(taller.responsablre.DNI) + ":" + str(
                taller.responsablre.identificador) + ":s:" + taller.localidad)


    fichero2.close()
    fichero.close()

def existeNIE(dni):
        fichero = open("Trabajadores.txt", "rt")
        fichero.seek(0)
        comprobacion = []
        existe = False
        it = (linea for i, linea in enumerate(fichero))
        for linea in it:
            comprobacion.append(linea.split(":"))

        for i in range(0, len(comprobacion)):
            if comprobacion[i][0] == dni:
                existe = True
        fichero.close()
        return existe


def existeId(id):
    for b in trabajadores:
        if b.identificador == id:
            if id == b.identificador:
                return True
    return False

def existeIdTaller(id):
    for b in talleres:
        if b.identificador == id:
            if id == b.identificador:
                return True
    return False

def plazaDisponible(localidad):
    for taller in talleres:
        if taller.localidad == localidad and taller.numPuestos > 0:
            return True
    return  False

def mayorId ():
    id = 0
    for b in trabajadores:
        if b.identificador > id:
            id = b.identificador
    return id

def altaTrabajador():
    opcion = Funciones.lee_opcion("¿Es una nueva incorporacion a la empresa este trabajador?\nS - SI\nN - NO",
                                  ["S", "N"])
    if opcion == "S":
        DNI = Funciones.escribeNIE()
        if existeNIE(DNI):
            preferencia = Funciones.escribeCadena("¿Que localidad prefiere?")
            for trabajador in trabajadores:
                if trabajador.DNI == DNI:
                    identificador = trabajador.identificador
                    trabajador.activo = True
                    trabajador.preferencia = preferencia
            if plazaDisponible(preferencia):
                fichero = open ("Trabajadores.txt", "a+")
                fichero.write("\n" + DNI + ":" + str(identificador) +":s"+":"+preferencia)
                fichero.close()
                for taller in talleres:
                    if taller.localidad == preferencia:
                        taller.numPuestos = taller.numPuestos -1
                print("Se le ha asignado", preferencia)
            else:
                posibilidad = False
                for taller in talleres:
                    if taller.numPuestos > 0 and not posibilidad:
                        posibilidad = True
                        localidad = taller.nombre
                        taller.numPuestos = taller.numPuestos -1
                        print("Se le ha asignado", localidad)
                fichero = open("Trabajadores.txt", "a+")
                fichero.write("\n" + DNI + ":" + str(identificador) + ":s" + ":" + localidad)
                fichero.close()
            print("El identificador asignado es: ", identificador)
        else:
            print("No existe el trabajador indicado")

    else:
        id = mayorId()+1
        nombre = Funciones.escribeCadena("Nombre del trabajador: ")
        apellidos = Funciones.escribeCadena("Apellido: ")
        DNI = Funciones.escribeNIE()
        preferencia = Funciones.escribeCadena("¿Que localidad prefiere?")
        if plazaDisponible(preferencia):
            fichero = open("Trabajadores.txt", "a+")
            fichero.write("\n" + DNI + ":" + str(id) + ":s" + ":" + preferencia)
            fichero.close()
            for taller in talleres:
                if taller.localidad == preferencia:
                    taller.numPuestos = taller.numPuestos - 1
            trabajadores.append(Trabajador(id,nombre, apellidos, DNI))
            print("Se le ha asignado", preferencia)
        else:
            posibilidad = False
            for taller in talleres:
                if taller.numPuestos > 0 and not posibilidad:
                    posibilidad = True
                    localidad = taller.nombre
                    taller.numPuestos = taller.numPuestos - 1
                    print("Se le ha asignado", localidad)
            fichero = open("Trabajadores.txt", "a+")
            fichero.write("\n" + DNI + ":" + str(id) + ":s" + ":" + localidad)
            fichero.close()
            trabajadores.append(Trabajador(id, nombre, apellidos, DNI))
        print("El identificador que ha sido asignado es: ", id)

def baja():
    id = Funciones.escribeEntero("Introduce el identificador del trabajador a dar de baja: ")
    if existeId(id):
        localidad = ""
        fichero = open("Trabajadores.txt", "a+")
        fichero.seek(0)
        comprobacion = []
        it = (linea for i, linea in enumerate(fichero))
        for linea in it:
            comprobacion.append(linea.split(":"))

        for i in range(0, len(comprobacion)):
            if comprobacion[i][2][0] == "s" and comprobacion[i][1] == str(id):
                dni = comprobacion[i][0]
                id = comprobacion[i][1]
                localidad = comprobacion[i][3]
                fichero.write(dni + ":" + str(id) + ":n" + ":" + localidad)
                print("El trabajador se ha registrado como inactivo")
        fichero.close()

        for trabajador in trabajadores:
            if trabajador.identificador == id:
                trabajador.activo = False
                print("La baja se ha hecho efectiva")

        for taller in talleres:
            if taller.localidad == localidad:
                taller.numPuestos = taller.numPuestos +1
                print("Hay un nuevo puesto libre en ", localidad)
    else:
        print("No se ha podido localizar el id introducido en la bdd")

def listarTalleres():
    for taller in talleres:
        print("nombre: ",taller.nombre, ", localidad:", taller.localidad, ", taller:", taller.identificador)
    opcion = Funciones.lee_opcion("\n ¿Quieres ver detalles de un taller concreto?\nS - Si\nN - No\n",["S","N"])
    if opcion == "S":
        id = Funciones.escribeEntero("Introduce el id del taller que quieres ver detalladamente")
        if existeIdTaller(id):
            for taller in talleres:
                if id == taller.identificador:
                    print("nombre: ", taller.nombre, ", localidad:", taller.localidad, ", taller:", taller.identificador, ", especialidad: ", taller.especialidad)
        else:
            print("El id no existe")

def listaResponsables():
    for trabajador in trabajadores:
        if isinstance(trabajador, Responsable):
            print("nombre: ", trabajador.nombre, ", dni:", trabajador.DNI, ", id:", trabajador.identificador)
    opcion = Funciones.lee_opcion("\n ¿Quieres ver detalles de un responsable concreto?\nS - Si\nN - No\n",["S","N"])
    if opcion == "S":
        id = Funciones.escribeEntero("Introduce el id del responsable que quieres ver detalladamente")
        if existeId(id):
            for responsable in trabajadores:
                if id == responsable.identificador:
                    print("nombre: ", responsable.nombre, ", taller:", responsable.identificador, ", dni: ", responsable.DNI)
        else:
            print("El id no existe")

def listaTrabajadores():
    for trabajador in trabajadores:
        print("nombre: ", trabajador.nombre, ", dni:", trabajador.DNI, ", id:", trabajador.identificador)
    opcion = Funciones.lee_opcion("\n ¿Quieres ver detalles de un responsable concreto?\nS - Si\nN - No\n",["S","N"])
    if opcion == "S":
        id = Funciones.escribeEntero("Introduce el id del trabajador que quieres ver detalladamente")
        if existeId(id):
            for responsable in trabajadores:
                if id == responsable.identificador:
                    print("nombre: ", responsable.nombre, ", id:", responsable.identificador, ", dni: ", responsable.DNI)
        else:
            print("El id no existe")

def menu ():
    salir = False
    while (not salir):
        print("MENU PRINCIPAL: ")
        print("1. Agregar trabajador")
        print("2. Dar baja trabajador")
        print("3. Listar Trabajadores")
        print("4. Listar talleres")
        print("5. Listar responsables")
        print("6. Generar informe taller")
        print("7. General informe trabajador")
        print("8. Salir")
        opcion = Funciones.escribeEntero("Introduce una opcion (1 - 5): ")

        if opcion < 1 or opcion > 5:
            print("ERROR: No has introducido un valor valido")
        else:
            if opcion == 1:
                altaTrabajador()
            if opcion == 2:
                baja()
            if opcion == 3:
                listaTrabajadores()
            if opcion == 4:
                listarTalleres()
            if opcion == 5:
                listaResponsables()
            if opcion == 8:
                salir = True
                print("Fin del programa.")

        print("\n\n")

def main():
    crearBdd()
    menu()

if __name__ == '__main__':
    main();