"2.	Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista."

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    numero2 = int(input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))

    if numero2 < 1:
        print("¡Imposible!")
    else:
        eliminar = []
        for i in range(numero2):
            print("Dígame la palabra", str(i + 1) + ": ", end="")
            palabra = input()
            eliminar += [palabra]
        print("La lista de palabras a eliminar es:", eliminar)

        for i in eliminar:
            for j in range(len(lista)-1, -1, -1):
                if lista[j] == i:
                    del(lista[j])
        print("La lista es ahora:", lista)