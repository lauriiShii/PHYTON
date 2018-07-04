import Funciones
from CasetaMeteorologica.Aparatos import Barometro

class CasetaMeteo ():

    #constructor
    def __init__(self, identificador, tipoFecha):
        self.identificador = identificador #int
        self.tipoFecha = tipoFecha #String
        self.aparatos = []

    #metodos
    def getObservaciones(self):
        import time
        fecha = str(time.strftime(self.tipoFecha))
        cadena = str(fecha)+"->"
        for aparato in self.aparatos:
            cadena = cadena + aparato.observacion()
        fichero = open("Observaciones.txt", "w+")
        fichero.write(cadena)
        fichero.close()
        print(cadena)

    def mayorId(self):
        id = 0
        for b in self.aparatos:
            if b.identificador > id:
                id = b.identificador
        return id

    def addAparato(self, nuevoAparato):
        self.aparatos.append(nuevoAparato)

    def valorBarometro(self):
        id =  Funciones.escribeEntero("Id del barometro: ")
        for b in self.aparatos:
            if b.identificador == id and isinstance(b, Barometro):
                b.observacion()
            else:
                print("No existe el id indicado como barometro")
