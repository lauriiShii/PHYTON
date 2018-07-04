
def dameTipoFecha():
    import datetime

    formato1 = "%a %b %d %H:%M:%S %Y"
    formato2 = "%d-%m-%y %I:%m %p"

    salir = False
    while (not salir):
        print("Fechas - Selecciona una opción: ")
        print("1.Formato1:", formato1)
        print("2.Formato2:", formato2)

        opcion = int(input("Introduce una opcion (1 - 2): "))

        if opcion == 1:
            return formato1
        if opcion == 2:
            return formato2