import Ejercicio03

opcion = 0

while (opcion >= 0 and opcion < 5):

    print("CALCULADORA - MENU PRINCIPAL")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Introduce una opcion (1 - 5): "))

    if (opcion == 1):
        valor1 = int(input("Introduce el valor 1: "))
        valor2 = int(input("Introduce el valor 2: "))
        resultado = Ejercicio03.llamada_de_retorno("sumar", valor1, valor2)
        print("Resultado:", resultado)

    if (opcion == 2):
        valor1 = int(input("Introduce el valor 1: "))
        valor2 = int(input("Introduce el valor 2: "))
        resultado = Ejercicio03.llamada_de_retorno("restar", valor1, valor2)
        print("Resultado:", resultado)

    if (opcion == 3):
        valor1 = int(input("Introduce el valor 1: "))
        valor2 = int(input("Introduce el valor 2: "))
        resultado = Ejercicio03.llamada_de_retorno("multiplicar", valor1, valor2)
        print("Resultado:", resultado)

    if (opcion == 4):
        valor1 = int(input("Introduce el valor 1: "))
        valor2 = int(input("Introduce el valor 2: "))
        resultado = Ejercicio03.llamada_de_retorno("dividir", valor1, valor2)
        print("Resultado:", resultado)

    if (opcion == 5):
        print("Fin del programa.")
