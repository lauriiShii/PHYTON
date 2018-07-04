def sumar(valor1, valor2):
    return valor1 + valor2


def restar(valor1, valor2):
    return valor1 - valor2


def multiplicar(valor1, valor2):
    return valor1 * valor2


def dividir(valor1, valor2):
    return valor1 / valor2


def llamada_de_retorno(func="", valor1="", valor2=""):
    if func in globals():
        if callable(globals()[func]):
            return globals()[func](valor1, valor2)
