def agregarContactos(agenda, nombre, telefono):
    agenda[nombre] = telefono

    return agenda


def eliminarContactos(agenda, nombre):
    existe = False

    for contacto in agenda:
        if contacto == nombre:
            existe = True

    if existe:
        agenda.pop(nombre)
        print("Cambio realizado")

    else:
        print("El contacto no existe")

    return agenda


def editarContacto(agenda, nombre, telefono):
    existe = False

    for contacto in agenda:
        if contacto == nombre:
            existe = True

    if existe:
        agenda[nombre] = telefono
        print("Cambio realizado")

    else:
        print("El contacto no existe")

    return agenda


def listarContactos(agenda):
    for contacto in agenda:
        print(contacto + " -> " + str(agenda[contacto]))


def buscarContactos(agenda, nombre):
    existe = False

    for contacto in agenda:
        if contacto == nombre:
            existe = True

    if existe:
        print(contacto + " -> " + str(agenda[contacto]))

    else:
        print("El contacto no existe")


agenda = {}
nombre = ""
telefono = 0
salir = False
opcion = 0

while (not salir):

    print("CONTACTOS - MENU PRINCIPAL")
    print("1. Agregar contactos")
    print("2. Eliminar contactos")
    print("3. Editar contacto")
    print("4. Listar contactos")
    print("5. Buscar contactos")
    print("6. Salir")

    opcion = int(input("Introduce una opcion (1 - 6): "))

    if (opcion == 1):
        nombre = input("Introduzca el nombre del nuevo contacto: ")
        telefono = int(input("Introduzca el numero de telefono del nuevo contacto: "))
        agenda = agregarContactos(agenda, nombre, telefono)

    if (opcion == 2):
        nombre = input("Introduzca el nombre del contacto a eliminar: ")
        agenda = eliminarContactos(agenda, nombre)

    if (opcion == 3):
        nombre = input("Introduzca el nombre del contacto a editar: ")
        telefono = int(input("Introduzca el nuevo numero de telefono: "))
        agenda = editarContacto(agenda, nombre, telefono)

    if (opcion == 4):
        listarContactos(agenda)

    if (opcion == 5):
        nombre = input("Introduzca el nombre del contacto a buscar: ")
        buscarContactos(agenda, nombre)

    if (opcion == 6):
        salir = True
        print("Fin del programa.")
