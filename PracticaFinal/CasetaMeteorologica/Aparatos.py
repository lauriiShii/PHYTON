from random import randint

class Aparato ():

    #constructor
    def __init__(self, identificador):
        self.identificador = identificador #int

    def observacion(self):
        pass

    def tryConexion(self):
        conexion = True

        if randint(1, 5) == 3:
            conexion = False

        return conexion

class Termometro (Aparato):

    #constructor
    def __init__(self, identificador):
        Aparato.__init__(self, identificador)

    def observacion(self):
        import random
        conexion = False
        numIntentos = 0

        while not conexion and numIntentos < 2:
            if not self.tryConexion():
                numIntentos += 1
            else:
                conexion = True

        if conexion:
            medida = random.uniform(30, 35)
            return " T: %f ºC" % (medida)
        else:
            return "--"

class Barometro (Aparato):

    # constructor
    def __init__(self, identificador):
        Aparato.__init__(self, identificador)

    def observacion(self):
        import random

        conexion = False
        numIntentos = 0

        while not conexion and numIntentos < 2:
            if not self.tryConexion():
                numIntentos += 1
            else:
                conexion = True

        if conexion:
            medida = random.uniform(1, 10)
            if medida < 5:
                return " H: %f Mb -> No se esperan lluvias" % (medida)
            else:
                return " H: %f Mb -> Se esperan lluvias" % (medida)
        else:
            return "--"



