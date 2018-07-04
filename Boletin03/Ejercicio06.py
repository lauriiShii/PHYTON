
clases = {}
clases["1CFGS"] = ["Carmen", 15]
clases["2CFGS"] = ["Eva", 30]
clases["1CFGM"] = ["Santi", 5]
clases["2CFGM"] = ["Eva", 6]

def menu():

    print (""" Menu
            1) Recorrer Clases
            2) Eliminar
            3) Agregar
            4) Salir""")

    opc = int(input("Elija una opción\n"))

    while (opc >0 and opc <4):
        if opc == 1:
            recorrer()
            opc = int(input("Elija una opción\n"))
        elif opc == 2:
            eliminar()
            opc = int(input("Elija una opción\n"))
        elif opc == 3:
            agregar()
            opc = int(input("Elija una opción\n"))

def recorrer():
    print(clases)

def eliminar():
    claseEliminar = input("Que clase deseas eliminar")
    del clases[claseEliminar]

def agregar():
    # clases[input("Que clase deseas crear")] = [input("Que profesor la impatte"), input("¿cuantos alumnos son?")]

    cont = 0
    profesor = input("Que profesor la impatte");

    for profe in clases:
        if profe == profesor:
            cont =  cont +1

    if(cont < 2):
        clases[input("Que clase deseas crear")] = [profesor, input("¿cuantos alumnos son?")]
    else:
        print("No es posible añadir mas clases para ese profesor")

menu()