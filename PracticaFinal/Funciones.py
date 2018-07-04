# pide un dni valido
def escribeNIE():
    valido = False

    while valido == False:
        dni = str(input("Introduce un DNI o CIF: "))
        valido = validoDNI(dni)

        if valido == False:
            print("Debe introducir un DNI o CIF valido")

    return dni


# metodo copiado de internet (funciona)
def validoDNI(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = "XYZ"
    reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) \
               and tabla[int(dni) % 23] == dig_control
    return False


# escribe un entero
def escribeEntero(mensaje):
    while True:
        try:
            entero = int(input(mensaje))
            break
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")

    return entero


# escribe una cadena
def escribeCadena(mensaje):
    while True:
        try:
            cad = str(input(mensaje))
            break
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")

    return cad


# comprueba si una cad solo tiene letras
def escribeAlfabetico(mensaje):
    valido = False

    while valido == False:
        cad = input(mensaje)
        if cad.isalpha() == True:
            valido = True
    return cad


def lee_opcion(mensaje, opciones):
    while True:
        opcion = str(input(mensaje)).upper()
        if opcion in opciones:
            return opcion

def ficheroVacio (archivo):
    import os
    vacio = False

    if os.stat(archivo).st_size == 0:
        vacio = True

    return vacio