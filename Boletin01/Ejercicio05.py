".	En un sistema de control de multas se quiere premiar a los sancionados que abonen pronto su sanción. Para ello se establece el siguiente sistema:"
import switch as switch

"•	Los que paguen su multa al día siguiente de la sanción se reducirá su cuantía en 50%"
"•	Los que paguen al segundo día 25%"
"•	Los que paguen al tercer día 10%"
"•	A partir del cuarto día pagarán el importe completo."

"Crea una aplicación que pida al usuario el importe de su multa y los días que hace que la recibió para calcular su importe final."


importe = input("¿Cual es el importe de la multa?");

dias = int(input("¿Cuantos dias han pasado de la sancion?"));

if dias == 0 or dias == 1:
    print("pagas : ", float(importe)*1.5);
elif dias == 2:
    print("pagas : ", float(importe)*1.25);
elif dias == 3:
    print("pagas : ", float(importe)*1.1);
else:
    print("la respuesta no es valida");
