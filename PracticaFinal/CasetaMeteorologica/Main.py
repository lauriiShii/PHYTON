"""Una caseta meteorológica está equipada con distintos aparatos de observación:
Termómetro (para medir la temperatura), barómetro (para medir la presión atmosférica), etc.
A lo largo del día se hace la observación, esto es, se leen los valores de cada uno de los aparatos para su registro.
La observación de cada uno de los aparatos está formada por un identificador del aparato, el valor numérico de la medida y la unidad de dicha medida.
Por ejemplo, “T: 34,6 ºC” en el caso del termómetro o “H: 7,4 Mb” en el caso del barómetro.
La caseta debe ofrecer un método para devolver una cadena con la lectura de las observaciones de los aparatos.

    a) Implementa el método que devuelva la observación de los aparatos (termómetro y el barómetro).
    b) El método getObservaciones de la clase que representa la caseta meteorológica (CasetaMeteo)
    devuelve una cadena de texto que incluye en primer lugar la fecha en la que se realiza la llamada
    seguida de las observaciones de los aparatos. Por ejemplo, “01/07/2009 T: 34,6 ºC – H: 7,4 Mb”.
    El formato de las fechas varía en función de la caseta. Por ejemplo, entre otros, una caseta podría
    tomar el formato abreviado “01/07/2009” mientras que otra caseta podría tomar el formato inglés “07/01/2009”.
    Al instalarse una caseta meteorológica se establece el formato de las fechas para las observaciones.

    Implementa la clase CasetaMeteo y todos los tipos que sean necesarios para conseguir la funcionalidad propuesta.
    Escribe el código que construya una caseta con el formato de fecha abreviado.

    c) Dado que los aparatos se encuentran instalados de forma externa, puede que al solicitar la observación del
    aparato exista algún error en la transmisión de los datos. En el caso de que se produzca un fallo en la observación se intentará
    la lectura una segunda vez. Si esta segunda vez tampoco es posible obtener la medida del aparato, se anotará en la lectura
    la cadena “--” para indicar que no se tomó la medida de ese aparato.

    Modifica el método getObservaciones de la clase CasetaMeteo para gestionar los fallos y reintentos descritos.

    d) Se puede considerar que existe probabilidad de lluvia cuando se produce un descenso significativo de l
    a presión atmosférica. Los barómetros, que son los encargados de medir la presión, podrían determinar si la presión actual
    ha descendido más de un determinado valor umbral desde la última observación. Esta situación puede consultarse mediante el
    método existeProbabilidadLluvia. Modifica el método getObservaciones de la clase CasetaMeteo de manera que se aproveche el
    momento en el que se obtienen las observaciones de los aparatos para que en la caseta se registre si existe probabilidad de lluvia.
    Supondremos que hay probabilidad de lluvia si alguno de los barómetros indica esta situación.

    e) Como resultado del trabajo de la caseta meteorológica se debe obtener un log donde se vayan anotando todas las medidas.

Ejemplo de examen: implementa la clase fecha e inclúyela en el funcionamiento de las casetas meteorológicas.

Continuará…
"""
from CasetaMeteorologica.CasetaMeteo import CasetaMeteo
from CasetaMeteorologica.Aparatos import Termometro
from CasetaMeteorologica.Aparatos import Barometro
import CasetaMeteorologica.Fecha
import Funciones

casetas = []


def mayorId():
    id = 0
    for b in casetas:
        if b.identificador > id:
            id = b.identificador
    return id


def existeId(id):
    for b in casetas:
        if b.identificador == id:
            return True
    return False

def addCaseta ():
    tipoFecha = CasetaMeteorologica.Fecha.dameTipoFecha()
    caseta = CasetaMeteo(mayorId()+1, tipoFecha)
    casetas.append(caseta)

def obtenerInforme():
    id = Funciones.escribeEntero("Id de la caseta que deseas obtener el informe: ")
    if existeId(id):
        for caseta in casetas:
            caseta.getObservaciones()
    else:
        print("El id no existe")

def probabilidadLluvia():
    id = Funciones.escribeEntero("Id de la caseta que deseas obtener el informe de un barometro: ")
    if existeId(id):
        for caseta in casetas:
            caseta.getObservaciones()
    else:
        print("El id no existe")

def addMaterial():
    id = Funciones.escribeEntero("Id de la caseta que deseas obtener el informe de un barometro: ")
    if existeId(id):
        opcion = Funciones.lee_opcion("T - Termometro\nH - Barometro\n", ["T","H"])
        for caseta in casetas:
            if opcion == "T":
                aparato = Termometro(caseta.mayorId())
                caseta.addAparato(aparato)
            else:
                aparato = Barometro(caseta.mayorId())
                caseta.addAparato(aparato)
    else:
        print("El id no existe")

def menu ():
    salir = False
    while (not salir):
        print("MENU PRINCIPAL: ")
        print("1. Agregar una caseta")
        print("2. Recoger datos casetas")
        print("3. Probabilidades de lluvia")
        print("4. Agregar material")
        print("5. Salir")
        opcion = Funciones.escribeEntero("Introduce una opcion (1 - 5): ")

        if opcion < 1 or opcion > 5:
            print("ERROR: No has introducido un valor valido")
        else:
            if opcion == 1:
                addCaseta()
            if opcion == 2:
                obtenerInforme()
            if opcion == 3:
                probabilidadLluvia()
            if opcion == 4:
                addMaterial()
            if opcion == 5:
                salir = True
                print("Fin del programa.")

        print("\n\n")

def main():
    menu()

if __name__ == '__main__':
    main();






