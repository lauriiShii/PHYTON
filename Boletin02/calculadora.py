def Calculadora():

    # mostramos menú
    print (""" Menu
            1) Suma
            2) Resta
            3) Multiplicacion
            4) Division
            5) Salir""")

    # pedimos respuesta
    opc = int(input("Elija una opción\n"))

    # segun la opcion seleccionada hace una cosa u otra
    while (opc >0 and opc <5):
        x = int(input("Número 1: \n"))
        y = int(input("Número 2: \n"))
        if opc == 1:
            print ("La Suma es:", x+y)
            opc = int(input("Elija una opción\n"))
        elif opc == 2:
            print ("La Resta es:", x-y)
            opc = int(input("Elija una opción\n"))
        elif opc == 3:
            print ("La Multiplicacion es:", x*y)
            opc = int(input("Elija una opción\n"))
        elif opc == 4:
            try:
              print ("La Division es:", x/y)
              opc = int(input("Elija una opción\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              opc = int(input("Elija una opción\n"))



def main():

    # llamamos al metodo calculadora
    Calculadora()

if __name__ == '__main__':
    main();