"8.	Escribe un programa que genere una matriz de enteros con las dimensiones que indique el usuario, "
"con los datos que introduzca el usuario y que finalmente muestre por pantalla la diagonal de dicha matriz."


def pideMatriz(col, row):
    # Se declara la primer matriz con el num de filas y columnas dados por el usuario
    matriz = [[0 for x in range(row)] for y in range(col)];

    # Se utiliza un ciclo para solicitar los valores de la primer matriz
    for i in range(row):
        for j in range(col):
            matriz[i][j] = int(input("Valor:"));

    return matriz;

def main():

    # se solicita al usuario el numero de columnas de las matrices
    col = int(input("NUMERO DE COLUMNAS:"));

    # se solicita al usuario el numero de filas de las matrices
    row = int(input("NUMERO DE FILAS:"));

    matriz = pideMatriz(col, row);
    lista = [];
    for i in range(row):
        for j in range(row):
            if i == j:
                lista.append(matriz[i][j]);

    print(lista);

if __name__ == '__main__':
    main();