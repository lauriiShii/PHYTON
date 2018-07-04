"""
2. Se desea realizar una aplicación que permita gestionar la cartera de clientes de una empresa. Pretendemos gestionar
 la cantidad total a cobrar a cada uno de esos clientes durante un mes de facturación.
De cada cliente se almacenará su CIF o NIF, nombre, apellidos y dirección.
Durante el mes se le irán anotando sus registros a cada cliente, y a finales de mes se le calculará la cantidad a pagar.
La empresa tiene dos tipos de clientes:
Normales. CantidadaCobrar = totalFacturado
Preferentes. CantidadaCobrar = totalFacturado – totalFacturado * descuento /100
El administrativo usará las siguientes opciones de la aplicación:
1. Añadir cliente
2. Añadir factura a cliente
3. Generar informe por cliente
4. Generar informe general del mes

Habrá un fichero clientes.txt donde se almacenarán los datos de los clientes. En él, solo puede haber una línea por cada cliente.
Para añadir facturas deberá existir el cliente primero, es decir, no se aceptarán facturas para clientes no dados de alta
en el sistema. Se utilizará el fichero “facturas.txt”, y para cada una: id de cliente, fecha, concepto y precio.
El informe por cliente mostrará todos los datos del cliente, así como la información de todas las compras realizadas en
ese mes. Se mostrará también el importe total de ese cliente en ese mes, y me debe permitir almacenarlo en un fichero si
así se desea. Se debe contemplar los descuentos. El nombre de ese fichero debe ser el NIF del cliente.
Genera informe general del mes, pretende mostrar un resumen agrupado por clientes, donde se muestre el gasto total para
cada cliente y el total ingresado en el mes. Se deben contemplar los descuentos. Me debe permitir almacenar este balance
del mes en un fichero si así se solicita.
Deben estar controlador los errores de formato de los datos a introducir. Formato de CIF, nombres de clientes no numéricos…
Se deben usar excepciones para controlar posibles fallos, pero en la medida de lo posible me debe permitir arreglar el error.
Los ficheros que almacenan (clientes,txt y facturas.txt) datos tendrán el formato:
Dato1(separador)dato2(separador)dato3(separador)…
Los ficheros que almacenan informes deben tener un formato de informe estándar: saltos de líneas, márgenes, información ordenada…
"""

import Funciones


def aniadirCliente():
    fichero = open("clientes.txt", "a+")
    print("\nNUEVO CLIENTE\n")
    dni = Funciones.escribeNIE()
    nombre = Funciones.escribeCadena("Nombre: ")
    apellidos = Funciones.escribeCadena("Apellidos: ")
    direccion = Funciones.escribeCadena("Direccion: ")
    opcion = Funciones.lee_opcion("Tipo (N - Normal / P - Preferente): ", ["N", "P"])
    fichero.write("\n" + dni + ":" + nombre + ":" + apellidos + ":" + direccion + ":" + "N")
    fichero.close()


def ultimaFactura():
    fichero = open("facturas.txt", "rt")
    fichero.seek(0)
    facturas = []
    id = 0

    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        facturas.append(linea.split(":"))

    for i in range(0, len(facturas) + 1):
        if i == len(facturas):
            id = i

    fichero.close()

    return id


def existeCliente(dni):
    fichero = open("clientes.txt", "rt")
    fichero.seek(0)
    clientes = []
    existe = False
    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        clientes.append(linea.split(":"))

    for i in range(0, len(clientes)):
        if clientes[i][0] == dni:
            existe = True

    fichero.close()

    return existe


def aniadirFactura():
    import time
    fichero = open("facturas.txt", "a+")
    print("\nNUEVA FACTURA\n")
    dni = ""

    while not existeCliente(dni):
        dni = Funciones.escribeNIE()

    fecha = time.strftime("%d/%m/%y")
    concepto = Funciones.escribeCadena("Concepto de la factura: ")
    importe = Funciones.escribeEntero("Importe(sin decimales): ")

    fichero.write("\n" + str(ultimaFactura() + 1) + ":" + dni + ":" + fecha + ":" + concepto + ":" + str(importe))
    fichero.close()


def generarInforme(dni, modoGuardar):
    fichero = open("clientes.txt", "rt")
    fichero.seek(0)
    clientes = []

    it = (linea for i, linea in enumerate(fichero))
    esPreferente = False;

    for linea in it:
        clientes.append(linea.split(":"))

    for i in range(0, len(clientes)):
        if clientes[i][0] == dni:
            print("-- DNI del cliente: " + clientes[i][0] + " Nombre: " + clientes[i][1] + " " + clientes[i][
                2] + " Dirección :" + clientes[i][3] + " Tipo de cliente: " + clientes[i][4] + "\n")
            if clientes[i][4][0] == "P":
                esPreferente = True

    fichero.close()

    fichero = open("facturas.txt", "rt")
    fichero.seek(0)
    facturas = []

    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        facturas.append(linea.split(":"))

    print("--Facturas:\n")
    total = 0

    for i in range(0, len(facturas)):
        if facturas[i][1] == dni:
            print(
                "ID: " + facturas[i][0] + " Fecha: " + facturas[i][2] + " Concepto: " + facturas[i][3] + " Importe: " +
                facturas[i][4])
            total = total + int(facturas[i][4])

            if esPreferente:
                total = total / 2

            print("Total: " + str(total))

    fichero.close()
    if modoGuardar:
        guardar = Funciones.lee_opcion("¿Quieres guardar el total? (SI / NO)", ["SI", "NO"])

        if guardar == "SI":
            fichero = open("total.txt", "w+")

            fichero.write(str(total))

            fichero.close()

    return total


def generarInformeGeneral():
    fichero = open("clientes.txt", "rt")
    fichero.seek(0)
    clientes = []

    totalMensual = 0

    it = (linea for i, linea in enumerate(fichero))
    for linea in it:
        clientes.append(linea.split(":"))

    for i in range(0, len(clientes)):
        totalMensual = totalMensual + generarInforme(clientes[i][0], False)

    print("Total mensual: " + str(totalMensual))

    fichero.close()

    guardar = Funciones.lee_opcion("¿Quieres guardar el total mensual? (SI / NO)", ["SI", "NO"])

    if guardar == "SI":
        fichero = open("balanceMensual.txt", "w+")

        fichero.write(str(totalMensual))

        fichero.close()


opcion = 0

while (opcion >= 0 and opcion < 5):

    print("CLIENTES Y FACTURAS - MENU PRINCIPAL")
    print("1. Añadir cliente")
    print("2. Añadir factura")
    print("3. Generar informe cliente")
    print("4. Generar informe mensual")
    print("5. Salir")

    opcion = int(input("Introduce una opcion (1 - 5): "))

    if opcion == 1:
        aniadirCliente()

    if opcion == 2:
        aniadirFactura()

    if opcion == 3:
        dni = ""

        while not existeCliente(dni):
            dni = Funciones.escribeNIE()

        generarInforme(dni, True)

    if opcion == 4:
        generarInformeGeneral()
