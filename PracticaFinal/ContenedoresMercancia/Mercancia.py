class Mercancia():
    # Volumen : va a ser redefinido en la herencia
    def volumen(self):
        pass


class Caja(Mercancia):
    def __init__(self, ancho, alto, fondo):
        self.ancho = ancho  # int
        self.alto = alto  # int
        self.fondo = fondo  # int

    def volumen(self):
        return self.ancho * self.alto * self.fondo

        # toString()
        def __str__(self):
            return " Caja --> ancho: %s, alto: %s, fondo: %s, volumen: %s" % (
            str(self.ancho), str(self.alto), str(self.fondo), str(self.ancho * self.alto * self.fondo))


class Cubo(Mercancia):
    def __init__(self, lado):
        self.lado = lado  # int

    def volumen(self):
        return self.lado * self.lado * self.lado

        # toString()
        def __str__(self):
            return " Caja --> lado: %s, volumen: %s" % (str(self.lado), str(self.lado * self.lado * self.lado))
