"Escriba un programa que pida un número y a continuación escriba la lista de todos los divisores del número (incluidos el uno y él mismo)."

numero = int(input("Escriba un número entero mayor que cero: "))
lista = []

if numero <= 0:
    print("¡Le he pedido un número entero mayor que cero!")
else:
    print("Los divisores de", numero, "son ", end="")
    for i in range(1, numero + 1):
        if numero % i == 0:
            lista.append(i)
print("Los divisores de", numero, "son ", lista)