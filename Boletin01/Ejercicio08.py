"8. Crea un programa que calcule el interés de un préstamo para una entidad bancaria. Se deberá pedir al usuario el importe que desea solicitar, y a razón de éste se aplicará:"

"* 20% si el importe está comprendido entre 500 y 1500€"
"* 15% si el importe está comprendido entre 1501 y 3000€"
"* 12% si el importe está entre 3001 y 6000€"
"* 10% si el importe es superior a 6000€"

"A criterio del agente que gestione el préstamo se le puede aplicar un descuento a “familiares/amigos” del 3%, así el programa deberá preguntar si se desea aplicar dicho descuento."
"Por último, el programa deberá proporcionar el importe total del préstamo: capital + intereses. Y la cantidad de intereses que incluye."
"Al finalizar la ejecución el programa deberá preguntar al agente si desea realizar más simulaciones, si se responde si deberá volver al inicio, y si se responde no deberá finalizar su ejecución."

"El comercial hara el descuento amigo familiar"
descuento = 0;
while descuento != 1 or descuento != 2:
    descuento = input("¿El agente va a aplicar el descuento del 3%?     1.SI     2.NO  ");

"Cual es el importe del prestamo"
finished = False;
while not finished:
    prestamo = input("¿Cual es el importe del prestamo solicitado?");
    if not isinstance(prestamo, int):
        print("ATENCIÓN: Debe ingresar un número entero.");
    else:
        finished = True;
