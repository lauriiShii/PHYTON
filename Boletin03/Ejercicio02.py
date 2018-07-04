"2. Escribir una función que, dados cuatro números, devuelva el mayor producto de dos de ellos. "
"Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más grande que se puede obtener entre ellos."

num1 = 1
num2 = 5
num3 = -2
num4 = -4

numeros = []

numeros.append(num1)
numeros.append(num2)
numeros.append(num3)
numeros.append(num4)
numOrden = []

def calcularProducto(numeros):

    #sorted los ordena de menor a mayor
    numOrden = sorted(numeros)

    #calcular producto con los dos primeros numeros
    producto1 = numOrden[0] * numOrden[1]

    #calcular producto con los dos ultimos numeros
    producto2 = numOrden[2] * numOrden[3]

    #comparar resultados
    if(producto1 > producto2):
        return producto1
    else:
        # devolvemos resultado mayor
        return producto2

print(calcularProducto(numeros))