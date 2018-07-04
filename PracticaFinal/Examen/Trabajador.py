class Trabajador():
    # constructor
    def __init__(self, identificador, nombre, apellidos, DNI):
        self.identificador = identificador  # int
        self.nombre = nombre  # String
        self.apellidos = apellidos  # String
        self.DNI = DNI  # String
        self.activo = False  # boolean
        self.tlf = 0  # int
        self.email = ""  # String
        self.preferencia = ""  # String
        self.numSeguridad = 0  # int

class Responsable(Trabajador):

    def __init__(self, identificador, nombre, apellidos, DNI, tlf, numSeguridad):
        Trabajador.__init__(self, identificador, nombre, apellidos, DNI)
        self.activo = False  # boolean
        self.tlf = 0  # int
        self.email = ""  # String
        self.preferencia = ""  # String
        self.numSeguridad = 0  # int