"4. Realiza un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 y monedas de 2 y 1. "
"Por ejemplo, si deseamos conocer el desglose de 434, el programa mostrará por pantalla el siguiente resultado"

dinero = {}
dinero[500] = "Billete"
dinero[200] = "Billete"
dinero[100] = "Billete"
dinero[50] = "Billete"
dinero[20] = "Billete"
dinero[10] = "Billete"
dinero[5] = "Billete"
dinero[2] = "Moneda"
dinero[1] = "Moneda"

cant = 1358;

def calcularDesglose(cant):
    resto = cant
    for din in dinero:
        division = resto/din
        resto = resto % din
        if(division != 0):
            if division == 1 or division > 1:
                print (int(division), str(dinero[din]), "de", int(din))

calcularDesglose(cant)

