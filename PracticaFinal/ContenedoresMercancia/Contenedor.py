class Contenedor ():

    #constructor
    def __init__(self, identificador, capacidad):
        self.identificador = identificador #int
        self.capacidad = capacidad #int
        self.mercancias = [] #array de mercancias
        self.abierto = False #boolean

    #metodos
    def abrirContenedor(self):
        self.abierto = True

    def cerrarContenedor(self):
        self.abierto = False

    def addMercancia(self, nuevaMercancia):
        if self.abierto:
            volumenTotal = 0
            for merca in self.mercancias:
                volumenTotal = volumenTotal + merca.volumen()

            if volumenTotal + nuevaMercancia.volumen() < self.capacidad:
                self.mercancias.append(nuevaMercancia)
            else:
                print("El objeto no cabe en el contenedor")

        else:
            print("El contenedor se encuentra cerrado")

    #toString()
    def __str__(self):
        return " Contenedor %s --> capacidad: %s, numero de mercancias: %s, abierto o cerrado: %s" % (str(self.capacidad), str(len(self.mercancias)), str(self.abierto))