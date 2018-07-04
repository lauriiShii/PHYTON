"7. Crea un programa que compruebe si una cadena es palíndromo."

var = input("Texto ::> ")

if var == var[::-1]:
    print("Es Palindromo");
else:
    print("No es palindromo");
