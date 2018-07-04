" 1. Escribe dos funciones que permitan calcular:"
"o La cantidad de segundos en un tiempo dado en horas, minutos y segundos."
"o La cantidad de horas, minutos y segundos de un tiempo dado en segundos."
"o Utilizando estas dos funciones escribe un programa que lea de teclado dos tiempos expresados en horas, minutos y segundos la sume y muestre el resultado en horas, minutos y segundos."

def calcularSegundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos


def calcularHorasMinutosSegundos(sec):
    horas = sec // 3600
    minutos = (sec - (horas * 3600)) // 60
    segundos = sec - (horas * 3600 + minutos * 60)

    return str(horas) + ":" + str(minutos) + ":" + str(segundos)


print("Los datos se deben introducir en el siguiente formato: HORAS MINUTOS SEGUNDOS. Ejemplo: 5 23 55")

hora1 = int(input("Introduzca las horas 1: "))
minuto1 = int(input("Introduzca los minutos 1: "))
segundo1 = int(input("Introduzca los segundos 1: "))
hora2 = int(input("Introduzca las horas 2: "))
minuto2 = int(input("Introduzca los minutos 2: "))
segundo2 = int(input("Introduzca los segundos 2: "))

tiempo1sec = calcularSegundos(hora1, minuto1, segundo1)
tiempo2sec = calcularSegundos(hora2, minuto2, segundo2)

tiempoTotalSec = tiempo1sec + tiempo2sec

tiempoTotal = calcularHorasMinutosSegundos(tiempoTotalSec)

print(tiempoTotal)