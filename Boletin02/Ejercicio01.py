"1.	Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista."


palabra = "c";
lista = []

# Introducimos datos en la lista
while palabra != " ":
    palabra = input("Ingresa dato (espacio para terminar): ")
    if palabra != " ":
        lista.append(palabra)

# Mostramos el resultado
print("Esta es la lista de inscritos: ", lista);

# Palabra para buscar
buscar = input("Dígame la palabra a buscar: ")

# contamos cuantas veces se repite
contador = 0
for i in lista:
    if i == buscar:
        contador += 1;

# mostramos resultado
if contador == 0:
    print("La palabra '" + buscar + "' no aparece en la lista.");
elif contador == 1:
    print("La palabra '" + buscar + "' aparece una vez en la lista.");
else:
    print("La palabra '" + buscar + "' aparece", contador, "veces en la lista.");