class Material ():

    #constructor
    def __init__(self, identificador, titulo, descripcion, numEjemplares):
        self.identificador = identificador #int
        self.titulo = titulo #String
        self.descripcion = descripcion #String
        self.numEjemplares = numEjemplares #int
        self.disponible = False #boolean
        self.prestamo = 0 #int

    #metodos
    def siDisponible(self):
        self.disponible = True

    def noDisponible(self):
        self.disponible = False

class Libro (Material):

    #constructor
    def __init__(self, identificador, titulo, descripcion, numEjemplares, editorial):
        Material.__init__(self, identificador, titulo, descripcion, numEjemplares)
        self.editorial = editorial #String
        self.prestamo = 7  # int

class Pelicula(Material):

    # constructor
    def __init__(self, identificador, titulo, descripcion, numEjemplares, director, actorPrincipal, anioPublicacion, genero):
        Material.__init__(self, identificador, titulo, descripcion, numEjemplares)
        self.director = director  # String
        self.actorPrincipal = actorPrincipal  # String
        self.anioPublicacion = anioPublicacion  # int
        self.genero = genero  # String
        self.prestamo = 3  # int

class Revista(Material):

    # constructor
    def __init__(self, identificador, titulo, descripcion, numEjemplares, tematica, mes, anio):
        Material.__init__(self, identificador, titulo, descripcion, numEjemplares)
        self.tematica = tematica  # String
        self.mes = mes #String
        self.anio = anio #int
        self.prestamo = 10  # int

