
def existeFichero (archivo):
    import os.path
    existe = False

    if os.path.exists(archivo):
        print("El fichero existe")
        existe = True

    else:
        print("El fichero no existe")

    return existe

def ficheroVacio (archivo):
    import os
    vacio = False

    if os.stat(archivo).st_size == 0:
        print('El archivo esta vacío.')
        vacio = True

    return vacio

def esTxt (archivo):
    import re

    txt = False

    if re.match(archivo, "\.txt") != None:
        print('El archivo es un archivo de texto')
        txt = True
    else:
        print('El archivo no es un archivo de texto')

    return txt


def mostrarLineas(fichero, lineas, pos, max, numLineas):
    pasar = " no "
    fin = False

    if lineas >= numLineas -1:
        max += numLineas -1

        fichero.seek(pos)
        it = (linea for i, linea in enumerate(fichero) if i >= pos and i <= max)
        for linea in it:
            print(linea)
    else:
        fichero.seek(pos)
        it = (linea for i, linea in enumerate(fichero) if i >= pos)
        for linea in it:
            print(linea)
            fin = True

    if fin == False:
        pasar = input("Se han mostrado 25 lineas, presiona intro si deseas seguir")

    if pasar == "":
        lineas -= max
        pos = max
        mostrarLineas(fichero, lineas, pos, max, numLineas)

def finfichero(n, fichero):

    lineas = len(fichero.readlines())

    fichero.seek(lineas - n)

    it = (linea for i, linea in enumerate(fichero) if i > n + 1 )
    for linea in it:
        print(linea)