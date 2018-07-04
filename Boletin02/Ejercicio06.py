"6.	Escribe un programa que partiendo de una tupla con nombres (al menos 6) compruebe qué elemento de la tupla contiene un determinado carácter. Éste será aportado por el usuario."

def main():
    nombres = ["laura", "Carlos", "Julio", "Samuel", "David", "Cristin"];

    caracter = input("¿que caracter desea que busquemos?")

    i = 0;
    lista = [];
    for nombre in nombres:

        if caracter in nombres[i]:
            lista.append(nombres[i]);

        i += 1;

    print("Los nombres con dicho caracter son : ", lista);

if __name__ == '__main__':
    main();