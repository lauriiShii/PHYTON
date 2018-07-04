"7.	Escribe un programa que calcule la suma de dos matrices."

def pideMatriz (col, row):

    # Se declara la primer matriz con el num de filas y columnas dados por el usuario
    matriz =[[0 for x in range(row)] for y in range(col)];

    #Se utiliza un ciclo para solicitar los valores de la primer matriz
    for i in range(row):
        for j in range(col):
            matriz[i][j] = int(input("Valor:"));
            
    return matriz;

def sumarMatriz (matriz1, matriz2, col, row):

    # Se declara una tercer matriz para almacenar el resultado de la suma
    matriz3 =[[0 for x in range(row)] for y in range(col)]

    #Se utiliza un ciclo para realizar la suma
    for i in range(row):
        for j in range(col):
            matriz3[i][j] = matriz1[i][j]+ matriz2[i][j];

    # Al final se imprime la matriz 3 con el resultado
    return matriz3;


def main():

    # se solicita al usuario el numero de columnas de las matrices
    col = int(input("NUMERO DE COLUMNAS:"));

    # se solicita al usuario el numero de filas de las matrices
    row = int(input("NUMERO DE FILAS:"));

    matriz1 = pideMatriz(col, row);
    matriz2 = pideMatriz(col, row);

    matriz3 = sumarMatriz(matriz1, matriz2, col, row);

    print(matriz3);

if __name__ == '__main__':
    main();