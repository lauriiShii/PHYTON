from enum import Enum;

class Operacion (Enum):
    SUMA = "suma";
    RESTA = "resta";
    MULTIPLICACION = "multiplicacion";
    DIVISION ="division";


def calculadora(num1, num2, OPCION):
    num3 = 0;
    return num3;


def llamada_de_retorno(func=""):
    return globals()[func]();


def main():

    # llamamos al metodo calculadora
    llamada_de_retorno("calculadora");

if __name__ == '__main__':
    main();
