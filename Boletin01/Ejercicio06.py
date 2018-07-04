"6. Crea un programa en que sea capaz de crear el inverso de una cadena a partir de una cadena dada. Esta cadena deberá ser aportada por el usuario."

cuenta = 0;
aux = "";
i = 0;

cad = input("Dame una frase: ");

for carac in cad:
        cuenta += 1
        aux = aux + cad[len(cad) - cuenta];
print(aux);
