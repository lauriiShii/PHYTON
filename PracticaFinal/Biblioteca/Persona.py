class Persona():
    # constructor
    def __init__(self, identificador, nombre, apellidos):
        self.identificador = identificador  # int
        self.titulo = nombre  # String
        self.descripcion = apellidos  # String

class Usuario(Persona):
    # constructor
    def __init__(self, identificador, nombre, apellidos):
        Persona.__init__(self, identificador, nombre, apellidos)
        self.tienePrestamo = False #booblean

    #metodos
    def siPrestamo (self):
        self.ienePrestamo = True

    def noPrestamo (self):
        self.ienePrestamo = False

class Trabajador(Persona):
    # constructor
    def __init__(self, identificador, nombre, apellidos):
        Persona.__init__(self, identificador, nombre, apellidos)