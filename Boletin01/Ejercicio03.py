"3.	Crea un script que pida 3 valores y que te muestre la media, el máximo y el mínimo."

num1 = input("¿Cual es el num1?");
num2 = input("¿Cual es el num2?");
num3 = input("¿Cual es el num3?");

print("media", int(num1+num2+num3)/3);
print("max", max(num1, num2, num3));
print("min", min(num1, num2, num3));