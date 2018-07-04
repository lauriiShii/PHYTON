from Examen.Trabajador import Responsable

class Taller():

    # constructor
    def __init__(self, identificador, nombre, especialidad, localidad):
        self.identificador = identificador  # int
        self.nombre = nombre # String
        self.especialidad = especialidad # String
        self.localidad = localidad # String
        self.numPuestos = 5 # int
        self.responsablre = Responsable(0,"","","",1, 1)