"2.	Queremos conocer el importe neto de un préstamo. Para ello debemos pedirle al cliente el importe a solicitar así como el número de cuotas en que quiere devolverlo."
"Calcula el importe total, así como la mensualidad que le quedará al cliente sabiendo que:"
"Importe_total=capital_solicitado + intereses."
"Intereses=5% del capital solicitado."

solicitud = input("¿Cual es el importe que deseas pedir?");

cuotas = input("¿En cuantas cuotas lo pagarias?");

total = float(solicitud)*float(1.05);

print("El importe a pagar es de", total, " €, por tanto debe pagar ", total/float(cuotas), " por cuota ");
